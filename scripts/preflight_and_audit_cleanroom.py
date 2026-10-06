"""
Pre-flight, Auditoria de Hardware Real, Software Lock y Calidad de Datos (GeNIS 2025)
Corrida Limpia: RUN_REPRO_V2_03_CLEANROOM
Protocolo de Investigacion V2 - Seminario de Tesis II
"""
import os
import sys
import json
import csv
import io
import zipfile
import hashlib
import platform
import subprocess
import psutil
import pandas as pd
import numpy as np

RUN_ID = "RUN_REPRO_V2_03_CLEANROOM"
BASE_DIR = os.path.join("tesis_experimentos", "runs", RUN_ID)

SUBDIRS = [
    "00_protocol", "01_environment", "02_audit", "03_splits",
    "04_cv", "05_models", "06_predictions", "07_metrics",
    "08_shap", "09_cicids", "10_cross_dataset", "11_report"
]

def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(1024 * 1024):
            h.update(chunk)
    return h.hexdigest()

def get_real_hardware():
    # CPU
    cpu_name = platform.processor()
    try:
        ps_cpu = subprocess.check_output(
            ["powershell", "-Command", "Get-CimInstance Win32_Processor | Select-Object -ExpandProperty Name"],
            text=True
        ).strip()
        if ps_cpu:
            cpu_name = ps_cpu
    except Exception:
        pass
        
    cores_phys = psutil.cpu_count(logical=False)
    cores_log = psutil.cpu_count(logical=True)
    ram_gb = round(psutil.virtual_memory().total / (1024**3), 2)
    
    # Disks
    disks = []
    try:
        ps_disk = subprocess.check_output(
            ["powershell", "-Command", "Get-CimInstance Win32_DiskDrive | Select-Object Model, MediaType, Size | ConvertTo-Json"],
            text=True
        ).strip()
        if ps_disk:
            disk_data = json.loads(ps_disk)
            if isinstance(disk_data, dict):
                disk_data = [disk_data]
            for d in disk_data:
                model = d.get("Model", "UNKNOWN")
                media = d.get("MediaType", "Fixed hard disk media")
                sz_gb = round(float(d.get("Size", 0)) / (1024**3), 2)
                disks.append({"model": model, "media_type": media, "size_gb": sz_gb})
    except Exception:
        pass

    return {
        "cpu": {
            "name": cpu_name,
            "physical_cores": cores_phys,
            "logical_cores": cores_log,
            "architecture": platform.machine()
        },
        "ram_gb": ram_gb,
        "storage": disks,
        "os": {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version()
        }
    }

def get_software_lock():
    import sklearn, xgboost, shap, imblearn, flask
    packages = {
        "python": platform.python_version(),
        "scikit-learn": sklearn.__version__,
        "xgboost": xgboost.__version__,
        "shap": shap.__version__,
        "imbalanced-learn": imblearn.__version__,
        "pandas": pd.__version__,
        "numpy": np.__version__,
        "psutil": psutil.__version__,
        "flask": flask.__version__
    }
    return packages

def compute_environment_id(hw_dict, sw_dict):
    raw_str = json.dumps({"hardware": hw_dict, "software": sw_dict}, sort_keys=True)
    return f"ENV_{hashlib.sha256(raw_str.encode('utf-8')).hexdigest()[:12]}"

