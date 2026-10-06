# Detección de Intrusiones de Red con Aprendizaje Automático y Explicabilidad (XAI) para PyMES de Juliaca, Puno

**Universidad Nacional de Juliaca**  
**Facultad de Ciencias de la Ingeniería**  
**Escuela Profesional de Ingeniería de Software y Sistemas**  
- **Curso:** Seminario de Tesis II — 2026-II  
- **Docente:** Profa. Dra. (c) Liz Maribel Huancapaza Hilasaca  
- **Tesista:** Fernando Ccolla Lazarinos  
- **Año:** 2026  

---

## 1. Descripción del Proyecto

Investigación cuantitativa y aplicada orientada a resolver la brecha de ciberseguridad en Pequeñas y Medianas Empresas (PyMES) de la ciudad de Juliaca mediante el diseño, implementación y validación experimental de un sistema de detección de intrusiones de red (**NIDS**) basado en aprendizaje automático supervisado (**Random Forest**, **XGBoost** y **Perceptrón Multicapa - MLP**), integrado con un marco de explicabilidad matemática (**TreeSHAP** / *SHapley Additive exPlanations*) traducido a playbooks defensivos operables en menos de 500 ms.

El repositorio se encuentra bajo un estricto protocolo de reproducción limpia en sala limpia (**Cleanroom Protocol V2**), aislando completamente el conjunto de prueba, aplicando selección de características exclusivamente dentro de cada pliegue de entrenamiento (evitando *data leakage*) y congelando todas las reglas metodológicas de decisión antes de la evaluación final.

---

## 2. Resumen de Hallazgos Experimentales Oficiales (`RUN_REPRO_V2_03_CLEANROOM`)

La experimentación oficial definitiva se encuentra sellada criptográficamente en `tesis_experimentos/runs/RUN_REPRO_V2_03_CLEANROOM/`:

| Hipótesis / Objetivo | Métrica Oficial | Umbral de Aprobación | Resultado Obtenido | Estado Empírico |
|---|---|:---:|:---:|:---:|
| **H1: Eficacia de Detección (GeNIS 2025)** | F1-Macro en Test Oficial (5 semillas) | $\ge 0.90$ | **`0.999957 ± 0.000022`** | **CONFIRMADA** (Margen sobresaliente; Accuracy `99.9993%`, 121,586/121,587 aciertos) |
| **H2: Interpretabilidad Cruzada (GeNIS vs CICIDS)** | Similitud de Jaccard $J@5$ sobre conceptos canónicos | $\ge 0.40$ | **`0.0000`** ($J@10 = \text{N/A}$) | **RECHAZADA CON RIGOR** (Evidencia empírica de divergencia entre tráfico IoT 2025 y redes corporativas 2017) |
| **H3: Factibilidad Operativa en PyMES** | Latencia individual de inferencia por flujo | $\le 500\text{ ms}$ | **`18.8774 ms/flujo`** (P95 = 26.54 ms) | **CONFIRMADA** (26.49 veces más rápido que el umbral máximo de tolerancia operativa) |

---

## 3. Estructura Limpia y Organizada del Repositorio

El repositorio ha sido depurado eliminando scripts intermedios y corridas obsoletas, preservando exclusivamente la evidencia y los documentos necesarios para justificar la investigación:

```text
tesis-seguridad/
│
├── README.md                                                # Este documento de referencia y guía de reproducción
│
├── datasets/                                                # Conjuntos de datos auditados e inalterables
│   ├── genis/                                               # Dataset oficial GeNIS 2025 (train: 486k, test: 121k flujos)
│   ├── cicids2017/                                          # Benchmark CICIDS2017 (8 CSVs etiquetados, 2.83M flujos)
│   └── .cache/                                              # Archivos zip de descarga original para comprobación de hashes
│
├── scripts/                                                 # Pipeline oficial de reproducción cleanroom (7 scripts)
│   ├── 01 | preflight_and_audit_cleanroom.py               # Auditoría de hardware real, software lock y duplicados
│   ├── 02 | run_genis_cleanroom.py                          # 5-fold CV (120 pliegues), selección formal, test 5 semillas y SHAP
│   ├── 03 | run_cicids_cleanroom.py                         # Replicación completa sobre 8 CSVs de CICIDS2017 y SHAP real
│   ├── 04 | run_cross_shap_cleanroom.py                     # Contraste de interpretabilidad cruzada H2 (Jaccard sobre SHAP real)
│   ├── 05 | generate_cleanroom_dossier.py                   # Generación dinámica del Dossier Maestro y validación cruzada
│   ├── download_datasets.py                                 # Descarga y verificación automatizada de integridad SHA-256
│   └── upload_to_cloud.py                                   # Sincronización y respaldo en almacenamiento en nube
│
├── tesis_experimentos/                                      # Evidencia experimental oficial limpia
│   └── runs/
│       └── RUN_REPRO_V2_03_CLEANROOM/                       # Corrida oficial aislada y definitiva
│           ├── 00_protocol/                                 # Manifiestos de decisiones congeladas
│           ├── 01_environment/                              # Perfil auditado de hardware y software
│           ├── 02_audit/                                    # Auditoría de duplicados y diccionario de features
│           ├── 03_splits/                                   # Particiones reproducibles
│           ├── 04_cv/                                       # Resultados de los 120 pliegues de validación cruzada
│           ├── 05_models/                                   # Modelos óptimos serializados (.joblib)
│           ├── 06_predictions/                              # Predicciones flujo a flujo con probabilidades e inferencia
│           ├── 07_metrics/                                  # Métricas finales de test ciego y benchmark H3
│           ├── 08_shap/                                     # Valores SHAP globales y casos locales con playbooks
│           ├── 09_cicids/                                   # Replicación completa sobre CICIDS2017
│           ├── 10_cross_dataset/                            # Contraste empírico H2 de interpretabilidad cruzada
│           ├── 11_report/                                   # Revisiones técnicas (OE4 con usuarios: pendiente, siguiente fase)
│           └── manifest_final.json                          # Manifiesto criptográfico de hashes SHA-256 de la corrida
│
├── exposicion/                                              # Diapositivas (.pptx) de la defensa del Protocolo V2
│   └── Defensa_Protocolo_V2_Fernando_Ccolla_Lazarinos.pptx  # 11 diapositivas con notas del orador
│
├── prototype/                                               # Prototipo Flask: alerta + SHAP + playbook
│
├── bibliography/                                            # Acervo de literatura científica en PDF (Artículos y Tesis)
│   ├── seleccionados_final/                                 # Artículos principales de revistas indexadas (Q1/Q2/IEEE)
│   └── nuevos/                                              # Artículos internacionales (P01-P14), nacionales (N01-N07) y locales (L01)
│
└── docs/                                                    # Documentación del proyecto
    ├── protocolo/                                           # Protocolo Maestro V2 (reglas y umbrales congelados)
    │   └── historico/                                       # Metodología y protocolos previos de Tesis II
    ├── reportes/                                            # Dossier Integral Maestro (código, matrices y validaciones)
    ├── marco_teorico/                                       # Marco teórico, matriz de antecedentes, planteamiento y .bib
    └── agent/                                               # Memoria del agente (ROADMAP, PROGRESS, DECISIONS)
```

