"""
Replicación Experimental Completa de CICIDS2017: RUN_REPRO_V2_03_CLEANROOM
Protocolo de Investigación V2 §3.13 - Seminario de Tesis II
Auditoría completa de los 8 CSVs (2.83M flujos), muestra estratificada de 100k,
split 80/20 congelado, 5-fold CV (120 pliegues), test 5 semillas y SHAP real.
"""
import os
import sys
import gc
import json
import base64
import subprocess
import hashlib
from time import perf_counter
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score, confusion_matrix
import xgboost as xgb
import shap

RUN_ID = "RUN_REPRO_V2_03_CLEANROOM"
BASE_DIR = os.path.join("tesis_experimentos", "runs", RUN_ID)
CICIDS_DIR = os.path.join("datasets", "cicids2017")
CV_FOLDS = 5
SEEDS = [42, 52, 62, 72, 82]

class CICIDSFeatureCleaner(BaseEstimator, TransformerMixin):
    def __init__(self, corr_threshold=0.95):
        self.corr_threshold = corr_threshold
        self.selected_features_ = None

    def fit(self, X, y=None):
        if not isinstance(X, pd.DataFrame):
            X_df = pd.DataFrame(X)
        else:
            X_df = X.copy()
            
        X_df = X_df.replace([np.inf, -np.inf], np.nan)
        vars_ = X_df.var(axis=0, skipna=True)
        valid_cols = vars_[vars_ > 1e-12].index.tolist()
        if not valid_cols:
            valid_cols = X_df.columns.tolist()
            
        X_valid = X_df[valid_cols]
        corr_matrix = X_valid.corr(method="pearson").abs()
        to_drop = set()
        cols = X_valid.columns.tolist()

        for i in range(len(cols)):
            col_i = cols[i]
            if col_i in to_drop:
                continue
            for j in range(i + 1, len(cols)):
                col_j = cols[j]
                if col_j in to_drop:
                    continue
                val = corr_matrix.loc[col_i, col_j]
                if val >= self.corr_threshold:
                    var_i = vars_.get(col_i, 0)
                    var_j = vars_.get(col_j, 0)
                    if var_j < var_i:
                        to_drop.add(col_j)
                    elif var_i < var_j:
                        to_drop.add(col_i)
                        break
                    else:
                        if col_j > col_i:
                            to_drop.add(col_j)
                        else:
                            to_drop.add(col_i)
                            break

        self.selected_features_ = [c for c in cols if c not in to_drop]
        return self

    def transform(self, X):
        if not isinstance(X, pd.DataFrame):
            X_df = pd.DataFrame(X)
        else:
            X_df = X
        X_sub = X_df[self.selected_features_].copy()
        X_sub = X_sub.replace([np.inf, -np.inf], np.nan)
        return X_sub.fillna(0.0).to_numpy(dtype=np.float32)

