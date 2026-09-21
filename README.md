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

Investigación aplicada y cuantitativa que diseña, implementa y evalúa un sistema de detección de intrusiones de red (NIDS) basado en modelos de aprendizaje automático (**Random Forest**, **XGBoost** y **Perceptrón Multicapa - MLP**) integrado con el marco de explicabilidad matemática **SHAP** (*SHapley Additive exPlanations*), traducido semánticamente hacia alertas operativas y playbooks defensivos para administradores y encargados no especializados de pequeñas y medianas empresas (PyMES) de Juliaca, Puno.

El estudio se rige bajo el **Protocolo de Ejecución V1.0** y la **Matriz de Trazabilidad Técnica**, garantizando reproducibilidad integral, control riguroso de sesgos (congelamiento de decisiones antes de abrir datos de prueba, aislamiento estricto de particiones y ausencia de fuga de datos) y contrastación externa en benchmarks consolidados.

---

## 2. Conjuntos de Datos y Enlaces de Acceso Rápido

Conforme a la metodología aprobada para Seminario de Tesis II, la investigación utiliza un diseño de validación cruzada con dos conjuntos de datos:

| Dataset | Rol Metodológico | Enlace Directo Nube (Descarga Rápida) | Fuente Oficial / DOI | Flujos / Columnas | Tamaño Comprimido |
|---|---|---|---|:---:|:---:|
| **GeNIS 2025** (*Ventana 30s*) | **Dataset Principal** | [Descargar GeNIS 30s (Gofile)](https://gofile.io/d/v5W0QmXN) | [Zenodo 14919237](https://doi.org/10.5281/zenodo.14919237) | 607,933 flujos / 87 cols | **72.34 MB** |
| **CICIDS2017** (*Completo*) | **Dataset de Contraste** | [Descargar CICIDS (Gofile)](https://gofile.io/d/LkY9UuFq) · [Mirror AWS](https://huggingface.co/datasets/bencorn/CICIDS2017/resolve/main/csvs/MachineLearningCSV.zip) | [UNB CIC](https://www.unb.ca/cic/datasets/ids-2017.html) | 2,830,743 flujos / 79 cols | **224.21 MB** |

### Enlaces Directos en la Nube (Sin Tiempos de Espera ni Rate-Limits)
- **GeNIS 2025 (Ventana Oficial 30s preprocesada):**  
  🔗 [https://gofile.io/d/v5W0QmXN](https://gofile.io/d/v5W0QmXN) *(72.34 MB, incluye `genis-30-sec-train.csv` y `genis-30-sec-test.csv`)*
- **CICIDS2017 (MachineLearningCSV con 8 CSVs etiquetados):**  
  🔗 Espejo 1 (Gofile): [https://gofile.io/d/LkY9UuFq](https://gofile.io/d/LkY9UuFq) *(224.21 MB)*  
  🔗 Espejo 2 (Hugging Face / AWS CloudFront): [https://huggingface.co/datasets/bencorn/CICIDS2017/resolve/main/csvs/MachineLearningCSV.zip](https://huggingface.co/datasets/bencorn/CICIDS2017/resolve/main/csvs/MachineLearningCSV.zip)
- **Registro Centralizado de Enlaces:** Consulta [`tesis_experimentos/01_data_metadata/enlaces_nube_rapida.txt`](tesis_experimentos/01_data_metadata/enlaces_nube_rapida.txt).

### Archivos Comprimidos Locales (Listos para subir a tu Google Drive personal)
Si deseas respaldarlos en tu propio Google Drive (`drive.google.com`), los paquetes ya están comprimidos localmente en:
- GeNIS 2025 (30s): `datasets/genis_2025_30sec.zip`
- CICIDS2017: `datasets/.cache/MachineLearningCSV.zip`

---

## 3. Adquisición y Verificación Automatizada

Para descargar, extraer y verificar la integridad criptográfica (hashes MD5 y SHA-256) de los datasets de forma 100% reproducible:

```powershell
python scripts/download_datasets.py
```

El script genera automáticamente las evidencias normativas del hito P02:
- [`tesis_experimentos/01_data_metadata/dataset_metadata.csv`](tesis_experimentos/01_data_metadata/dataset_metadata.csv): inventario formal con DOIs, citas y licencias.
- [`tesis_experimentos/01_data_metadata/dataset_files_hashes.csv`](tesis_experimentos/01_data_metadata/dataset_files_hashes.csv): hashes criptográficos SHA-256 y MD5 de los 10 archivos CSV.
- [`tesis_experimentos/01_data_metadata/data_inventory.md`](tesis_experimentos/01_data_metadata/data_inventory.md): reporte cuantitativo del hito P02.
- [`tesis_experimentos/00_protocol/protocolo_v1.0.md`](tesis_experimentos/00_protocol/protocolo_v1.0.md): Protocolo de Ejecución V1.0 congelado.

---

## 4. Estructura del Repositorio

```text
tesis-seguridad/
├── docs/
│   ├── agent/                      # Memoria persistente del agente autónomo (ROADMAP, PLAN, PROGRESS, etc.)
│   └── protocol/                   # Documentos metodológicos maestros de Tesis II
├── datasets/
│   ├── genis/                      # Flujos oficiales de GeNIS 2025 (30s)
│   └── cicids2017/                 # Flujos etiquetados de CICIDS2017
├── scripts/
│   └── download_datasets.py        # Pipeline de adquisición, extracción y verificación
├── tesis_experimentos/             # Árbol normativo de evidencias (Protocolo V1.0)
│   ├── 00_protocol/                # Decisiones congeladas (decision_log.csv, protocolo_v1.0.md)
│   ├── 01_data_metadata/           # Hashes, inventario y perfiles de hardware/entorno
│   ├── 02_audit/                   # Auditoría de faltantes, duplicados y distribuciones (P03)
│   ├── 03_splits/                  # Manifiestos reproducibles de particiones (P05)
│   ├── 04_configs/                 # Archivos YAML de hiperparámetros y transformaciones (P06-P07)
│   ├── 05_logs/                    # Bitácoras de ejecución con IDs únicos de experimento
│   ├── 06_models/                  # Modelos entrenados serializados (RF, XGBoost, MLP)
│   ├── 07_predictions/             # Predicciones a nivel de flujo individual
│   ├── 08_metrics/                 # Métricas de rendimiento (F1 macro, Accuracy, confusión)
│   ├── 09_shap/                    # Valores SHAP globales/locales y rankings de explicabilidad
│   ├── 10_prototype/               # Código y capturas del prototipo de alertas y playbooks
│   ├── 11_usability/               # Registro anonimizado de evaluación con administradores de PyMES
│   └── 12_reports/                 # Reportes técnicos consolidados y contrastación de hipótesis
└── README.md
```

---

## 5. Decisiones Metodológicas Congeladas (P01)

Antes de abrir o ajustar sobre el conjunto de prueba, se encuentran formalmente congeladas las siguientes pautas en `tesis_experimentos/00_protocol/decision_log.csv`:

1. **Métrica Principal de Selección:** F1 Macro promedio en validación cruzada estratificada de 5 pliegues (semilla 42).
2. **Control de Data Leakage:** Escalado (`StandardScaler`) y balanceo (`SMOTE`) se ajustan **exclusivamente dentro de cada pliegue de entrenamiento** y jamás en los datos de test o validación externa.
3. **Rol de CICIDS2017:** Exclusivamente de contrastación independiente para comprobar estabilidad de características y desempeño generalizado; **no interviene** en la selección del modelo de GeNIS 2025.
4. **Explicabilidad:** `TreeExplainer` para modelos basados en árboles (RF/XGBoost) y `KernelExplainer` (con 100 instancias base y 500 de prueba) si se selecciona MLP.
5. **Criterios de Usabilidad:** Participación de 8 a 12 administradores de PyMES sin formación especializada en ciberseguridad, validación con 3 expertos y piloto previo con 2 usuarios.
