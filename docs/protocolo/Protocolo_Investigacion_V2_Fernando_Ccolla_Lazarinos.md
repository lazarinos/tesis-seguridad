# PROTOCOLO DE INVESTIGACIÓN

## METODOLOGÍA, PROTOCOLO EXPERIMENTAL V2 Y MATRIZ DE TRAZABILIDAD TÉCNICA

### Detección de intrusiones de red con aprendizaje automático y técnicas de explicabilidad (XAI) para pequeñas y medianas empresas de Juliaca, Puno

| Campo | Información |
|---|---|
| **Docente** | Liz Huancapaza Hilasaca |
| **Curso** | Seminario de Tesis II |
| **Autor** | Ccolla Lazarinos, Fernando |
| **Título de la tesis** | Detección de intrusiones de red con aprendizaje automático y técnicas de explicabilidad (XAI) para pequeñas y medianas empresas de Juliaca, Puno |
| **Versión** | V2 |
| **Fecha** | 03/10/2026 |
| **Finalidad** | Entrega de protocolo de investigación - versión 2, ejecutable, reproducible y trazable |

> **Nota.** Las decisiones sobre procedencia de datos, particiones, homologación de variables, preprocesamiento, modelos, métricas, entorno de ejecución, explicabilidad y evaluación con usuarios se establecen antes del análisis final para mantener la coherencia, reproducibilidad y trazabilidad del estudio.

---

## 1. PLANTEAMIENTO DE LA INVESTIGACIÓN

**Objetivo general.** Desarrollar y evaluar un sistema de detección de intrusiones de red basado en aprendizaje automático e integrado con explicabilidad SHAP, utilizando GeNIS 2025 como conjunto principal y CICIDS2017 como repetición experimental independiente, y orientar sus salidas a alertas comprensibles, útiles y accionables para administradores de pymes de Juliaca, Puno.

- **OE1.** Comparar Random Forest, XGBoost y Perceptrón Multicapa (MLP) bajo un mismo esquema de evaluación, usando F1-macro como métrica principal en GeNIS 2025 y repitiendo el procedimiento de forma independiente en CICIDS2017.
- **OE2.** Identificar las variables con mayor contribución a las predicciones mediante valores SHAP y comparar entre datasets únicamente los conceptos de red que hayan sido homologados de manera documentada.
- **OE3.** Implementar un prototipo local que traduzca la predicción y las atribuciones SHAP en alertas comprensibles, útiles y accionables para usuarios no especializados en ciberseguridad.
- **OE4.** Evaluar de forma exploratoria la comprensión, utilidad percibida, confianza y respuesta inicial asociadas a las alertas del prototipo en una muestra intencional de 8 a 12 administradores o encargados de pymes de Juliaca.

## 2. METODOLOGÍA

La metodología adopta un diseño aplicado y cuantitativo con dos componentes complementarios: experimentación computacional y evaluación exploratoria del prototipo con usuarios. La procedencia de los datos, la comparabilidad de variables, las reglas de preprocesamiento, selección y análisis se fijan antes de abrir los conjuntos de prueba para evitar ajustes guiados por los resultados.

### 2.1 Enfoque, tipo y diseño de investigación

La investigación adopta un enfoque cuantitativo y es de tipo aplicada. Integra: (a) experimentación computacional comparativa con Random Forest, XGBoost y MLP; y (b) evaluación no experimental, transversal y exploratoria de un prototipo de alertas. El componente técnico busca comparar modelos bajo condiciones reproducibles. El componente con usuarios busca detectar problemas de comprensión y utilidad práctica, no estimar parámetros de toda la población de pymes.

### 2.2 Unidades de análisis, población y muestra

| Componente | Unidad de análisis | Población / fuente | Muestra utilizada |
|---|---|---|---|
| **Técnico - GeNIS** | Flujo de red etiquetado | GeNIS 2025, versión oficial publicada en Zenodo. | Archivos oficiales `genis-30-sec-train.csv` y `genis-30-sec-test.csv`; no se vuelve a particionar el test. |
| **Técnico - CICIDS2017** | Flujo de red etiquetado | CICIDS2017, fuente oficial del Canadian Institute for Cybersecurity. | Muestra reproducible de 100 000 flujos obtenida después de la auditoría, con muestreo estratificado y semilla 42; luego split 80/20 estratificado. |
| **Usabilidad** | Administrador, encargado o responsable operativo de pyme | Responsables operativos de pymes de Juliaca. | Muestreo no probabilístico intencional. Meta: 10 sesiones válidas; rango operativo 8 a 12. Uso exclusivamente exploratorio/formativo. |

**Justificación del tamaño de usuarios.** El rango 8-12 no se usa para inferencia estadística ni para afirmar que una proporción representa a todas las pymes de Juliaca. Su función es evaluar un prototipo temprano, identificar patrones de comprensión, errores recurrentes y oportunidades de mejora. Los resultados se presentarán como evidencia descriptiva del grupo observado.

### 2.3 Procedencia, versión y partición de los datasets