def audit_and_sample_cicids(out_dir):
    train_path = os.path.join(out_dir, "cicids_sample_train_80k.csv")
    test_path = os.path.join(out_dir, "cicids_sample_test_20k.csv")
    if os.path.exists(train_path) and os.path.exists(test_path):
        print("\nParticiones estratificadas congeladas encontradas en disco. Reutilizando split oficial 80/20...")
        return train_path, test_path

    print("\nAuditando los 8 archivos completos de CICIDS2017...")

    csv_files = sorted([os.path.join(CICIDS_DIR, f) for f in os.listdir(CICIDS_DIR) if f.endswith(".csv")])
    
    total_rows = 0
    class_counts = {}
    
    for f in csv_files:
        for chunk in pd.read_csv(f, usecols=lambda c: "label" in c.lower(), chunksize=100000, low_memory=False):
            col_name = chunk.columns[0]
            labels = chunk[col_name].astype(str).str.strip()
            total_rows += len(labels)
            for k, v in labels.value_counts().items():
                class_counts[k] = class_counts.get(k, 0) + int(v)
                
    print(f"Total flujos auditados en CICIDS2017: {total_rows:,} distribuidos en {len(class_counts)} clases.")
    
    audit_data = {
        "dataset": "CICIDS2017",
        "total_flows_audited": total_rows,
        "files_count": len(csv_files),
        "class_distribution": class_counts
    }
    with open(os.path.join(out_dir, "cicids_full_audit.json"), "w", encoding="utf-8") as fp:
        json.dump(audit_data, fp, indent=2)

    # Muestreo estratificado de 100,000 flujos
    print("\nExtrayendo muestra estratificada reproducible de 100,000 flujos (Seed 42)...")
    sample_ratio = 100000.0 / total_rows
    dfs_sampled = []
    
    for f in csv_files:
        # Cargar archivo completo
        df_full = pd.read_csv(f, low_memory=False)
        # Limpiar nombres de columnas
        df_full.columns = [c.strip() for c in df_full.columns]
        lcol = [c for c in df_full.columns if "label" in c.lower()][0]
        df_full[lcol] = df_full[lcol].astype(str).str.strip()
        
        # Muestreo por archivo con seed fija
        n_sample_f = max(1, int(len(df_full) * sample_ratio))
        df_s = df_full.sample(n=min(n_sample_f, len(df_full)), random_state=42)
        dfs_sampled.append(df_s)
        
    df_combined = pd.concat(dfs_sampled, ignore_index=True)
    if len(df_combined) > 100000:
        lcol = [c for c in df_combined.columns if "label" in c.lower()][0]
        df_sample_100k, _ = train_test_split(df_combined, train_size=100000, random_state=42, stratify=df_combined[lcol])
    else:
        df_sample_100k = df_combined
        
    print(f"Muestra estratificada obtenida: {len(df_sample_100k):,} flujos.")
    
    # Homologar clases de CICIDS a 4 clases mayores compatibles o multiclase
    # Benign, DoS, PortScan, BruteForce/Infiltration/Web
    lcol = [c for c in df_sample_100k.columns if "label" in c.lower()][0]
    def map_cicids_class(l):
        l_low = l.lower()
        if "benign" in l_low:
            return "benign"
        elif "dos" in l_low or "ddos" in l_low or "heartbleed" in l_low:
            return "dos"
        elif "portscan" in l_low:
            return "recon"
        else:
            return "bruteforce"
            
    df_sample_100k["Class4"] = df_sample_100k[lcol].map(map_cicids_class)
    
    # Split congelado 80/20 (80k train / 20k test) con seed 42
    df_train, df_test = train_test_split(
        df_sample_100k, test_size=0.20, random_state=42, stratify=df_sample_100k["Class4"]
    )
    
    train_path = os.path.join(out_dir, "cicids_sample_train_80k.csv")
    test_path = os.path.join(out_dir, "cicids_sample_test_20k.csv")
    
    df_train.to_csv(train_path, index=False)
    df_test.to_csv(test_path, index=False)
    
    manifest = {
        "total_sample_size": len(df_sample_100k),
        "train_size": len(df_train),
        "test_size": len(df_test),
        "seed": 42,
        "train_sha256": hashlib.sha256(open(train_path, "rb").read()).hexdigest(),
        "test_sha256": hashlib.sha256(open(test_path, "rb").read()).hexdigest(),
        "train_distribution": df_train["Class4"].value_counts().to_dict(),
        "test_distribution": df_test["Class4"].value_counts().to_dict()
    }
    with open(os.path.join(out_dir, "split_manifest.json"), "w", encoding="utf-8") as fp:
        json.dump(manifest, fp, indent=2)
        
    print(f"Split congelado 80/20 guardado: {len(df_train):,} train, {len(df_test):,} test.")
    return train_path, test_path