def main():
    print(f"=== INICIANDO PRE-FLIGHT Y AUDITORÍA: {RUN_ID} ===")
    
    # 1. Crear directorios
    for sd in SUBDIRS:
        os.makedirs(os.path.join(BASE_DIR, sd), exist_ok=True)
    print(f"Directorios creados en: {BASE_DIR}")
    
    # 2. Hardware Real & Software Lock
    hw = get_real_hardware()
    sw = get_software_lock()
    env_id = compute_environment_id(hw, sw)
    print(f"Environment ID generado: {env_id}")
    print(f"CPU Real: {hw['cpu']['name']} ({hw['cpu']['logical_cores']} hilos)")
    print(f"RAM Total: {hw['ram_gb']} GB")
    
    with open(os.path.join(BASE_DIR, "01_environment", "hardware_profile.json"), "w", encoding="utf-8") as f:
        json.dump(hw, f, indent=2)
        
    with open(os.path.join(BASE_DIR, "01_environment", "software_lock.json"), "w", encoding="utf-8") as f:
        json.dump({"environment_id": env_id, "packages": sw}, f, indent=2)

    # 3. Hashes de Datasets
    print("\nCalculando hashes SHA-256 de datasets oficiales...")
    datasets_info = []
    
    genis_train_path = os.path.join("datasets", "genis", "genis-30-sec-train.csv")
    genis_test_path = os.path.join("datasets", "genis", "genis-30-sec-test.csv")
    
    if os.path.exists(genis_train_path):
        datasets_info.append({
            "dataset": "GeNIS_2025",
            "file": "genis-30-sec-train.csv",
            "size_bytes": os.path.getsize(genis_train_path),
            "sha256": sha256_file(genis_train_path)
        })
    if os.path.exists(genis_test_path):
        datasets_info.append({
            "dataset": "GeNIS_2025",
            "file": "genis-30-sec-test.csv",
            "size_bytes": os.path.getsize(genis_test_path),
            "sha256": sha256_file(genis_test_path)
        })
        
    cicids_dir = os.path.join("datasets", "cicids2017")
    if os.path.exists(cicids_dir):
        for cfile in sorted(os.listdir(cicids_dir)):
            if cfile.endswith(".csv"):
                cpath = os.path.join(cicids_dir, cfile)
                datasets_info.append({
                    "dataset": "CICIDS2017",
                    "file": cfile,
                    "size_bytes": os.path.getsize(cpath),
                    "sha256": sha256_file(cpath)
                })
                
    df_hashes = pd.DataFrame(datasets_info)
    df_hashes.to_csv(os.path.join(BASE_DIR, "01_environment", "dataset_files_hashes.csv"), index=False)
    print(f"Hashes guardados para {len(datasets_info)} archivos de datasets.")
    
    # 4. Auditoría de Calidad y Duplicados de GeNIS
    print("\nAuditoría exhaustiva de calidad de datos GeNIS 2025...")
    df_train = pd.read_csv(genis_train_path)
    df_test = pd.read_csv(genis_test_path)
    
    num_cols = df_train.select_dtypes(include=[np.number]).columns.tolist()
    
    # Missing e Infinitos
    missing_train = int(df_train.isna().sum().sum())
    missing_test = int(df_test.isna().sum().sum())
    
    inf_train = int(np.isinf(df_train[num_cols].to_numpy()).sum())
    inf_test = int(np.isinf(df_test[num_cols].to_numpy()).sum())
    
    # Duplicados intra-split
    dup_train_intra = int(df_train.duplicated().sum())
    dup_test_intra = int(df_test.duplicated().sum())
    
    print(f"Train - Filas: {len(df_train):,}, Faltantes: {missing_train}, Infinitos: {inf_train}, Duplicados Intra: {dup_train_intra:,}")
    print(f"Test  - Filas: {len(df_test):,}, Faltantes: {missing_test}, Infinitos: {inf_test}, Duplicados Intra: {dup_test_intra:,}")
    
    # Duplicados cruzados Train <-> Test (exact duplicates)
    print("Buscando solapamiento exacto de flujos Train <-> Test...")
    feature_cols = [c for c in df_train.columns if c not in ["record_id", "BinaryLabel", "CategoryLabel", "SubCategoryLabel"]]
    
    train_row_hashes = set(pd.util.hash_pandas_object(df_train[feature_cols], index=False))
    test_row_hashes = pd.util.hash_pandas_object(df_test[feature_cols], index=False)
    
    mask_in_train = test_row_hashes.isin(train_row_hashes)
    cross_split_duplicates = int(mask_in_train.sum())
    cross_split_overlap_pct = round(100.0 * cross_split_duplicates / len(df_test), 4)
    
    print(f"Solapamiento exacto Train <-> Test: {cross_split_duplicates:,} flujos ({cross_split_overlap_pct}%)")
    
    # Distribución de clases usando CategoryLabel oficial
    train_dist = df_train["CategoryLabel"].value_counts().to_dict()
    test_dist = df_test["CategoryLabel"].value_counts().to_dict()
    
    audit_genis = {
        "run_id": RUN_ID,
        "environment_id": env_id,
        "train_rows": len(df_train),
        "test_rows": len(df_test),
        "total_rows": len(df_train) + len(df_test),
        "columns_count": len(df_train.columns),
        "missing_values": {"train": missing_train, "test": missing_test},
        "infinite_values": {"train": inf_train, "test": inf_test},
        "intra_split_duplicates": {"train": dup_train_intra, "test": dup_test_intra},
        "cross_split_exact_duplicates": cross_split_duplicates,
        "cross_split_overlap_pct": cross_split_overlap_pct,
        "train_class_distribution": train_dist,
        "test_class_distribution": test_dist,
        "sensitivity_test_size_without_train_duplicates": len(df_test) - cross_split_duplicates
    }
    
    with open(os.path.join(BASE_DIR, "02_audit", "dataset_audit_genis.json"), "w", encoding="utf-8") as f:
        json.dump(audit_genis, f, indent=2)
    print("Guardado: 02_audit/dataset_audit_genis.json")
    
    # 5. Auditoría Semántica de Características contra Diccionario Oficial
    print("\nAuditoría semántica de características contra diccionario oficial...")
    zip_0info = os.path.join("datasets", ".cache", "0-info.zip")
    genis_feat_dict = {}
    if os.path.exists(zip_0info):
        with zipfile.ZipFile(zip_0info, "r") as z:
            if "0-info/genis-features.csv" in z.namelist():
                with z.open("0-info/genis-features.csv") as zf:
                    text_stream = io.TextIOWrapper(zf, encoding="utf-8", errors="replace")
                    reader = csv.reader(text_stream)
                    header = next(reader, None)
                    for row in reader:
                        if len(row) >= 3:
                            genis_feat_dict[row[0].strip()] = {
                                "type": row[1].strip(),
                                "desc": row[2].strip()
                            }
                        elif len(row) == 2:
                            genis_feat_dict[row[0].strip()] = {
                                "type": row[1].strip(),
                                "desc": ""
                            }
                            
    all_features = [c for c in df_train.columns if c not in ["BinaryLabel", "CategoryLabel", "SubCategoryLabel"]]
    semantic_records = []
    
    for c in all_features:
        info = genis_feat_dict.get(c, {"type": "Continuous/Discrete", "desc": "Característica de flujo Argus"})
        defn = info["desc"]
        ftype = info["type"]
        c_lower = c.lower()
        
        if c in ["Sport", "Dport"]:
            risk = "PORT_TOPOLOGY"
            decision = "EXCLUDED_BY_PROTOCOL"
            just = "Puerto de red excluido según Protocolo V2 §3.6 para evitar memorización topológica."
        elif c in ["FlowID", "Rank", "Offset", "Seq"]:
            risk = "IDENTIFIER_SEQUENCE"
            decision = "EXCLUDED_BY_PROTOCOL"
            just = "Identificador o número de secuencia secuencial excluido."
        elif c in ["StartTime", "LastTime"]:
            risk = "TIMESTAMP"
            decision = "EXCLUDED_BY_PROTOCOL"
            just = "Marca temporal absoluta excluida para evitar sesgo de orden temporal."
        elif "proto_" in c_lower or "flgs_" in c_lower or "state_" in c_lower:
            risk = "BEHAVIORAL_CATEGORICAL_OHE"
            decision = "KEPT_CANDIDATE"
            just = "Variable categórica de protocolo, banderas TCP o estado de conexión codificada en One-Hot."
        elif c in ["Sdaddr", "Ssaddr"]:
            risk = "TOPOLOGICAL_HOST_COUNT"
            decision = "KEPT_CANDIDATE_DOCUMENTED"
            just = "En Argus/GeNIS representa conteo agregado de direcciones de hosts activos en la ventana de 30s (comportamiento de abanico DoS/Scan), no una IP fija."
        else:
            risk = "BEHAVIORAL_METRIC"
            decision = "KEPT_CANDIDATE"
            just = "Estadística conductual de flujo legítima (duración, tasa de bytes/paquetes, RTT, TTL, jitter, etc.)."
            
        semantic_records.append({
            "feature": c,
            "argus_type": ftype,
            "definition": defn,
            "risk_type": risk,
            "decision": decision,
            "justification": just
        })
        
    df_sem = pd.DataFrame(semantic_records)
    df_sem.to_csv(os.path.join(BASE_DIR, "02_audit", "feature_semantic_audit.csv"), index=False)
    print(f"Auditoría semántica guardada para {len(semantic_records)} características.")
    print("=== PRE-FLIGHT Y AUDITORÍA COMPLETADOS EXITOSAMENTE ===")

if __name__ == "__main__":
    main()