**GeNIS 2025.** Se utilizará la versión oficial GeNIS: GECAD Network Intrusion Scenarios, publicada en Zenodo (DOI 10.5281/zenodo.14919237) y descrita por Silva et al. (2025). El análisis principal empleará los archivos preprocesados de 30 segundos `genis-30-sec-train.csv` y `genis-30-sec-test.csv`. La documentación oficial indica que los conjuntos preprocesados se construyeron mediante barajado y estratificación para conservar la proporción de clases. La separación train/test oficial se preservará y se registrarán sus conteos reales y hashes antes de cualquier transformación.

**CICIDS2017.** Se utilizarán los archivos de flujos etiquetados procedentes de la distribución oficial del Canadian Institute for Cybersecurity, University of New Brunswick, documentada por Sharafaldin et al. (2018). Los archivos se combinarán conservando el archivo de origen de cada registro. Después de la auditoría de calidad se construirá una muestra estratificada de 100 000 flujos con semilla 42. Sobre esa muestra se fijará un split estratificado 80 % entrenamiento/validación y 20 % prueba. El test queda aislado hasta el cierre de la selección dentro de CICIDS2017.

> **Regla de comparabilidad.** GeNIS y CICIDS2017 no se concatenarán para entrenar un único modelo. La repetición en CICIDS2017 es un experimento independiente. Esto evita asumir que ambas taxonomías, herramientas de extracción y distribuciones son equivalentes.

### 2.4 Procedimiento de homologación de variables GeNIS-CICIDS2017

La homologación se utilizará únicamente para comparar explicaciones SHAP entre datasets. No se usará para mezclar filas ni transferir un modelo entrenado en un dataset al otro. El procedimiento se ejecutará antes de analizar SHAP y generará `feature_mapping.csv`.

1. Extraer el diccionario de variables de GeNIS (`genis-features.csv`) y los nombres/definiciones documentadas de las variables de CICIDS2017. Normalizar solo el nombre textual para búsqueda; la decisión se toma por definición, no por parecido de nombres.
2. Asignar a cada variable un concepto canónico de tráfico, por ejemplo duración de flujo, conteo de paquetes por dirección, bytes por dirección, tasa de paquetes, estadísticos de tamaño, tiempos entre arribos o banderas TCP.
3. Evaluar cada posible equivalencia con cinco criterios obligatorios: mismo concepto; misma dirección del flujo; mismo estadístico (total, media, máximo, desviación, etc.); misma unidad o conversión determinista documentable; y ventana/agregación compatible.
4. Clasificar la relación como **EXACTA**, **CONVERTIBLE** o **NO_COMPARABLE**. Solo EXACTA y CONVERTIBLE pueden entrar al análisis cruzado. Las conversiones permitidas son únicamente transformaciones de unidad explícitas y reversibles; no se permiten regresiones, imputaciones aprendidas ni aproximaciones semánticas.
5. Excluir de la homologación identificadores, direcciones IP, puertos, marcas temporales, etiquetas y cualquier campo cuya definición dependa de una topología concreta. Si existe duda semántica, la variable se marca **NO_COMPARABLE**.
6. Congelar `feature_mapping.csv` antes de calcular el Jaccard de top-k. El archivo contendrá: `genis_feature`, `cicids_feature`, `canonical_concept`, `direction`, `statistic`, `unit_genis`, `unit_cicids`, `transform`, `status`, `justification` y `source_reference`.
7. Calcular el solapamiento SHAP usando `canonical_concept`, nunca el nombre crudo de la columna. Si el número de variables homologables es insuficiente para una comparación interpretable, se reportará "no aplicable" en lugar de forzar correspondencias.

**Trazabilidad.** La homologación queda documentada mediante criterios explícitos de concepto, dirección, estadístico, unidad y ventana de agregación. Cada correspondencia aceptada o descartada conservará su justificación en `feature_mapping.csv`.

### 2.5 Calidad de datos, preprocesamiento y control de fuga

1. Carga e inventario de archivos, versión, hash, columnas, etiquetas y número de registros.
2. Detección documentada de faltantes, infinitos, duplicados exactos y registros técnicamente inválidos.
3. Eliminación o tratamiento de registros inválidos según regla definida antes del modelado; toda exclusión conserva motivo.
4. Selección de características usando solo datos de entrenamiento: varianza cero, correlación alta y revisión de multicolinealidad.
5. Ajuste de `StandardScaler` exclusivamente con entrenamiento cuando el algoritmo lo requiera.
6. Aplicación de SMOTE únicamente dentro del entrenamiento. Durante validación cruzada, selección, escalado y SMOTE se ajustan dentro de cada pliegue.
7. Aplicación de transformaciones congeladas a validación y prueba sin recalibración.

### 2.6 Modelos, validación, selección y métricas

