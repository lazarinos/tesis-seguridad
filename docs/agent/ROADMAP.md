# Roadmap de implementación: Adquisición de Datasets y Protocolo V1.0 (Tesis II)

## Objetivo
Descargar, auditar y verificar los datasets de la tesis (**GeNIS 2025** como principal y **CICIDS2017** como contraste independiente), formalizar el Protocolo de Ejecución V1.0 y la Matriz de Trazabilidad Técnica para Seminario de Tesis II (2026-II), y reorganizar la estructura del repositorio con trazabilidad total.

## Estado general
- Estado: Completado
- Última actualización: 2026-09-21 10:41
- Riesgo actual: Bajo
- Responsable: Agente autónomo

## Alcance
- Incluye:
  - Creación de memoria persistente del agente en `docs/agent/`.
  - Estructuración de carpetas de experimentación (`tesis_experimentos/` según Protocolo V1.0).
  - Congelamiento de decisiones metodológicas iniciales P01 (`decision_log.csv`, `environment.txt`, `hardware_profile.txt`).
  - Pipeline de descarga reproducible (`scripts/download_datasets.py`) con verificación de integridad (hashes MD5 y SHA256) para GeNIS 2025 y CICIDS2017.
  - Extracción e inventariado formal de los flujos CSV (P02).
  - Actualización de `README.md` y contraste con `datasets_complementarios_tesis.md`.
  - Validación de lectura y carga básica de ambos conjuntos de datos.
- No incluye:
  - Modificación de hiperparámetros o entrenamiento previo a la fase de preprocesamiento (P06).
  - Exposición de tráfico sensible de redes productivas de PyMES.

## Criterios de aceptación
- [x] Memoria persistente del agente inicializada en `docs/agent/`.
- [x] Estructura de directorios `tesis_experimentos/` creada de acuerdo con el Protocolo V1.0.
- [x] Hito P01 documentado con `decision_log.csv`, `environment.txt` y `hardware_profile.txt`.
- [x] Script `scripts/download_datasets.py` funcional y documentado.
- [x] Descarga e integridad verificada de GeNIS 2025 (`genis-30-sec-train.csv`, `genis-30-sec-test.csv`).
- [x] Descarga e integridad verificada de CICIDS2017 (`MachineLearningCSV.zip` y 8 flujos CSV extraídos).
- [x] Metadatos y hashes registrados en `tesis_experimentos/01_data_metadata/`.
- [x] `README.md` actualizado con las fuentes activas y comandos de reproducción.
- [x] Smoke test de carga con pandas verificando dimensiones y tipos en ambos datasets.

## Etapa 1 — Inicialización de memoria y estructura normativa
- [x] Crear archivos de memoria persistente en `docs/agent/`.
- [x] Crear estructura de directorios `tesis_experimentos/` según Protocolo V1.0.
- [x] Ubicar copias normativas del protocolo en `tesis_experimentos/00_protocol/`.
- [x] Generar evidencias del hito P01: `decision_log.csv`, `hardware_profile.txt` y `environment.txt`.

**Validación:** Archivos existentes en `docs/agent/` y `tesis_experimentos/00_protocol/`.  
**Finaliza cuando:** La estructura base de trazabilidad esté establecida.

## Etapa 2 — Script de adquisición y verificación de datasets (P02)
- [x] Desarrollar `scripts/download_datasets.py` para GeNIS 2025 y CICIDS2017.
- [x] Incluir soporte para reintentos, verificación de hashes (MD5 / SHA256) y extracción selectiva.
- [x] Integrar generación automática de `dataset_metadata.csv`, `dataset_files_hashes.csv` y `data_inventory.md`.

**Validación:** `python scripts/download_datasets.py` ejecutado con éxito.  
**Finaliza cuando:** El script esté listo para descargar de forma robusta.

## Etapa 3 — Descarga, extracción y verificación de integridad
- [x] Descargar `4-preprocessed.zip` de GeNIS 2025 desde Zenodo API y extraer particiones de 30 segundos.
- [x] Descargar `MachineLearningCSV.zip` de CICIDS2017 desde Hugging Face y extraer flujos etiquetados.
- [x] Calcular hashes MD5 y SHA256 y guardar en `tesis_experimentos/01_data_metadata/`.
- [x] Validar que los archivos no estén truncados o corruptos.

