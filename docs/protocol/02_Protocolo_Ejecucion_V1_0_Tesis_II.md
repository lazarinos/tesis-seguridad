# UNIVERSIDAD NACIONAL DE JULIACA
## Facultad de Ciencias de la Ingeniería
### Escuela Profesional de Ingeniería de Software y Sistemas

**Curso:** Seminario de Tesis II — 2026-II  
**Docente:** Liz Huancapaza Hilasaca  
**Autor:** Ccolla Lazarinos, Fernando  
**Título:** *Detección de intrusiones de red con aprendizaje automático y técnicas de explicabilidad (XAI) para pequeñas y medianas empresas de Juliaca, Puno*

# PROTOCOLO DE EJECUCIÓN V1.0

## 1. Propósito

Este protocolo convierte la metodología de la tesis en una secuencia ejecutable, reproducible y verificable. Define qué se hará, con qué datos, en qué orden, bajo qué condiciones, qué decisiones estarán congeladas antes de utilizar el conjunto de prueba y qué evidencias deberán conservarse.

El flujo operativo será:

**Registro → auditoría → homologación → partición → preprocesamiento → validación → selección → prueba → contraste → SHAP → prototipo → piloto → usabilidad → análisis → cierre.**

---

## 2. Alcance

El protocolo cubre:

- GeNIS 2025 como dataset principal.
- CICIDS2017 como dataset de contraste independiente.
- Random Forest, XGBoost y MLP.
- Explicabilidad mediante SHAP.
- Prototipo de alertas con traducción semántica y playbooks.
- Evaluación de usabilidad con 8 a 12 administradores o encargados de pymes de Juliaca.
- Registro completo de configuraciones, predicciones, métricas, incidencias y evidencias.

No incluye captura de tráfico real en pymes ni despliegue del sistema dentro de redes productivas.

---

## 3. Decisiones congeladas antes de ejecutar

| Elemento | Decisión V1.0 |
|---|---|
| Dataset principal | GeNIS 2025, ventana de 30 s |
| Dataset de contraste | CICIDS2017 |
| Modelos | Random Forest, XGBoost, MLP |
| Métrica principal de selección | F1 macro |
| Métricas secundarias | Accuracy, Precision macro, Recall macro, F1 por clase, matriz de confusión |
| Validación | Stratified K-Fold, 5 pliegues |
| Semilla general | 42 |
| Balanceo | SMOTE solo en entrenamiento |
| Escalado | StandardScaler ajustado solo con entrenamiento |
| Model selection | Solo con entrenamiento/validación de GeNIS |
| Test GeNIS | Aislado hasta congelar el modelo |
| CICIDS2017 | No interviene en selección; se usa después como contraste |
| SHAP | TreeExplainer para RF/XGBoost; KernelExplainer si MLP es seleccionado |
| KernelExplainer | 100 instancias de referencia y 500 observaciones de prueba estratificadas, semilla 42 |
| Participantes | 8 a 12 |
| Piloto | 2 usuarios |
| Escenarios | DoS, Port Scan/Reconocimiento, Brute Force |
| Expertos del instrumento | 3 |
| Umbral H3 | Inferencia < 500 ms/flujo |

No se cambiarán estas decisiones únicamente porque un resultado posterior sea desfavorable. Una modificación justificada exigirá actualizar el protocolo a V1.1 o superior y registrar el motivo.

---

## 4. Identificación y estructura de evidencias

Cada experimento tendrá un ID:

`EXP_{DATASET}_{MODELO}_{ETAPA}_S42_{N}`

Ejemplos:

```text
EXP_GENIS_RF_CV_S42_001
EXP_GENIS_XGB_TEST_S42_001
EXP_CICIDS_MLP_CONTRASTE_S42_001
```

Estructura de carpetas:

