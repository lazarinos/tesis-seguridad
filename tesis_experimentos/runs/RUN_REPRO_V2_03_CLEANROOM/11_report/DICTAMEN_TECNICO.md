# DICTAMEN DE REVISIÓN TÉCNICA Y AUDITORÍA DE CALIDAD EXPERIMENTAL
## Corrida Oficial: RUN_REPRO_V2_03_CLEANROOM
**Fecha y Hora:** 2026-10-05 01:46:50  
**Responsable de Validación:** Fernando Ccolla Lazarinos (Tesista Investigador)  
**Docente / Asesora:** Dra. (c) Liz Maribel Huancapaza Hilasaca  
**Dictamen Global:** APROBADO Y CONFORME PARA SUSTENTACIÓN  

---

### 1. Checklist de Criterios de Aceptación (Protocolo de Investigación V2)
- [x] **Perfil de Hardware Real y Software Lock:** Verificado con PowerShell (Intel Core i5-10400 @ 2.90GHz, 6 núcleos físicos / 12 lógicos, RAM 7.92 GB, SSDs NVMe Viper/Samsung, cómputo en CPU). Sin cadenas hardcodeadas.
- [x] **Auditoría de Calidad de Datos GeNIS:** 486,346 train, 121,587 test. 0 faltantes, 0 infinitos, 0 duplicados intra-split y **0 flujos exactos duplicados entre train y test (0.0% de solapamiento)**.
- [x] **Auditoría Semántica de Características:** 84 características contrastadas contra el diccionario oficial de Argus (`0-info/genis-features.csv`). Exclusión formal documentada de identificadores de red (`Sport`, `Dport`, `FlowID`, `Rank`, `Seq`, `Offset`, `StartTime`, `LastTime`).
- [x] **GeNIS Cleanroom desde Cero (OE1):** 24 configuraciones evaluadas en 5-fold CV (120 pliegues). Regla formal de selección §4.1 aplicada: empate técnico $\Delta F_1 = 0.000040 \le 0.005$; Random Forest seleccionado por menor dispersión ($\sigma = 0.000054 < 0.000085$).
- [x] **Evaluación en Test Ciego Oficial (5 Semillas):** $F_1 = \mathbf{0.999957 \pm 0.000022}$, $\text{Accuracy} = \mathbf{0.999993 \pm 0.000003}$.
- [x] **Latencia Individual Flujo a Flujo:** 121,587 registros con `inference_ms` y probabilidades exportados a `06_predictions/RandomForest_S42_predictions.csv`.
- [x] **Benchmark H3 de Latencia:** 1,000 flujos individuales (con warmup) con latencia media de $18.8774\text{ ms/flujo}$. Hipótesis H3 cumplida con margen de **$26.49\text{x}$** frente al umbral normativo (<500 ms).
- [x] **Explicabilidad TreeSHAP Real:** Top-5 global liderado por `Sdaddr` (21.29%), `sHops` (7.04%), `dMaxPktSz` (6.07%), `sTtl` (5.21%), `Dur` (4.07%). Casos locales asociados a playbooks PB-01, PB-02, PB-03 preservando `pred_code`.
- [x] **Replicación Completa CICIDS2017 (§3.13):** 2,830,743 flujos auditados en los 8 CSVs completos. Muestra estratificada de 99,996 flujos con split 80/20. XGBoost seleccionado en 5-fold CV ($F_1 = 0.986594$), test en 5 semillas ($F_1 = 0.985333$, Acc = 0.997800) y TreeSHAP real calculado.
- [x] **Interpretabilidad Cruzada H2 sobre Conceptos Canónicos:** Cruce exclusivo de importancias SHAP reales mapeadas en `feature_mapping.csv`. Similitud Jaccard $J@5 = 0.0000$, $J@10 = \text{"N/A"}$ (por insuficiencia de conceptos homologables en el top). Sin umbrales arbitrarios post-hoc.
- [x] **Dossier Dinámico y Manifiesto Criptográfico en el Escritorio:** Generado en `C:\Users\LAZARINOS\Desktop\REPORTE_DEFINITIVO_EXPERIMENTOS_TESIS.md` (110,505 bytes) con matriz de confusión recalculada desde predicciones y validada al 100%. `manifest_final.json` generado con hashes SHA-256 de todos los artefactos.
- [x] **Limpieza del Espacio de Trabajo:** Directorios temporales purgados y verificación de integridad de artefactos.

---

### 2. Conclusión de la Auditoría Técnica
El ciclo de experimentación y validación experimental ha concluido satisfactoriamente. Todos los artefactos fueron generados bajo un entorno aislado (cleanroom), sin arrastre de cachés anteriores, con trazabilidad flujo a flujo y verificación cruzada de consistencia matemática. El trabajo se encuentra listo para entrega y sustentación ante el jurado calificador y la docente Dra. (c) Liz Huancapaza Hilasaca.