Se compararán Random Forest, XGBoost y MLP. La optimización se ejecutará únicamente sobre entrenamiento mediante validación cruzada estratificada de cinco pliegues. F1-macro será la métrica principal en GeNIS y CICIDS2017 porque pondera por igual cada clase y mantiene una regla de comparación coherente. Accuracy, Precision macro, Recall macro, F1 por clase y matriz de confusión se reportarán como métricas complementarias, pero no se combinarán con F1-macro en una misma regla de selección.

En GeNIS, el modelo primario se seleccionará por mayor F1-macro medio de validación. Si la diferencia absoluta entre los dos primeros es menor o igual a 0,005, se preferirá la menor desviación estándar y, si persiste el empate, el menor tiempo medio de inferencia medido en validación. CICIDS2017 no reabre la selección del modelo principal; repite el procedimiento para evaluar estabilidad metodológica en otro dataset.

| Componente | Métricas / indicadores |
|---|---|
| **Clasificación** | F1-macro (principal), Accuracy, Precision macro, Recall macro, F1 por clase y matriz de confusión. |
| **Explicabilidad** | `mean(\|SHAP\|)`, ranking top-10, contribución acumulada y Jaccard únicamente sobre conceptos homologados. |
| **Eficiencia** | Tiempo de inferencia por flujo y tiempo de explicación SHAP por flujo, medidos en la estación de trabajo registrada. |
| **Usabilidad** | Aciertos n/N por escenario, claridad, utilidad, confianza e intención de adopción en Likert 1-5, tiempo de reacción y observaciones cualitativas breves. |

### 2.7 Entorno de hardware y software

Antes de la primera ejecución válida se generará `environment/hardware_profile.json` y `environment/software_lock.txt`. El perfil queda asociado a cada experimento mediante un hash. No se aceptará una medición de tiempo sin ese perfil.

| Elemento | Registro obligatorio |
|---|---|
| **CPU** | Fabricante, modelo exacto, núcleos físicos y lógicos. |
| **RAM** | Memoria física total en GiB. |
| **GPU** | Modelo y VRAM; si no se usa aceleración, registrar explícitamente "no utilizada". |
| **Almacenamiento** | Tipo de unidad donde se encuentran dataset y entorno de ejecución (SSD/NVMe/HDD). |
| **Sistema operativo** | Nombre, edición y versión/build. |
| **Software** | Versión de Python y versiones exactas de numpy, pandas, scikit-learn, xgboost, imbalanced-learn, shap y Flask. |
| **Control** | Si CPU, RAM, GPU o configuración relevante cambia, los nuevos tiempos pertenecen a otra serie y no se promedian con la anterior. |

> **Criterio de validez.** La especificación válida del entorno será la del equipo físico que ejecute los experimentos. CPU, RAM, GPU cuando corresponda, almacenamiento, sistema operativo y versiones de software se capturarán antes de medir H3 y se conservarán junto con los resultados.

### 2.8 Estrategia SHAP, prototipo y evaluación de usabilidad

Para Random Forest y XGBoost se utilizará TreeExplainer. Si MLP resulta seleccionado, se utilizará KernelExplainer con 100 instancias de referencia y 500 observaciones de prueba elegidas mediante muestreo estratificado reproducible con semilla 42. Las explicaciones globales y locales conservarán los identificadores de flujo y la versión del modelo.

El prototipo local en Flask presentará tipo de alerta, confianza cuando esté disponible, variables con mayor contribución SHAP, explicación operativa y playbook inicial. La evaluación usará tres escenarios simulados: DoS, Port Scan y Brute Force. El instrumento será revisado por tres expertos y probado con 2 usuarios antes de la aplicación final.

En la evaluación final, cada participante resolverá los tres escenarios. Se registrará si identifica correctamente el ataque, si selecciona el playbook previsto, sus respuestas Likert de claridad, utilidad, confianza e intención de adopción, el tiempo de reacción y comentarios breves. Por el tamaño de la muestra, la lectura principal será descriptiva; no se inferirá una tasa poblacional ni se usará un porcentaje fijo como frontera de aprobación.

### 2.9 Hipótesis de trabajo y criterios de análisis

| Hipótesis | Formulación | Criterio operativo |
|---|---|---|
| **H1 - Rendimiento** | Los algoritmos evaluados presentarán diferencias de rendimiento en la detección de intrusiones, observables mediante F1-macro. | Comparar F1-macro medio y DE en CV; confirmar el desempeño en test y reportar Accuracy, Precision y Recall como métricas complementarias. |
| **H2 - Explicabilidad** | SHAP identificará variables o conceptos dominantes y permitirá comparar solo lo homologable. | `mean(\|SHAP\|)`, top-10, contribución acumulada y Jaccard sobre `canonical_concept`; sin forzar equivalencias. |
| **H3 - Eficiencia** | La inferencia debe ser compatible con una alerta interactiva en el equipo registrado. | Tiempo medio por flujo menor de 500 ms bajo el mismo `environment_id`. SHAP se reporta aparte. |
| **H4 - Usabilidad** | Los participantes del grupo evaluado comprenderán las alertas y podrán realizar una respuesta inicial apoyada por el prototipo. | Analizar conjuntamente aciertos n/N, respuestas Likert, tiempo de reacción y observaciones; la interpretación será descriptiva y no inferencial. |