```text
tesis_experimentos/
├── 00_protocol/
├── 01_data_metadata/
├── 02_audit/
├── 03_splits/
├── 04_configs/
├── 05_logs/
├── 06_models/
├── 07_predictions/
├── 08_metrics/
├── 09_shap/
├── 10_prototype/
├── 11_usability/
└── 12_reports/
```

Todo archivo generado deberá poder asociarse a un ID de experimento.

---

## 5. P01 — Congelamiento del protocolo y registro inicial

### Acción

1. Guardar este documento como `protocolo_v1.0.md`.
2. Crear `decision_log.csv`.
3. Registrar fecha, autor, versión y resumen de decisiones.
4. Registrar hardware y sistema operativo de la estación de trabajo.
5. Crear `environment.txt` o equivalente con versiones de Python y librerías.

### Evidencias

- `protocolo_v1.0.md`
- `decision_log.csv`
- `environment.txt`
- `hardware_profile.txt`

### Regla de control

No iniciar la evaluación final hasta que P01–P08 estén completos.

---

## 6. P02 — Adquisición e inventario de datasets

### GeNIS 2025

Registrar:

- fuente;
- fecha de descarga;
- licencia;
- archivo de entrenamiento;
- archivo de prueba;
- tamaño;
- número de registros;
- hash del archivo.

Archivos de trabajo esperados:

- `genis-30-sec-train.csv`
- `genis-30-sec-test.csv`

### CICIDS2017

Registrar:

- fuente;
- fecha de descarga;
- archivos de origen;
- tamaño;
- número total de registros;
- clases disponibles;
- hash o identificador de versión.

### Evidencias

- `dataset_metadata.csv`
- `dataset_files_hashes.csv`
- `data_inventory.md`

---

## 7. P03 — Auditoría inicial de calidad

Para cada dataset:

1. verificar columnas;
2. verificar tipos;
3. contar valores faltantes;
4. contar duplicados exactos;
5. identificar valores infinitos o técnicamente inválidos;
6. calcular frecuencia y porcentaje por clase;
7. identificar variables constantes;
8. revisar posibles campos identificadores;
9. revisar si existe información de sesión, archivo, día o escenario que permita construir `group_id`;
10. registrar cada exclusión.

### Estructura mínima del registro

| Campo | Descripción |
|---|---|
| record_id | Identificador reproducible del flujo |
| source_dataset | GeNIS o CICIDS2017 |
| source_file | Archivo original |
| original_label | Etiqueta original |
| normalized_label | Etiqueta homologada |
| status | válido/excluido |
| reason | motivo de exclusión |
| group_id | grupo/sesión si existe |
| split | train/validation/test |

### Evidencias

- `dataset_audit_genis.csv`
- `dataset_audit_cicids.csv`
- `class_distribution.csv`
- `audit_report.md`

### Regla

No se excluirán registros por el hecho de ser difíciles de clasificar.

---

## 8. P04 — Homologación de etiquetas y características

### 8.1. Etiquetas

Se utilizará la siguiente taxonomía para la comparación entre datasets:

| Clase común | GeNIS 2025 | CICIDS2017 |
|---|---|---|
| Benigno | Benign | BENIGN |
| DoS-family | DoS | DoS/DDoS compatibles |
| Recon/PortScan | Reconnaissance | PortScan |
| Brute Force | Brute Force | Brute Force |

Las categorías sin equivalencia defendible se marcarán como `NO_HOMOLOGABLE` para el contraste principal.

### 8.2. Características

Se construirá `feature_mapping.csv` con:

- nombre en GeNIS;
- nombre en CICIDS2017;
- definición;
- unidad;
- compatibilidad conceptual;
- decisión de inclusión;
- justificación.

Solo las características marcadas como conceptualmente homologables se utilizarán para el cálculo del índice de Jaccard entre rankings SHAP.

### Evidencias

- `label_mapping.csv`
- `feature_mapping.csv`
- `homologation_report.md`

---

## 9. P05 — Particiones y aislamiento del conjunto de prueba

### GeNIS 2025

