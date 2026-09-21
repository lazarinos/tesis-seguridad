# Plan Técnico Persistente del Agente

## 1. Contexto y Objetivos
El proyecto corresponde a la tesis titulada:
*Detección de intrusiones de red con aprendizaje automático y técnicas de explicabilidad (XAI) para pequeñas y medianas empresas de Juliaca, Puno*, desarrollada por Fernando Ccolla Lazarinos en el marco del curso Seminario de Tesis II (2026-II), Escuela Profesional de Ingeniería de Software y Sistemas, Universidad Nacional de Juliaca.

## 2. Decisiones Arquitectónicas de Datos
- **Dataset Principal:** GeNIS 2025 (*GECAD Network Intrusion Scenarios*), disponible en Zenodo (DOI 10.5281/zenodo.14919237). Se emplearán las particiones preprocesadas oficiales de ventana temporal de 30 segundos (`genis-30-sec-train.csv` y `genis-30-sec-test.csv`).
- **Dataset de Contraste Independiente:** CICIDS2017 (Canadian Institute for Cybersecurity, UNB), espejo verificado en Hugging Face (`bencorn/CICIDS2017`, `MachineLearningCSV.zip`). Se construirá un subconjunto estratificado de 100 000 registros con semilla 42 para evaluación de generalización sin afectar la selección del modelo.
- **Modelos Evaluados:** Random Forest (RF), XGBoost (XGB) y Multilayer Perceptron (MLP).
- **Métrica Principal:** F1 Macro en Stratified 5-Fold Cross Validation con semilla 42.

## 3. Plan de Carpetas y Trazabilidad
```text
tesis-seguridad/
├── docs/
│   ├── agent/                 # Memoria persistente del agente
│   └── protocol/              # Documentos metodológicos maestros
├── datasets/                  # Almacenamiento local de datasets
│   ├── genis/
│   └── cicids2017/
├── scripts/                   # Scripts utilitarios reproducibles
├── tesis_experimentos/        # Árbol estandarizado de evidencias (Protocolo V1.0)
│   ├── 00_protocol/
│   ├── 01_data_metadata/
│   ├── 02_audit/
│   ├── 03_splits/
│   ├── 04_configs/
│   ├── 05_logs/
│   ├── 06_models/
│   ├── 07_predictions/
│   ├── 08_metrics/
│   ├── 09_shap/
│   ├── 10_prototype/
│   ├── 11_usability/
│   └── 12_reports/
```