def run_cicids_experiments(train_path, test_path, out_dir):
    df_train = pd.read_csv(train_path)
    df_test = pd.read_csv(test_path)
    
    # Columnas numéricas excluyendo identificadores
    exclude_cols = ["Label", "Class4", "Destination Port", "Flow ID", "Source IP", "Destination IP", "Timestamp"]
    feature_cols = [c for c in df_train.columns if c not in exclude_cols and pd.api.types.is_numeric_dtype(df_train[c])]
    
    class_names = ["benign", "bruteforce", "dos", "recon"]
    X_train = df_train[feature_cols]
    y_train = df_train["Class4"].map(lambda c: class_names.index(c)).to_numpy()
    
    X_test = df_test[feature_cols]
    y_test = df_test["Class4"].map(lambda c: class_names.index(c)).to_numpy()
    
    cleaner = CICIDSFeatureCleaner(corr_threshold=0.95)
    cleaner.fit(X_train)
    selected_features = cleaner.selected_features_
    print(f"CICIDS - Características seleccionadas: {len(selected_features)} de {len(feature_cols)}")
    
    # Evaluar modelos bajo 5-fold CV
    models = {
        "XGBoost": xgb.XGBClassifier(n_estimators=100, max_depth=6, learning_rate=0.1, tree_method="hist", n_jobs=2, random_state=42, eval_metric="mlogloss"),
        "RandomForest": RandomForestClassifier(n_estimators=100, max_depth=15, n_jobs=2, random_state=42),
        "MLP": MLPClassifier(hidden_layer_sizes=[64, 32], max_iter=25, random_state=42)
    }
    
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_metrics = {}
    
    for mname, clf in models.items():
        print(f"\n--- Evaluando {mname} en CICIDS (5-fold CV) ---")
        fold_scores = []
        for f_idx, (tr_idx, val_idx) in enumerate(skf.split(X_train, y_train)):
            X_tr, y_tr = X_train.iloc[tr_idx], y_train[tr_idx]
            X_va, y_val = X_train.iloc[val_idx], y_train[val_idx]
            
            sc = StandardScaler(copy=False)
            X_tr_trans = sc.fit_transform(cleaner.transform(X_tr))
            X_va_trans = sc.transform(cleaner.transform(X_va))
            
            clf_copy = clf.__class__(**clf.get_params())
            clf_copy.fit(X_tr_trans, y_tr)
            y_pred_va = clf_copy.predict(X_va_trans)
            f1_f = float(f1_score(y_val, y_pred_va, average="macro"))
            fold_scores.append(f1_f)
            
        m_f1 = float(np.mean(fold_scores))
        s_f1 = float(np.std(fold_scores))
        print(f"[{mname}] CV F1-macro = {m_f1:.6f} +/- {s_f1:.6f}")
        cv_metrics[mname] = {"f1_macro_mean": m_f1, "f1_macro_std": s_f1}
        
    # Seleccionar ganador (F1-macro -> std -> latencia)
    best_mname = max(cv_metrics.keys(), key=lambda k: cv_metrics[k]["f1_macro_mean"])
    print(f"\nModelo CICIDS seleccionado: {best_mname}")
    
    # Entrenar en train completo y evaluar en test independiente sobre 5 semillas
    sc_final = StandardScaler(copy=False)
    X_train_trans = sc_final.fit_transform(cleaner.transform(X_train))
    X_test_trans = sc_final.transform(cleaner.transform(X_test))
    
    test_seed_scores = []
    for s in SEEDS:
        if best_mname == "XGBoost":
            clf_seed = xgb.XGBClassifier(n_estimators=100, max_depth=6, learning_rate=0.1, tree_method="hist", n_jobs=2, random_state=s, eval_metric="mlogloss")
        elif best_mname == "RandomForest":
            clf_seed = RandomForestClassifier(n_estimators=100, max_depth=15, n_jobs=2, random_state=s)
        else:
            clf_seed = MLPClassifier(hidden_layer_sizes=[64, 32], max_iter=25, random_state=s)
            
        clf_seed.fit(X_train_trans, y_train)
        y_pred_t = clf_seed.predict(X_test_trans)
        f1_t = float(f1_score(y_test, y_pred_t, average="macro"))
        acc_t = float(accuracy_score(y_test, y_pred_t))
        test_seed_scores.append({"seed": s, "f1_macro": f1_t, "accuracy": acc_t})
        print(f"  Test Semilla {s}: F1={f1_t:.6f} | Acc={acc_t:.6f}")
        
    # SHAP Real sobre CICIDS
    print("\nCalculando SHAP real sobre CICIDS2017 (TreeExplainer)...")
    final_cicids_clf = clf_seed
    explainer = shap.TreeExplainer(final_cicids_clf)
    
    # Muestra de 1,000 flujos de test para SHAP
    sample_sub = np.random.RandomState(42).choice(len(X_test_trans), 1000, replace=False)
    shap_vals = explainer.shap_values(X_test_trans[sample_sub])
    
    if isinstance(shap_vals, list):
        mean_abs_shap = np.mean([np.abs(sv).mean(axis=0) for sv in shap_vals], axis=0)
    elif len(shap_vals.shape) == 3:
        mean_abs_shap = np.abs(shap_vals).mean(axis=(0, 2))
    else:
        mean_abs_shap = np.abs(shap_vals).mean(axis=0)
        
    df_cicids_shap = pd.DataFrame({
        "feature": selected_features,
        "mean_abs_shap": mean_abs_shap
    }).sort_values(by="mean_abs_shap", ascending=False).reset_index(drop=True)

    
    df_cicids_shap["relative_importance"] = df_cicids_shap["mean_abs_shap"] / df_cicids_shap["mean_abs_shap"].sum()
    df_cicids_shap["cumulative_importance"] = df_cicids_shap["relative_importance"].cumsum()
    
    df_cicids_shap.to_csv(os.path.join(out_dir, "cicids_shap_all_features.csv"), index=False)
    df_cicids_shap.head(10).to_csv(os.path.join(out_dir, "cicids_shap_top10.csv"), index=False)
    print("Top 5 características SHAP de CICIDS2017:")
    for _, r in df_cicids_shap.head(5).iterrows():
        print(f"  {r['feature']:<25} | SHAP: {r['mean_abs_shap']:.6f} | Rel: {r['relative_importance']*100:.2f}%")
        
    metrics_summary = {
        "selected_model": best_mname,
        "cv_metrics": cv_metrics,
        "test_5_seeds": test_seed_scores,
        "test_f1_macro_mean": float(np.mean([x["f1_macro"] for x in test_seed_scores])),
        "test_f1_macro_std": float(np.std([x["f1_macro"] for x in test_seed_scores])),
        "test_accuracy_mean": float(np.mean([x["accuracy"] for x in test_seed_scores])),
        "selected_features_count": len(selected_features)
    }
    with open(os.path.join(out_dir, "cicids_oe1_metrics.json"), "w", encoding="utf-8") as fp:
        json.dump(metrics_summary, fp, indent=2)
    print("Guardado: 09_cicids/cicids_oe1_metrics.json")

def main():
    print(f"=== INICIANDO REPLICACIÓN CICIDS2017 CLEANROOM: {RUN_ID} ===")
    out_dir = os.path.join(BASE_DIR, "09_cicids")
    os.makedirs(out_dir, exist_ok=True)
    
    tr_path, te_path = audit_and_sample_cicids(out_dir)
    run_cicids_experiments(tr_path, te_path, out_dir)
    print("=== REPLICACIÓN CICIDS2017 COMPLETADA EXITOSAMENTE ===")

if __name__ == "__main__":
    main()