1. Conservar las particiones oficiales.
2. `train` se utilizará para validación cruzada y ajuste.
3. `test` permanecerá aislado hasta completar P08.
4. No se calcularán decisiones de selección a partir del test.

### CICIDS2017

1. Filtrar las clases homologables.
2. Obtener un subconjunto estratificado de 100 000 registros con semilla 42.
3. Separar 80 % para entrenamiento/repetición y 20 % para prueba de contraste.
4. Si existe `group_id`, utilizar una separación que mantenga cada grupo en una única partición.
5. Registrar índices exactos en `cicids_split.csv`.

### Evidencias

- `genis_split_manifest.csv`
- `cicids_split.csv`
- `split_summary.md`

### Regla crítica

El test no se utilizará para selección de variables, escalado, SMOTE, ajuste de hiperparámetros o elección de modelo.

---

## 10. P06 — Preprocesamiento reproducible

Orden obligatorio:

1. cargar training split;
2. eliminar solo los registros definidos por los criterios de exclusión;
3. eliminar variables de varianza cero;
4. analizar multicolinealidad exclusivamente sobre entrenamiento;
5. congelar la lista de características;
6. ajustar StandardScaler en entrenamiento;
7. ejecutar SMOTE únicamente sobre entrenamiento;
8. aplicar el transformador congelado a validación/test sin recalibrar;
9. guardar el pipeline serializado.

Durante validación cruzada, selección, escalado y SMOTE estarán dentro del pipeline del pliegue para impedir fuga de información.

### Parámetros de control

- `random_state = 42`
- `SMOTE(random_state=42)`
- umbral de correlación alta sugerido en V1.0: `|r| >= 0.95`
- cualquier cambio del umbral deberá registrarse antes del test.

### Evidencias

- `preprocessing_config.yaml`
- `selected_features.csv`
- `preprocessing_pipeline.pkl`
- `preprocessing_log.csv`

---

## 11. P07 — Entrenamiento y ajuste de modelos

### Validación

Se utilizará:

```text
StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
```

La función de puntuación principal será `f1_macro`.

### Espacio predefinido de ajuste

#### Random Forest

| Hiperparámetro | Valores |
|---|---|
| n_estimators | 200, 400 |
| max_depth | None, 20 |
| min_samples_split | 2, 5 |
| max_features | sqrt |
| class_weight | balanced |

#### XGBoost

| Hiperparámetro | Valores |
|---|---|
| n_estimators | 200, 400 |
| max_depth | 4, 8 |
| learning_rate | 0.05, 0.10 |
| subsample | 0.80 |
| colsample_bytree | 0.80 |

#### MLP

| Hiperparámetro | Valores |
|---|---|
| hidden_layer_sizes | (128, 64), (64, 32) |
| activation | ReLU |
| solver | Adam |
| alpha | 0.0001, 0.001 |
| learning_rate_init | 0.001 |
| batch_size | 256 |
| max_iter | 300 |
| early_stopping | Sí |
| n_iter_no_change | 10 |

Si el costo computacional impide ejecutar la cuadrícula completa, la reducción del espacio deberá definirse y registrarse **antes** de abrir el test.

### Evidencias por modelo

- configuración;
- resultados por pliegue;
- F1 macro media;
- desviación estándar;
- tiempo de entrenamiento;
- modelo ajustado;
- log de ejecución.

Archivos sugeridos:

```text
cv_results_rf.csv
cv_results_xgb.csv
cv_results_mlp.csv
```

---

## 12. P08 — Selección y congelamiento del modelo

Regla:

1. seleccionar el modelo con mayor F1 macro promedio en los cinco pliegues;
2. si existe empate práctico, seleccionar el de menor desviación estándar de F1 macro;
3. si persiste el empate, seleccionar el de menor tiempo de inferencia medido sobre validación.

Después:

- congelar características;
- congelar preprocesamiento;
- congelar hiperparámetros;
- entrenar el modelo final con todo el conjunto de entrenamiento permitido;
- guardar `selected_model_manifest.json`.

### Evidencias

- `model_comparison.csv`
- `selected_model_manifest.json`
- modelo final serializado.

### Prohibición

No consultar GeNIS-test ni CICIDS2017 para decidir qué modelo seleccionar.

---

## 13. P09 — Evaluación final en GeNIS 2025

Abrir el conjunto de prueba una vez que P08 esté completo.

Calcular:

- Accuracy;
- Precision macro;
- Recall macro;
- F1 macro;
- F1 por clase;
- matriz de confusión;
- tiempo de inferencia por flujo.

Guardar predicciones individuales:

| record_id | true_class | predicted_class | model | seed | inference_ms |
|---|---|---|---|---:|---:|

### Evidencias

- `genis_test_predictions.csv`
- `genis_test_metrics.json`
- `genis_confusion_matrix.*`
- `genis_test_report.md`

### Regla

El resultado del test se reporta; no se utilizará para volver a ajustar el modelo dentro de V1.0.

---

## 14. P10 — Contraste independiente en CICIDS2017

Una vez congelado el procedimiento principal:

1. reproducir el mismo esquema de preprocesamiento compatible;
2. entrenar con la partición de entrenamiento CICIDS2017;
3. aplicar la configuración metodológica previamente fijada;
4. evaluar en la partición de prueba CICIDS2017;
5. comparar la estabilidad del rendimiento con GeNIS 2025.

No se utilizará CICIDS2017 para reabrir la selección del modelo de GeNIS.

### Evidencias

- `cicids_test_predictions.csv`
- `cicids_test_metrics.json`
- `cross_dataset_comparison.csv`
- `contrast_report.md`

---

## 15. P11 — Explicabilidad SHAP

Para el modelo seleccionado:

### Si el modelo es RF o XGBoost

Utilizar `TreeExplainer`.

### Si el modelo es MLP

Utilizar `KernelExplainer` con:

- 100 instancias de referencia;
- 500 observaciones de prueba;
- selección estratificada;
- semilla 42.

Calcular:

- `mean(|SHAP|)` por variable;
- ranking global;
- contribución acumulada de las 10 variables principales;
- explicaciones locales de casos de interés;
- Jaccard entre top variables homologadas de ambos datasets.

### Evidencias

- `shap_global.csv`
- `shap_top10.csv`
- `shap_local_cases.csv`
- gráficos SHAP;
- `shap_jaccard.json`

---

## 16. P12 — Construcción del prototipo

El prototipo deberá mostrar como mínimo:

- tipo de alerta;
- nivel o salida de detección disponible;
- variables principales explicadas por SHAP;
- traducción a lenguaje natural;
- playbook recomendado.

Escenarios requeridos:

1. DoS.
2. Port Scan / Reconocimiento.
3. Brute Force.

### Evidencias

- código fuente;
- versión del prototipo;
- capturas de pantalla;
- `prototype_changelog.md`.

---

## 17. P13 — Validación del instrumento y piloto

### Juicio de expertos

Tres expertos revisarán:

- pertinencia;
- claridad;
- coherencia.

Registrar cada observación y decisión de corrección.

### Piloto

Realizar con 2 usuarios antes de la recolección definitiva.

El piloto verificará:

- comprensión de instrucciones;
- claridad de opciones;
- tiempo aproximado;
- errores de interfaz;
- problemas en el registro de respuestas.

### Evidencias

- fichas de juicio de expertos;
- `expert_review_matrix.csv`;
- `pilot_report.md`;
- versión final del cuestionario.

---

## 18. P14 — Evaluación de usabilidad

### Participantes

8 a 12 administradores o encargados de pymes de Juliaca que cumplan los criterios de inclusión.

### Secuencia por participante