---

## 3. PROTOCOLO EXPERIMENTAL V2

### 3.1 Propósito, alcance y flujo

El protocolo fija las decisiones necesarias para ejecutar el estudio sin modificar criterios después de observar los resultados. Todo cambio sustancial posterior exige una nueva versión del protocolo y una justificación registrada.

**Flujo experimental:** fuentes oficiales -> inventario y hashes -> auditoría -> partición -> preprocesamiento -> validación/ajuste -> selección -> test final -> repetición CICIDS2017 -> homologación para SHAP -> explicaciones -> prototipo -> piloto -> usabilidad -> análisis -> cierre.

### 3.2 Registro de procedencia y auditoría de datasets

Cada archivo se registrará antes del procesamiento. `dataset_metadata.csv` conservará, como mínimo:

| Campo | Descripción |
|---|---|
| `record_id` | Identificador reproducible del flujo dentro de la ejecución. |
| `source_dataset` | GeNIS 2025 o CICIDS2017. |
| `source_provider` | Zenodo/GECAD para GeNIS; CIC-UNB para CICIDS2017. |
| `source_file` | Archivo de procedencia exacto. |
| `source_url_or_doi` | DOI o página oficial utilizada para obtención. |
| `dataset_version` | Versión/fecha de descarga registrada. |
| `dataset_hash` | SHA-256 del archivo o manifest de la versión. |
| `original_label` | Etiqueta original. |
| `status / reason` | Válido o excluido y motivo de exclusión. |
| `split` | train, fold, validation o test. |

**Evidencias.** `dataset_metadata.csv`, `dataset_manifest.json`, `dataset_audit_genis.csv`, `dataset_audit_cicids.csv` y reporte de caracterización.

### 3.3 Control de duplicados y fuga de información

Se buscarán duplicados exactos dentro de cada partición y entre entrenamiento y prueba. Si un registro idéntico aparece en entrenamiento y prueba de una partición creada por el estudio, se conservará en entrenamiento y se excluirá de prueba, dejando constancia. En GeNIS se respetará primero el split oficial y se documentará cualquier solapamiento detectado sin reconstruir silenciosamente la partición. Toda selección de características, escalado y SMOTE se ajustará únicamente con entrenamiento o fold de entrenamiento.

### 3.4 Caracterización inicial

- Número total de flujos y número de flujos por clase.
- Porcentaje por clase y nivel de desbalance.
- Faltantes, infinitos, duplicados y registros inválidos.
- Número de características originales y características utilizadas.
- Registros excluidos y motivo de exclusión.
- Archivo de origen y hash de cada dataset.

### 3.5 División de datos

| Dataset | Entrenamiento / selección | Prueba final | Control |
|---|---|---|---|
| **GeNIS 2025** | `genis-30-sec-train.csv` oficial. Dentro de train: CV estratificada de 5 pliegues. | `genis-30-sec-test.csv` oficial. | No se vuelve a mezclar. Test aislado hasta congelar pipeline/modelo. Se reporta proporción real observada. |
| **CICIDS2017** | De la muestra estratificada de 100 000 flujos auditados: 80 % train/validación, semilla 42. | 20 % test, semilla 42. | Split estratificado congelado en `split_manifest.csv`. Test aislado dentro de la repetición CICIDS. |

### 3.6 Homologación de características para comparación SHAP

Se ejecutará después de congelar la procedencia de los datasets y antes de calcular cualquier indicador cruzado de explicabilidad. La salida `feature_mapping.csv` será versionada. La comparación se hará por concepto canónico y solo con filas `status=EXACTA` o `status=CONVERTIBLE`. Las transformaciones de unidad se aplicarán antes de documentar la equivalencia. Variables `NO_COMPARABLE` quedan fuera del Jaccard y no se reemplazan por aproximaciones.

| Validación | Regla |
|---|---|
| Mismo concepto de red | Obligatorio |
| Misma dirección del flujo | Obligatorio cuando aplica |
| Mismo estadístico | Obligatorio |
| Unidad compatible | Obligatorio; se permite conversión determinista |
| Ventana/agregación compatible | Obligatorio |
| Identificadores/topología específica | Excluir |
| Duda semántica | Clasificar `NO_COMPARABLE` |

### 3.7 Preprocesamiento reproducible

**Orden lógico por fold:** limpieza predefinida -> selección de características -> `StandardScaler` cuando corresponda -> SMOTE -> clasificador. Los pasos que aprenden parámetros se ajustan dentro del entrenamiento. El test recibe únicamente transformaciones ya ajustadas.

| Decisión | Configuración V2 |
|---|---|
| **Semilla general** | 42 |
| **Varianza cero** | Excluir características con varianza 0 calculada en entrenamiento. |
| **Correlación alta** | Si \|r\| es mayor o igual a 0,95, conservar una variable del par según menor proporción de faltantes; si empatan, conservar la primera por orden alfabético. La decisión se calcula solo con entrenamiento. |
| **Escalado** | `StandardScaler` ajustado exclusivamente con entrenamiento para los modelos que lo requieran. |
| **Balanceo** | SMOTE, `random_state=42`, solo en entrenamiento/fold de entrenamiento. |

