# Bitácora de Pruebas y Validación (TESTING.md)

## Registro de Pruebas

### TST-001: Verificación de Endpoints de Datasets
- **Fecha:** 2026-09-21
- **Herramienta:** `curl.exe`
- **Resultados:**
  - `https://zenodo.org/api/records/14919237/files/0-info.zip/content`: HTTP 200 OK (3,308 bytes).
  - `https://huggingface.co/datasets/bencorn/CICIDS2017/resolve/main/csvs/MachineLearningCSV.zip`: HTTP 200 OK (235,102,953 bytes).
- **Estado:** APROBADO.

### TST-002: Verificación de Dependencias Base
- **Fecha:** 2026-09-21
- **Librerías verificadas:** `pandas 2.3.3`, `scikit-learn 1.9.0`, `shap 0.51.0`, `xgboost 3.2.0`, `torch 2.13.0`.
- **Estado:** APROBADO.

### TST-003: Verificación de Integridad Criptográfica de Archivos Descargados
- **Fecha:** 2026-09-21
- **Archivos verificados:**
  - `4-preprocessed.zip`: MD5 `1856f231354cf4928e40ba606080a9b2` (coincidencia exacta con metadatos de Zenodo).
  - `MachineLearningCSV.zip`: 224.21 MB (descarga íntegra desde CloudFront/HuggingFace).
- **Estado:** APROBADO.

### TST-004: Smoke Test de Carga y Esquema de Clases
- **Fecha:** 2026-09-21
- **Dataset GeNIS 2025 (30s):**
  - Train: 486,346 filas, 87 columnas. Clases: dos (423,700), benign (26,027), recon (22,186), bruteforce (14,433).
  - Test: 121,587 filas, 87 columnas. Clases: 1 (115,080), 0 (6,507).
  - Columnas de etiquetas confirmadas: `BinaryLabel`, `CategoryLabel`, `SubCategoryLabel`.
- **Dataset CICIDS2017:**
  - 8 archivos CSV con 79 columnas.
  - Flujos totales: 2,830,743 flujos.
  - Clases homologables confirmadas: BENIGN (2.27M), DoS Hulk (231k), PortScan (158k), DDoS (128k), DoS GoldenEye (10k), FTP-Patator (7.9k), SSH-Patator (5.8k).
- **Estado:** APROBADO.