1. entregar y explicar consentimiento;
2. asignar código anónimo;
3. registrar datos generales;
4. presentar escenario 1;
5. registrar identificación del ataque;
6. registrar playbook seleccionado;
7. registrar tiempo de reacción;
8. registrar valoraciones Likert;
9. repetir para los tres escenarios;
10. completar evaluación global;
11. cerrar la sesión.

### Evidencias

- consentimientos almacenados separadamente;
- `participants_anonymous.csv`;
- `usability_responses.csv`;
- `reaction_times.csv`;
- registro de incidencias de sesión.

---

## 19. P15 — Análisis y contrastación

### Rendimiento

Comparar métricas de los tres modelos y presentar el resultado final del modelo seleccionado.

### Explicabilidad

Evaluar:

- contribución acumulada top 10;
- Jaccard entre rankings homologados;
- casos locales.

### Usabilidad

Calcular:

- % de identificación correcta;
- % de selección correcta del playbook;
- media/desviación del tiempo de reacción;
- descriptivos de ítems Likert;
- alfa de Cronbach exploratorio.

### Hipótesis

| Hipótesis | Regla |
|---|---|
| H1 | Accuracy ≥ 90 % en GeNIS y F1 macro ≥ 0.85 en CICIDS2017 |
| H2 | Top 10 SHAP ≥ 70 % de contribución y Jaccard ≥ 0.40 |
| H3 | Inferencia < 500 ms/flujo |
| H4 | Ataque correcto ≥ 70 % y playbook correcto ≥ 60 % |

No se modificará un umbral para acomodarlo a los resultados obtenidos.

---

## 20. P16 — Incidencias, versionado y cierre

Cada desviación se registrará en:

`incident_log.csv`

Campos mínimos:

| Campo | Contenido |
|---|---|
| fecha | fecha/hora |
| experimento | ID |
| incidencia | qué ocurrió |
| impacto | datos/modelo/tiempo |
| decisión | acción adoptada |
| justificación | motivo |
| versión | protocolo aplicable |

Ejemplos de incidencias:

- falla eléctrica;
- interrupción de entrenamiento;
- archivo corrupto;
- insuficiencia de memoria;
- error de librería;
- participante que abandona la sesión.

Los fallos y resultados negativos se conservarán.

---

## 21. Criterios de cierre de la experimentación

La fase experimental terminará cuando:

- los tres modelos hayan sido evaluados bajo el protocolo;
- la selección del modelo esté documentada;
- GeNIS-test haya sido evaluado una sola vez después del congelamiento;
- CICIDS2017 haya sido ejecutado como contraste independiente;
- predicciones y métricas estén almacenadas;
- SHAP tenga trazabilidad hasta las predicciones;
- el prototipo esté versionado;
- la prueba piloto esté documentada;
- las sesiones de usabilidad estén completas;
- toda incidencia esté registrada;
- exista un README que permita repetir el flujo.

---

## 22. Checklist de protocolo ejecutable

- [ ] ¿Cada objetivo tiene una evidencia definida?
- [ ] ¿El procedimiento tiene pasos y orden claros?
- [ ] ¿Datasets, participantes y sistemas están identificados?
- [ ] ¿Métrica principal y criterios están fijados?
- [ ] ¿Comparadores están definidos?
- [ ] ¿Los cinco pliegues y la semilla están definidos?
- [ ] ¿El test está aislado?
- [ ] ¿CICIDS2017 se usa solo después de congelar la selección?
- [ ] ¿Existe plan de registro y trazabilidad?
- [ ] ¿Se documentan incidencias?
- [ ] ¿Se registran resultados negativos?
- [ ] ¿Están contempladas amenazas de validez?
- [ ] ¿Están contempladas las consideraciones éticas?

**Prueba final de reproducibilidad:** otra persona debe poder explicar cómo ejecutar el estudio sin recibir instrucciones orales adicionales y debe poder rastrear cualquier F1 reportado hasta el dataset, partición, configuración, semilla, predicciones y experimento que lo produjo.