### 3.8 Experimentos de Machine Learning

Los tres algoritmos utilizarán las mismas particiones dentro de cada dataset y la misma métrica de selección. `RandomizedSearchCV` se ejecutará con `scoring=f1_macro`, CV estratificada de cinco pliegues, `random_state=42` y hasta 10 configuraciones por modelo, o todas si el espacio contiene menos de 10.

| Modelo | Espacio de búsqueda fijado |
|---|---|
| **Random Forest** | `n_estimators={200,400,600}; max_depth={None,20,40}; min_samples_split={2,5}; min_samples_leaf={1,2}; max_features={sqrt}`. |
| **XGBoost** | `n_estimators={200,400}; max_depth={4,6,8}; learning_rate={0.05,0.10}; subsample={0.8,1.0}; colsample_bytree={0.8,1.0}`. |
| **MLP** | `hidden_layer_sizes={(128,64),(64,32)}; alpha={0.0001,0.001}; learning_rate_init={0.001}; batch_size=256; max_iter=300; early_stopping=True; n_iter_no_change=10`. |

Por configuración se guardarán hiperparámetros, fold, semilla, tiempo de entrenamiento y métricas. El espacio de búsqueda queda congelado antes de abrir test.

### 3.9 Captura del entorno de ejecución

Antes de medir tiempos, el script de preparación generará `hardware_profile.json` y `software_lock.txt`. Cada resultado de timing incluirá `environment_id`. El perfil debe contener CPU exacta, núcleos físicos/lógicos, RAM total, GPU/VRAM si aplica, almacenamiento, sistema operativo y versiones de librerías. Si el entorno cambia, se crea un `environment_id` nuevo y los tiempos no se combinan con la serie anterior.

### 3.10 Selección del modelo principal

Se seleccionará en GeNIS el algoritmo con mayor F1-macro medio en CV. Si la diferencia absoluta entre los dos primeros es menor o igual a 0,005, se escogerá el de menor desviación estándar; si persiste el empate, el de menor tiempo medio de inferencia medido en validación bajo el mismo `environment_id`. GeNIS-test y CICIDS2017 no participan en esta decisión.

### 3.11 Repeticiones y control de aleatoriedad

Con la configuración final congelada se ejecutarán cinco repeticiones con semillas 42, 52, 62, 72 y 82. Las particiones de prueba permanecen fijas. Se reportará media y desviación estándar. La semilla 42 será la ejecución de referencia para conservar predicciones individuales y figuras detalladas.

### 3.12 Evaluación final en GeNIS 2025

El modelo congelado se aplicará a `genis-30-sec-test.csv`. Por flujo se conservarán `record_id`, `true_class`, `predicted_class`, `model`, `seed`, `environment_id`, `inference_ms` y probabilidades por clase cuando estén disponibles. Se calcularán F1-macro, Accuracy, Precision macro, Recall macro, F1 por clase y matriz de confusión. El test no se utilizará para reabrir ajustes en V2.

### 3.13 Repetición independiente en CICIDS2017

El experimento se repetirá de forma independiente en la muestra CICIDS2017: auditoría, split congelado 80/20, pipeline ajustado solo con entrenamiento, búsqueda de los mismos tres algoritmos, evaluación en test y cinco semillas de estabilidad. La métrica principal vuelve a ser F1-macro. La comparación con GeNIS se interpretará como estabilidad del procedimiento en otra fuente de datos, no como equivalencia directa de clases ni como validación cruzada entre datasets.

### 3.14 Explicabilidad SHAP

Sobre el modelo seleccionado se generarán explicaciones globales y locales. RF/XGBoost usarán TreeExplainer. Si MLP es seleccionado se usará KernelExplainer con 100 instancias de referencia y 500 observaciones de prueba estratificadas con semilla 42. Se conservarán `mean(|SHAP|)`, top-10, contribución acumulada y casos locales. El Jaccard cruzado se calcula exclusivamente sobre `canonical_concept` definido en `feature_mapping.csv`.

### 3.15 Prototipo de alertas

El prototipo V2 se implementará localmente en Flask y mostrará: (1) tipo de alerta; (2) predicción y confianza cuando esté disponible; (3) variables o conceptos con mayor contribución SHAP; (4) explicación en lenguaje operativo; y (5) playbook inicial. Los escenarios de evaluación serán DoS, Port Scan y Brute Force.

### 3.16 Validación del instrumento y piloto

El cuestionario será revisado por tres expertos - dos en ciberseguridad y uno en metodología - respecto a pertinencia, claridad y coherencia. Se realizará una prueba piloto con 2 usuarios. Toda observación y cambio quedará registrado en `expert_matrix.csv` y `pilot_report.md` antes de la evaluación definitiva.