**Validación:** Existencia física de los CSV y verificación de hashes en `dataset_files_hashes.csv`.  
**Finaliza cuando:** Ambos datasets estén en disco listos para auditoría.

## Etapa 4 — Validación de datos (Smoke Test) y contrastación documental
- [x] Ejecutar smoke test con Python/pandas verificando filas, columnas y clases.
- [x] Actualizar `README.md` eliminando enlaces caídos e incorporando el nuevo estándar.
- [x] Contrastar y sincronizar `datasets_complementarios_tesis.md`.
- [x] Actualizar memoria técnica y roadmap con evidencia de ejecución.

**Validación:** Script de smoke test con exit code 0 y reporte en `TESTING.md`.  
**Finaliza cuando:** Los criterios de aceptación estén completamente cumplidos y verificados.

## Etapa 5 — Limpieza de repositorio, respaldo en la nube y despliegue a GitHub
- [x] Limpieza del árbol Git: deselección de archivos temporales pesados (`node_modules`, `scratch`, logs, DBs).
- [x] Actualización de `.gitignore` para bloquear permanentemente datasets, logs de playwright y bases sqlite temporales.
- [x] Carga y respaldo de datasets en la nube para acceso rápido (`enlaces_nube_rapida.txt`).
- [~] Preparación de commits limpios y push al repositorio remoto en GitHub (`origin master`).

**Validación:** `git status` limpio, `git log` coherente y `git push origin master` exitoso sin violación de cuotas ni datasets pesados en el árbol Git.  
**Finaliza cuando:** El repositorio remoto en GitHub contenga el código estructurado, la documentación, los scripts y la memoria técnica actualizada.

## Bloqueos, riesgos y decisiones
- [x] Bloqueo 403 y desconexiones intermitentes de Zenodo resueltos mediante la herramienta oficial `zenodo_get` (con `httpx2` y reintentos automáticos).
- [x] Archivos temporales de node_modules (370k líneas del commit e463512) eliminados de la indexación con `git rm -r --cached`.

## Evidencia de validación
| Hito | Comando / Acción | Resultado |
|---|---|---|
| P01 Perfil de Hardware | `hardware_profile.txt` | Intel Core 6 núcleos, Windows 10, Python 3.11.9 |
| P01 Decision Log | `decision_log.csv` | 20 decisiones congeladas (DEC-001 a DEC-020) |
| P02 GeNIS 2025 | `zenodo_get -r 14919237` | MD5 `1856f231354cf4928e40ba606080a9b2` verificado (572.16 MB) |
| P02 Partición Train GeNIS | `genis-30-sec-train.csv` | 486,346 filas, 87 columnas |
| P02 Partición Test GeNIS | `genis-30-sec-test.csv` | 121,587 filas, 87 columnas |
| P02 CICIDS2017 | `MachineLearningCSV.zip` | 8 archivos CSV, 2,830,743 flujos, 79 columnas |
| Smoke test de clases | `BinaryLabel`, `CategoryLabel` | GeNIS: dos (423k), benign (26k), recon (22k), bruteforce (14k) |
| Integridad criptográfica | `dataset_files_hashes.csv` | 10 archivos CSV con MD5 y SHA256 completos |
| Respaldo Nube GeNIS | `upload_to_cloud.py` | `https://gofile.io/d/v5W0QmXN` (72.34 MB) |
| Limpieza de Git | `git rm -r --cached` | 370k líneas temporales removidas del tracking |

## Resumen final
- Completado: Hitos P01, P02, adquisición de datasets, scripts de pipelines, respaldo en la nube y limpieza profunda de Git.
- Pendiente: Push a GitHub y verificación de sincronización remota.
- Bloqueado: Ninguno.
- Riesgos remanentes: Ninguno. Datasets pesados protegidos e ignorados fuera del tracking de Git.