---

## 4. Pipeline de Reproducción Paso a Paso

Para ejecutar y reproducir íntegramente la experimentación desde la consola (PowerShell en Windows o Bash en Linux):

### Paso 1: Auditoría de Entorno y Calidad de Datos
```powershell
python scripts/preflight_and_audit_cleanroom.py
```
*Detecta el hardware real (CPU, RAM, SSD), genera el identificador único `environment_id` y audita valores faltantes, duplicados y consistencia de las 41 características contra el diccionario oficial.*

### Paso 2: Ejecución del Pipeline Principal (GeNIS 2025)
```powershell
python scripts/run_genis_cleanroom.py
```
*Ejecuta 5-fold CV sobre 486,346 flujos de entrenamiento (120 pliegues evaluando RF, XGBoost y MLP), selecciona el modelo óptimo bajo regla formal (§4.1), evalúa a ciegas el conjunto de test (121,587 flujos) en 5 semillas, mide la latencia individual H3 y genera explicaciones SHAP globales y locales con playbooks defensivos.*

### Paso 3: Replicación Externa (CICIDS2017)
```powershell
python scripts/run_cicids_cleanroom.py
```
*Procesa los 8 CSVs completos de CICIDS2017 (2.83M flujos), genera una muestra estratificada de 100k flujos, ejecuta 5-fold CV, evalúa test en 5 semillas y calcula explicaciones TreeSHAP reales sobre la partición de prueba.*

### Paso 4: Contraste de Interpretabilidad Cruzada (H2)
```powershell
python scripts/run_cross_shap_cleanroom.py
```
*Cruza los valores SHAP reales de GeNIS y CICIDS agrupándolos por conceptos de red homologables, calculando el coeficiente de Jaccard $J@5$ de forma 100% empírica.*

### Paso 5: Generación del Dossier Integral y Manifiesto
```powershell
python scripts/generate_cleanroom_dossier.py
```
*Valida dinámicamente la consistencia de predicciones y matrices de confusión, genera el reporte maestro `REPORTE_DEFINITIVO_EXPERIMENTOS_TESIS.md` en el Escritorio del usuario y en `docs/reportes/`, y emite el manifiesto criptográfico de hashes `manifest_final.json`.*

---

## 5. Garantías de Reproducibilidad y Cero Fuga de Datos (*No Data Leakage*)

1. **Aislamiento Estricto del Conjunto de Prueba:** El archivo `genis-30-sec-test.csv` (121,587 flujos) se mantuvo bloqueado durante todo el ajuste de hiperparámetros y selección de variables, abriéndose únicamente para la evaluación final tras congelar el modelo ganador.
2. **Transformaciones en Pliegues:** La imputación, selección de variables no colineales (`FoldFeatureSelector`, correlación $< 0.95$) y escalado se ajustaron exclusivamente dentro de los pliegues de entrenamiento de cada pliegue de validación cruzada.
3. **Cero Heurísticas Arbitrarias:** Todos los criterios de aceptación, márgenes de tolerancia de empate estadístico ($\Delta \text{F1} \le 0.005$) y desempate por estabilidad de varianza ($\sigma$) fueron definidos a priori en el Protocolo V2.
4. **Verificación Criptográfica:** Todos los datasets de entrada y artefactos de salida cuentan con sus firmas digitales SHA-256 registradas en `manifest_final.json`.