### 3.17 Evaluación exploratoria de usabilidad

Se buscarán 10 sesiones válidas, aceptando un mínimo operativo de 8 y un máximo de 12. Cada participante firmará consentimiento, recibirá un código anónimo y resolverá los tres escenarios. El orden de escenarios se rotará de forma equilibrada. El tiempo se medirá desde la presentación de la alerta hasta la selección del playbook y se registrará en segundos con precisión mínima de 0,1 s.

**Criterios de inclusión.** mayor de 18 años; administrador, encargado o responsable operativo de una pyme de Juliaca; uso regular de computadora o smartphone; sin formación certificada especializada en ciberseguridad/redes; consentimiento firmado.

**Exclusión de sesión.** sesión incompleta; respuestas técnicamente imposibles de interpretar por fallos de registro; participante con formación especializada; conocimiento previo del prototipo por pertenecer al equipo investigador.

Los resultados se reportarán como conteos n/N por escenario; medianas y distribución de Likert; mediana e IQR del tiempo de reacción, además de observaciones recurrentes. Los porcentajes pueden mostrarse como apoyo visual, siempre acompañados por n/N. No se usarán como prueba de generalización poblacional.

### 3.18 Métricas y contrastación

| Criterio | Regla de interpretación |
|---|---|
| **H1** | F1-macro será la métrica principal para comparar y seleccionar modelos en GeNIS. CICIDS2017 se analizará de forma independiente. Se reportarán media, desviación estándar, Accuracy, Precision y Recall como información complementaria. |
| **H2** | SHAP global/local y comparación de top-k solo sobre conceptos homologados. Si la base homologable no es suficiente, el indicador cruzado se declara no aplicable. |
| **H3** | Tiempo medio de inferencia por flujo menor de 500 ms bajo un `environment_id` congelado. SHAP se reporta por separado. |
| **H4** | La comprensión y respuesta inicial se interpretarán de manera conjunta mediante aciertos n/N, respuestas Likert, tiempos de reacción y observaciones del grupo evaluado. |

### 3.19 Registro de cada experimento

| Campo | Ejemplo de registro |
|---|---|
| **ID experimento** | `EXP_GENIS_RF_S042_2026` |
| **Modelo** | Random Forest |
| **Dataset / versión** | GeNIS 2025 / hash registrado |
| **Split** | train oficial + fold / test oficial |
| **Seed** | 42 |
| **Environment ID** | `ENV_001_<hash>` |
| **Configuración** | `configs/EXP_GENIS_RF_S042_2026.json` |
| **Predicciones** | `predictions/EXP_GENIS_RF_S042_2026.csv` |
| **Métricas** | `metrics/EXP_GENIS_RF_S042_2026.json` |
| **Observaciones** | Incidencias y notas asociadas |

### 3.20 Registro de incidencias y versionado

Toda desviación se registrará con fecha, experimento, incidencia, impacto, decisión y justificación. Los fallos no se eliminan silenciosamente. Si un cambio altera partición, métrica principal, espacio de hiperparámetros, método de homologación, entorno de timing o criterio de selección, se crea una nueva versión del protocolo antes de continuar.

### 3.21 Evidencias de reproducibilidad y criterio de finalización

Se conservarán: datasets y hashes; manifests de split; código; configuraciones; semillas; `environment_id`; modelos; predicciones; métricas; logs; versiones de librerías; `feature_mapping.csv`; artefactos SHAP; versión del prototipo; respuestas anonimizadas; incidencias y README con el orden de reproducción. La fase experimental finaliza cuando todas las ejecuciones planificadas están completas, las incidencias están documentadas y cada resultado puede rastrearse hasta datos, configuración y entorno.

**Pregunta de control.** Si se solicita demostrar de dónde salió un valor de F1-macro o un tiempo de inferencia, debe poder identificarse el dataset, archivo y hash, split, pipeline, configuración, semilla, `environment_id`, predicciones y experimento que lo produjeron.

### 3.22 Checklist de protocolo ejecutable

- [ ] Cada objetivo tiene evidencia definida.
- [ ] La procedencia oficial, versión y hash de cada dataset están registrados.
- [ ] Las particiones y semillas están congeladas antes de test.
- [ ] El método de homologación GeNIS-CICIDS2017 está documentado y versionado.
- [ ] La métrica principal es F1-macro en ambos experimentos.
- [ ] El test permanece aislado hasta la selección correspondiente.
- [ ] Existe `hardware_profile.json` y `software_lock.txt` antes de medir tiempos.
- [ ] Existe registro de configuraciones, predicciones, métricas e incidencias.
- [ ] El instrumento tiene juicio de expertos y piloto.
- [ ] La muestra de usuarios se interpreta como exploratoria y no inferencial.
- [ ] Las consideraciones éticas y amenazas a la validez están documentadas.

---

## 4. MATRIZ DE TRAZABILIDAD TÉCNICA

