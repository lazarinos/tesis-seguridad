# Registro de Decisiones de Arquitectura y Metodología (DECISIONS.md)

## DEC-001: Selección de Fuentes Oficiales y Espejos para Datasets
- **Fecha:** 2026-09-21
- **Decisión:** 
  1. Para GeNIS 2025: utilizar el endpoint de la API REST de Zenodo (`https://zenodo.org/api/records/14919237/files/4-preprocessed.zip/content`) que proporciona acceso directo y sin bloqueo 403 al archivo de flujos preprocesados de 30s.
  2. Para CICIDS2017: utilizar el espejo público verificado de Hugging Face (`https://huggingface.co/datasets/bencorn/CICIDS2017/resolve/main/csvs/MachineLearningCSV.zip`), que permite descarga de alta velocidad de los CSVs generados por UNB CIC.
- **Razón:** Los enlaces antiguos de Google Drive estaban caídos/inactivos, impidiendo la reproducibilidad requerida por Tesis II.

## DEC-002: Estructura de Carpetas de Evidencias Conforme al Protocolo V1.0
- **Fecha:** 2026-09-21
- **Decisión:** Adoptar la estructura fija `tesis_experimentos/00_protocol/` hasta `12_reports/` para garantizar la trazabilidad de cada paso (P01 a P16) establecida en el Protocolo V1.0.

## DEC-003: Congelamiento de Decisiones Metodológicas (P01)
- **Fecha:** 2026-09-21
- **Decisión:** Registrar formalmente en `decision_log.csv` las 20 decisiones metodológicas congeladas (métrica principal F1 macro, 5-fold CV estratificado, semilla 42, SMOTE y StandardScaler exclusivamente en training, test aislado, CICIDS2017 como contraste con 100k flujos).