La matriz enlaza cada objetivo con actividades, datos de entrada, procedimientos, controles, evidencias verificables, métricas y resultados esperados. Se actualizará durante la ejecución sin borrar versiones anteriores y mantendrá la trazabilidad de la procedencia de datos, homologación de variables, entorno de hardware y evaluación exploratoria de usabilidad.

| ID | Obj. | Actividad | Entrada / datos | Procedimiento | Configuración / control | Evidencia verificable | Métrica / criterio | Resultado esperado |
|---|---|---|---|---|---|---|---|---|
| **T01** | OE1 | Registrar procedencia | GeNIS y CICIDS2017 | Inventariar fuente, archivo, versión, DOI/URL, hash y etiqueta. | Antes de procesar. | `dataset_manifest.json` + `dataset_metadata.csv` | N° archivos, registros, clases. | Datos identificados y trazables. |
| **T02** | OE1 | Auditar calidad | Datasets registrados | Detectar faltantes, infinitos, duplicados, inválidos y desbalance. | Criterios de exclusión predefinidos. | `dataset_audit_*.csv` + reporte | Integridad, duplicados, distribución. | Calidad documentada. |
| **T03** | OE1/OE2 | Homologar variables | Diccionarios de variables | Mapear por concepto, dirección, estadístico, unidad y ventana; clasificar EXACTA/CONVERTIBLE/NO_COMPARABLE. | Congelar antes de SHAP cruzado. | `feature_mapping.csv` | N° exactas, convertibles, no comparables. | Base válida para comparación SHAP. |
| **T04** | OE1 | Particionar datos | Datasets auditados | GeNIS conserva train/test oficial; CICIDS: 100k estratificado y split 80/20. | Semilla 42; manifests; test aislado. | `split_manifest.csv` | Distribución por clase; solapamiento. | Particiones reproducibles. |
| **T05** | OE1 | Preprocesar sin fuga | Train de cada dataset | Limpieza -> selección -> escalado -> SMOTE. | Todo ajuste dentro de train/fold. | pipeline + `selected_features.csv` | N° variables; clases antes/después. | Pipeline sin leakage. |
| **T06** | OE1 | Entrenar RF | Train procesado | RandomizedSearchCV + 5-fold CV. | `scoring=f1_macro`; seed 42; espacio V2. | `rf_config.json` + CV + modelo | F1-macro principal + métricas complementarias. | Rendimiento y variabilidad RF. |
| **T07** | OE1 | Entrenar XGBoost | Train procesado | RandomizedSearchCV + 5-fold CV. | `scoring=f1_macro`; seed 42; espacio V2. | `xgb_config.json` + CV + modelo | F1-macro principal + complementarias. | Rendimiento y variabilidad XGBoost. |
| **T08** | OE1 | Entrenar MLP | Train procesado | RandomizedSearchCV + 5-fold CV. | Early stopping; seed 42; espacio V2. | `mlp_config.json` + CV + modelo | F1-macro principal + complementarias. | Rendimiento y variabilidad MLP. |
| **T09** | OE1 | Capturar entorno | Estación de trabajo | Registrar CPU, RAM, GPU, almacenamiento, SO y librerías. | `environment_id` congelado antes de timing. | `hardware_profile.json` + `software_lock.txt` | Completitud del perfil. | Tiempos interpretables y reproducibles. |
| **T10** | OE1 | Seleccionar modelo | Resultados CV GeNIS | Aplicar F1-macro medio -> DE -> tiempo de inferencia. | GeNIS-test y CICIDS no participan. | `model_selection.csv` + manifest | F1-macro medio y DE. | Modelo/configuración congelados. |
| **T11** | OE1 | Evaluar GeNIS-test | Modelo congelado + test oficial | Ejecutar 5 semillas con test fijo; conservar predicciones. | Seeds 42,52,62,72,82; mismo `environment_id` para tiempos. | predictions + metrics + confusión | F1-macro, Accuracy, Precision, Recall, tiempo. | Desempeño final GeNIS. |
| **T12** | OE1 | Repetir CICIDS2017 | Muestra 100k + split 80/20 | Repetir pipeline y comparación de RF/XGB/MLP de forma independiente. | Mismos principios; no reabre selección GeNIS. | `cicids_predictions` + metrics | F1-macro principal + complementarias. | Contraste metodológico independiente. |
| **T13** | OE2 | Generar SHAP | Modelo seleccionado + test | TreeExplainer o KernelExplainer según modelo. | MLP: 100 referencias + 500 pruebas; seed 42. | `shap_global.csv` + casos locales | `mean(\|SHAP\|)`, top-10. | Variables dominantes globales/locales. |
| **T14** | OE2 | Comparar explicaciones | Rankings SHAP + mapping | Convertir a `canonical_concept` y calcular solapamiento cuando aplica. | Solo status EXACTA/CONVERTIBLE; no forzar mapping. | `shap_top10.csv` + `shap_jaccard.json` | Contribución acumulada; Jaccard o NA. | Comparación explicable y defendible. |
| **T15** | OE3 | Implementar prototipo | Predicción + SHAP + playbooks | Integrar detección, explicación y respuesta en Flask. | DoS, Port Scan, Brute Force. | Código + capturas + changelog | Flujo funcional; timing registrado. | Prototipo funcional. |
| **T16** | OE3/OE4 | Validar instrumento | Cuestionario + prototipo | Juicio de 3 expertos y piloto con 2 usuarios. | Registrar cada observación/cambio. | `expert_matrix` + `pilot_report` | Pertinencia, claridad, coherencia. | Instrumento listo. |
| **T17** | OE4 | Evaluar usabilidad | 8-12 participantes | Tres escenarios; ataque, playbook, Likert, tiempo y comentarios. | Meta 10; consentimiento; anonimización; orden rotado. | `usability_responses.csv` + `times.csv` | n/N, Likert, mediana/IQR, patrones. | Evidencia exploratoria de comprensión y utilidad. |
| **T18** | OE1-OE4 | Analizar y contrastar | Métricas técnicas + respuestas | Consolidar descriptivos, errores, SHAP y criterios H1-H4. | Sin inferencia poblacional para usuarios. | tablas + matriz de contrastación | H1-H4 según los criterios definidos. | Conclusiones alineadas con evidencia. |
| **T19** | OE1-OE4 | Registrar incidencias | Todos los experimentos | Documentar fecha, impacto, decisión y versión. | Cambio sustancial -> nueva versión. | `incident_log.csv` | N° incidencias y resolución. | Auditoría completa. |
| **T20** | OE1-OE4 | Garantizar reproducibilidad | Todos los artefactos | Integrar datos, hashes, código, configs, seeds, entorno, logs, README. | Versionado de protocolo y software. | Repositorio + README + manifests | Trazabilidad objetivo->resultado. | Experimento reproducible y rastreable. |

### 4.1 Cómo interpretar la matriz

La lógica es: Objetivo -> actividad -> datos -> procedimiento -> configuración/control -> evidencia -> métrica -> análisis -> resultado. La trazabilidad no termina en una cifra: debe permitir regresar desde un F1-macro, un tiempo de inferencia o una respuesta de usabilidad hasta el archivo, split, configuración, semilla y entorno que lo originaron.

---

## 5. AMENAZAS A LA VALIDEZ Y LÍMITES DE INTERPRETACIÓN

| Amenaza | Control / alcance |
|---|---|
| **Validez de datos** | Los datasets fueron capturados en contextos y años diferentes. El protocolo no interpreta CICIDS2017 como réplica idéntica de GeNIS; solo como repetición independiente del procedimiento. |
| **Compatibilidad de variables** | Las herramientas y definiciones de flujo pueden diferir. Por ello, el análisis SHAP cruzado utiliza únicamente conceptos homologados con reglas explícitas. |
| **Desbalance de clases** | Accuracy puede ocultar rendimiento minoritario. Por eso F1-macro es la métrica principal y se reportan métricas por clase. |
| **Muestra de usuarios** | 8-12 participantes no permiten generalizar a todas las pymes de Juliaca. Los resultados describen el grupo observado y sirven para refinar el prototipo. |
| **Rendimiento temporal** | Los tiempos dependen del hardware/software. H3 solo es interpretable junto al `environment_id` correspondiente. |
| **Riesgo de ajuste posterior** | El test no se usa para seleccionar características, hiperparámetros ni reabrir decisiones en la misma versión del protocolo. |

**Consideraciones éticas.** Participación voluntaria con consentimiento informado; respuestas anonimizadas; uso académico de datasets públicos; no se capturará ni intervendrá tráfico real de las redes de las pymes participantes.

## 6. REFERENCIAS

Silva, M., Pinto, D., Vitorino, J., Gonçalves, J., Maia, E., & Praça, I. (2025). *GeNIS: A modular dataset for network intrusion detection and classification*. Data in Brief, 60, 111487. https://doi.org/10.1016/j.dib.2025.111487

Silva, M., Pinto, D., Vitorino, J., Gonçalves, J., Maia, E., & Praça, I. (2025). *GeNIS: GECAD Network Intrusion Scenarios* (Version 1.0.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.14919237

Sharafaldin, I., Habibi Lashkari, A., & Ghorbani, A. A. (2018). Toward generating a new intrusion detection dataset and intrusion traffic characterization. In *Proceedings of the 4th International Conference on Information Systems Security and Privacy (ICISSP)* (pp. 108-116). SciTePress. https://doi.org/10.5220/0006639801080116

Pinto, D., Amorim, I., Maia, E., & Praça, I. (2024). A novel approach to network traffic analysis: The HERA tool. *2024 IEEE 23rd International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom)*, 1850-1856. https://doi.org/10.1109/TrustCom63139.2024.00255

> **Cierre metodológico.** La procedencia y características generales de los datasets se sustentan en el registro oficial de GeNIS en Zenodo, su artículo de datos de 2025 y la página oficial de CICIDS2017 de la University of New Brunswick. Los resultados de la investigación deberán provenir exclusivamente de las ejecuciones experimentales realizadas bajo este protocolo.
