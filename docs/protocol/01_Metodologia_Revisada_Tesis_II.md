# UNIVERSIDAD NACIONAL DE JULIACA
## Facultad de Ciencias de la Ingeniería
### Escuela Profesional de Ingeniería de Software y Sistemas

**Curso:** Seminario de Tesis II — 2026-II  
**Docente:** Liz Huancapaza Hilasaca  
**Autor:** Ccolla Lazarinos, Fernando  
**Título de la tesis:** *Detección de intrusiones de red con aprendizaje automático y técnicas de explicabilidad (XAI) para pequeñas y medianas empresas de Juliaca, Puno*

# METODOLOGÍA REVISADA

## 1. Criterio de revisión metodológica

La presente versión revisa y operacionaliza la metodología desarrollada en el avance de Tesis I para que pueda ejecutarse durante las 17 semanas del semestre 2026-II y sea coherente con el protocolo experimental y la matriz de trazabilidad técnica solicitados en Seminario de Tesis II.

Se fijan antes de la experimentación las decisiones esenciales de datos, partición, preprocesamiento, modelos, métricas, selección, explicabilidad, evaluación de usabilidad y registro de evidencias. El conjunto de prueba no se utilizará para ajustar hiperparámetros, seleccionar características, modificar métricas ni escoger el modelo final.

La investigación se divide en dos componentes complementarios:

1. **Componente técnico:** experimentación computacional comparativa con Random Forest, XGBoost y Perceptrón Multicapa (MLP).
2. **Componente de usabilidad:** evaluación no experimental y transversal de la comprensibilidad, utilidad y capacidad de respuesta frente a las alertas generadas por el prototipo.

---

## 2. Objetivos vinculados con la metodología

### Objetivo general

Desarrollar y evaluar un sistema de detección de intrusiones de red basado en aprendizaje automático e integrado con el marco de explicabilidad SHAP, entrenado principalmente con el conjunto de datos GeNIS 2025, contrastado mediante la repetición independiente del experimento en CICIDS2017, y orientado a la generación de alertas comprensibles, útiles y accionables para administradores de pymes de Juliaca, Puno.

### Objetivos específicos

- **OE1.** Comparar el rendimiento de al menos tres algoritmos de aprendizaje automático en GeNIS 2025 y mediante la repetición independiente del experimento en CICIDS2017.
- **OE2.** Identificar las variables con mayor contribución a las predicciones del modelo seleccionado mediante los valores SHAP.
- **OE3.** Implementar un prototipo que traduzca las atribuciones generadas por SHAP en alertas comprensibles, útiles y accionables para usuarios no técnicos.
- **OE4.** Evaluar la comprensibilidad, utilidad percibida y capacidad de respuesta inicial asociada a las alertas del prototipo en una muestra intencional de 8 a 12 administradores de pymes sin formación especializada en ciberseguridad.

---

## 3. Enfoque, tipo, nivel y diseño

### 3.1. Enfoque

La investigación adopta un **enfoque cuantitativo**, debido a que tanto el rendimiento técnico del sistema como la respuesta de los participantes serán expresados mediante indicadores numéricos.

En el componente técnico se medirán exactitud, precisión macro, sensibilidad o recall macro, puntuación F1 macro, matriz de confusión, tiempo de inferencia y métricas de explicabilidad. En el componente de usabilidad se medirán porcentaje de identificación correcta del ataque, porcentaje de selección correcta del playbook, tiempo de reacción y puntuaciones Likert de claridad, utilidad, confianza e intención de adopción.

### 3.2. Tipo de investigación

La investigación es **aplicada**, porque utiliza conocimientos existentes de aprendizaje automático, ciberseguridad e inteligencia artificial explicable para desarrollar y evaluar una solución concreta orientada a pymes de Juliaca.

### 3.3. Nivel

El alcance es **descriptivo y exploratorio**.

- Es descriptivo porque caracteriza cuantitativamente el rendimiento del sistema y las respuestas de usabilidad.
- Es exploratorio porque la evaluación con 8 a 12 participantes busca obtener evidencia inicial y no pretende generalizar estadísticamente los resultados a todas las pymes de Juliaca.

### 3.4. Diseño

El estudio integra dos diseños:

**a) Experimentación computacional comparativa.**  
Se evaluarán Random Forest, XGBoost y MLP bajo condiciones equivalentes de datos, preprocesamiento, validación y métricas. La métrica principal para la selección será **F1 macro**. Las demás métricas tendrán función complementaria.

**b) Diseño no experimental transversal de usabilidad.**  
Cada participante interactuará una sola vez con escenarios simulados de alertas. No habrá asignación aleatoria a grupos ni manipulación experimental sobre los participantes.

---

## 4. Flujo metodológico general

El proceso técnico seguirá el siguiente orden:

**Datos → auditoría → homologación → partición → preprocesamiento → entrenamiento/validación → selección del modelo → evaluación final → contraste independiente → SHAP → traducción semántica → prototipo → evaluación de usabilidad → análisis → conclusiones.**

Las decisiones posteriores a la apertura del conjunto de prueba no podrán modificar retroactivamente la configuración usada para obtener los resultados. Cualquier cambio sustancial deberá registrarse como una nueva versión del protocolo.

---

## 5. Población, muestra y unidad de análisis

### 5.1. Componente técnico

**Población:** totalidad de flujos etiquetados contenidos en GeNIS 2025 y CICIDS2017.

**Muestra de GeNIS 2025:** se conservarán las particiones oficiales de 30 segundos:

- `genis-30-sec-train.csv`: entrenamiento.
- `genis-30-sec-test.csv`: prueba final.

**Muestra de CICIDS2017:** se construirá un subconjunto reproducible de **100 000 flujos**, estratificado por la taxonomía homologada de clases y generado con **semilla 42**. Para el contraste independiente se reservará una partición de prueba que no será utilizada para ajustar el modelo.

**Unidad de análisis:** un flujo de red individual.

### 5.2. Componente de usabilidad

**Población:** administradores, encargados o responsables operativos de pymes de Juliaca.

**Muestra:** entre **8 y 12 participantes**, seleccionados mediante muestreo no probabilístico intencional.

**Unidad de análisis:** cada participante que interactúa con los escenarios de alerta y completa el cuestionario.

### 5.3. Criterios de inclusión y exclusión

**Participantes — inclusión:**

- Mayor de 18 años.
- Administrador, encargado o responsable operativo de una pyme de Juliaca.
- Uso regular de computadora o smartphone en su actividad laboral.
- Sin formación certificada especializada en ciberseguridad, redes o áreas equivalentes.
- Consentimiento informado firmado.

**Participantes — exclusión:**

- Formación o certificación especializada en ciberseguridad o redes.
- Sesión de evaluación incompleta.
- Cuestionario claramente inválido.
- Conocimiento previo del prototipo por pertenecer al equipo investigador.

**Flujos de red — inclusión:**

- Etiqueta válida.
- Características requeridas disponibles.
- Registro compatible con la taxonomía y las variables definidas para el experimento.

**Flujos de red — exclusión:**

- Etiquetas inconsistentes o corruptas.
- Duplicados exactos.
- Registros técnicamente inválidos documentados en la auditoría.
- Clases no homologables cuando se realice la comparación directa entre datasets.

---

## 6. Conjuntos de datos y función dentro del estudio

| Aspecto | GeNIS 2025 | CICIDS2017 |
|---|---|---|
| Rol | Dataset principal | Dataset de contraste independiente |
| Uso | Entrenamiento, validación y prueba del estudio principal | Repetición independiente para evaluar estabilidad/generalización |
| Tipo de datos | Flujos de red etiquetados | Flujos de red etiquetados |
| Partición | Se conservan las particiones oficiales train/test | Subconjunto estratificado de 100 000 registros; partición reproducible |
| Semilla de operaciones aleatorias | 42 | 42 |
| Riesgo principal | Fuga entre entrenamiento y prueba | Diferencia de distribución y de taxonomía |

### 6.1. Homologación de etiquetas para el contraste

Como ambos datasets no comparten exactamente el mismo espacio de categorías, la comparación entre ellos utilizará una taxonomía común definida **antes** de calcular resultados:

| Superclase de contraste | GeNIS 2025 | CICIDS2017 |
|---|---|---|
| Benigno | Benign | BENIGN |
| DoS-family | DoS | DoS y DDoS compatibles con el análisis |
| Recon/PortScan | Reconnaissance | PortScan |
| Brute Force | Brute Force | Brute Force |

Las clases de CICIDS2017 que no tengan equivalencia defendible con GeNIS 2025 se conservarán en la auditoría, pero no se mezclarán dentro de la comparación principal entre datasets.

Esta decisión evita comparar métricas generadas sobre espacios de clases diferentes.

---

## 7. Auditoría y control de calidad de los datos

Antes del entrenamiento se generará un inventario que registre, como mínimo:

- nombre y versión del dataset;
- archivo de origen;
- número de registros;
- variables disponibles;
- clases y frecuencia por clase;
- valores faltantes;
- duplicados exactos;
- registros inválidos;
- posibles variables identificadoras;
- distribución de clases;
- criterios y cantidad de exclusiones;
- hash o identificador de la versión de datos procesada.

Toda exclusión deberá quedar registrada con su motivo. No se eliminarán observaciones únicamente porque sean difíciles de clasificar o porque empeoren las métricas.

Cuando se identifiquen grupos de flujos relacionados por sesión, archivo, día o escenario de captura, se comprobará si existe riesgo de que el mismo grupo aparezca en entrenamiento y prueba. Si el dataset dispone de un identificador de grupo utilizable, la separación se realizará por grupos; si no existe, esta limitación se dejará documentada.

---

## 8. Preprocesamiento

El preprocesamiento se realizará exclusivamente con información del conjunto de entrenamiento y seguirá este orden:

1. Carga y verificación de tipos.
2. Auditoría de faltantes, duplicados y registros inválidos.
3. Eliminación documentada de registros que cumplan criterios de exclusión.
4. Homologación de nombres y significado de características cuando corresponda.
5. Eliminación de variables de varianza cero.
6. Evaluación de multicolinealidad; para pares con correlación absoluta alta se aplicará una regla fija de selección documentada.
7. Ajuste de `StandardScaler` solo con entrenamiento.
8. Aplicación de SMOTE exclusivamente al entrenamiento y nunca al conjunto de prueba.
9. Aplicación de transformaciones congeladas a validación/prueba, sin recalibración.

Durante la validación cruzada, la selección de características, el escalado y SMOTE se ejecutarán **dentro de cada pliegue de entrenamiento**, evitando fuga de información hacia el pliegue de validación.

---

## 9. Modelos y estrategia de comparación

Se evaluarán tres algoritmos:

- **Random Forest (RF).**
- **XGBoost.**
- **Perceptrón Multicapa (MLP).**

Como control de referencia se registrará el desempeño de una predicción trivial basada en la clase mayoritaria. Este control no competirá como modelo final; únicamente servirá para demostrar que los algoritmos entrenados superan una línea base mínima.

### 9.1. Validación y ajuste

El conjunto de entrenamiento de GeNIS 2025 se evaluará mediante **validación cruzada estratificada de cinco pliegues**, con barajado reproducible y semilla 42.

La búsqueda de hiperparámetros se realizará únicamente sobre entrenamiento. La configuración seleccionada se congelará antes de abrir el conjunto de prueba.

### 9.2. Regla de selección del modelo

La selección seguirá esta jerarquía:

1. Mayor **F1 macro promedio** en la validación cruzada de GeNIS 2025.
2. Si existe empate práctico, menor variabilidad de F1 macro entre pliegues.
3. Si persiste el empate, menor tiempo de inferencia medido en datos de validación.

**CICIDS2017 no participará en la selección del modelo.** Su función será únicamente contrastar, de forma independiente, el comportamiento del modelo ya congelado.

Esta regla evita escoger el modelo en función del conjunto de prueba o del dataset de contraste.

---

## 10. Métricas y criterios definidos antes del análisis

### 10.1. Rendimiento clasificatorio

**Métrica principal:**

- F1 macro.

**Métricas secundarias:**

- Exactitud.
- Precisión macro.
- Recall o sensibilidad macro.
- F1 por clase.
- Matriz de confusión.

### 10.2. Explicabilidad

- Valor absoluto medio de SHAP por variable.
- Porcentaje de contribución acumulada de las 10 variables principales.
- Índice de Jaccard entre conjuntos de variables homologadas dominantes de GeNIS 2025 y CICIDS2017.

### 10.3. Eficiencia

- Tiempo de inferencia por flujo, en milisegundos.
- Tiempo de generación de explicación SHAP por flujo, en milisegundos.

### 10.4. Usabilidad

- Porcentaje de identificación correcta del tipo de ataque.
- Porcentaje de selección correcta del playbook.
- Tiempo de reacción.
- Claridad percibida.
- Utilidad percibida.
- Confianza.
- Intención de adopción.

Las escalas Likert se reportarán de forma descriptiva. No se realizará inferencia poblacional debido al tamaño y tipo de muestra.

---

## 11. Explicabilidad SHAP

Una vez seleccionado y congelado el mejor modelo:

- Para Random Forest o XGBoost se utilizará `TreeExplainer`.
- Para MLP, si resulta seleccionado, se utilizará `KernelExplainer`.
- Para `KernelExplainer` se utilizarán **100 instancias de referencia** y **500 observaciones de prueba**, obtenidas mediante muestreo estratificado reproducible con semilla 42.
- Se conservarán explicaciones globales y casos locales.
- Se registrará la lista de las 10 variables con mayor valor absoluto medio de SHAP.

Las explicaciones obtenidas serán la base para la construcción de las alertas semánticas y no se modificarán con el objetivo de favorecer una interpretación determinada.

---

## 12. Prototipo de alertas y playbooks

El prototipo integrará tres componentes:

1. **Detección:** clase predicha y nivel de confianza disponible.
2. **Explicación:** variables que más contribuyeron según SHAP.
3. **Traducción operativa:** mensaje en lenguaje comprensible y playbook inicial.

Los escenarios de evaluación representarán:

- DoS.
- Port Scan / reconocimiento.
- Brute Force.

La interfaz será desarrollada con Flask o Tkinter, conforme al avance de la tesis. Antes de la aplicación definitiva se realizará una prueba piloto con **2 usuarios**.

---

## 13. Instrumento de evaluación de usabilidad

El cuestionario se organizará en tres partes:

### Parte A. Perfil del participante

Datos demográficos y nivel de experiencia tecnológica necesarios para caracterizar la muestra.

### Parte B. Tres escenarios de interacción

Para cada alerta el participante deberá:

1. identificar el tipo de ataque entre opciones cerradas;
2. seleccionar el playbook inicial entre opciones cerradas;
3. valorar claridad y confianza en escala Likert;
4. completar la interacción mientras se registra el tiempo de reacción.

### Parte C. Evaluación global

Cinco ítems Likert relacionados con claridad general, utilidad, confianza e intención de adopción.

El instrumento será revisado por **tres expertos**: dos del área de ciberseguridad y uno de metodología. La prueba piloto con 2 usuarios permitirá detectar problemas de comprensión antes de la aplicación definitiva.

---

## 14. Procedimiento alineado con las 17 semanas de Tesis II

| Semana | Actividad metodológica principal | Evidencia |
|---:|---|---|
| 1 | Revisar Tesis I y congelar decisiones metodológicas | Protocolo V1.0 y matriz de decisiones |
| 2 | Descargar/inspeccionar datasets y preparar instrumento | Inventario de datasets + cuestionario |
| 3 | Auditoría y homologación | Reporte EDA + tabla de equivalencias |
| 4 | Preprocesamiento reproducible | Pipeline y datos procesados v1 |
| 5 | Preparación experimental | Configuraciones, semillas y datasets congelados |
| 6 | Evaluación Unidad I | Paquete de evidencias metodológicas |
| 7 | Entrenamiento RF/XGBoost/MLP | Modelos y resultados de validación |
| 8 | Ajuste y selección | Modelo congelado + tabla comparativa |
| 9 | Explicabilidad SHAP | Ranking, gráficos y casos explicados |
| 10 | Prototipo de alertas | Prototipo funcional v1 |
| 11 | Evaluación técnica y piloto | Métricas + informe del piloto |
| 12 | Evaluación Unidad II | Demostración + resultados preliminares |
| 13 | Contraste CICIDS2017 y preparación de campo | Resultados de contraste + consentimientos |
| 14 | Evaluación de usabilidad | Base de respuestas y tiempos |
| 15 | Análisis de resultados | Tablas, gráficos y consistencia interna |
| 16 | Contrastación y discusión | Matriz de contrastación + discusión |
| 17 | Evaluación final | Tesis consolidada + evidencias reproducibles |

La redacción y documentación se desarrollarán de manera transversal durante las 17 semanas.

---

## 15. Análisis de datos

### 15.1. Análisis técnico

Por cada modelo se reportarán:

- media y desviación estándar de F1 macro en los cinco pliegues;
- exactitud, precisión macro, recall macro y F1 macro;
- F1 por clase;
- matriz de confusión;
- tiempo de inferencia;
- resultados del conjunto de prueba;
- resultados del contraste independiente en CICIDS2017.

El resultado principal de prueba se calculará **una vez que el modelo y las transformaciones hayan sido congelados**.

### 15.2. Análisis SHAP

Se reportarán:

- ranking global de variables;
- contribución acumulada de las 10 variables principales;
- explicaciones locales de casos seleccionados;
- Jaccard de variables homologadas entre GeNIS 2025 y CICIDS2017.

### 15.3. Análisis de usabilidad

Se utilizarán:

- frecuencias y porcentajes;
- media y desviación estándar del tiempo de reacción;
- promedios de ítems Likert con interpretación descriptiva;
- alfa de Cronbach de forma exploratoria, interpretado con cautela por el tamaño reducido de muestra.

No se utilizará estadística inferencial para generalización poblacional.

---

## 16. Criterios para contrastar las hipótesis

| Hipótesis | Criterio previamente fijado |
|---|---|
| H1 — Rendimiento | Al menos RF o XGBoost alcanza exactitud ≥ 90,0 % en GeNIS 2025 y el modelo seleccionado mantiene F1 macro ≥ 0,85 en el contraste de CICIDS2017 |
| H2 — Explicabilidad | Las 10 variables principales concentran ≥ 70,0 % de la contribución absoluta total y Jaccard ≥ 0,40 en variables homologadas |
| H3 — Eficiencia | Tiempo de inferencia por flujo < 500 ms en la estación de trabajo del estudio |
| H4 — Usabilidad | Identificación correcta del ataque ≥ 70,0 % y selección correcta del playbook ≥ 60,0 % |

Los criterios no podrán modificarse después de observar los resultados finales.

---

## 17. Reproducibilidad y trazabilidad

Por cada ejecución se conservarán:

- versión del dataset;
- partición utilizada;
- variables seleccionadas;
- configuración del preprocesamiento;
- algoritmo e hiperparámetros;
- semilla;
- versión de software;
- fecha y hora;
- tiempo de ejecución;
- predicciones;
- métricas;
- archivos SHAP;
- incidencias.

Cada experimento utilizará un identificador único, por ejemplo:

`EXP_GENIS_RF_CV_S42_001`

La estructura mínima de evidencias será:

```text
tesis_experimentos/
├── data_metadata/
├── splits/
├── configs/
├── logs/
├── models/
├── predictions/
├── metrics/
├── shap/
├── prototype/
├── usability/
└── reports/
```

Una modificación sustancial del procedimiento generará una nueva versión del protocolo. Ningún fallo o resultado negativo será eliminado del registro.

---

## 18. Amenazas a la validez y medidas de control

| Amenaza | Medida de control |
|---|---|
| Fuga de información | Ajustar selección, escalado y SMOTE únicamente con entrenamiento; test aislado |
| Desbalance de clases | SMOTE solo en entrenamiento y uso de F1 macro |
| Dependencia entre flujos relacionados | Auditoría de grupos/sesiones y partición por grupos cuando exista identificador utilizable |
| Diferencias entre datasets | Taxonomía de clases y características homologadas definida antes del contraste |
| Sobreajuste de hiperparámetros | Validación cruzada de cinco pliegues y congelamiento previo al test |
| Selección oportunista de métricas | F1 macro y criterios de hipótesis fijados antes del análisis final |
| Muestra pequeña de usuarios | Alcance exploratorio; sin generalización poblacional |
| Sesgo del instrumento | Juicio de tres expertos y piloto con 2 usuarios |
| Variabilidad del hardware | Misma estación de trabajo y registro de condiciones de ejecución |

---

## 19. Consideraciones éticas

La participación de administradores de pymes será voluntaria y requerirá consentimiento informado. Las respuestas serán registradas de forma anónima o codificada y solo se utilizarán con fines académicos.

No se capturará tráfico real de las redes de las pymes participantes ni se desplegarán herramientas intrusivas en su infraestructura. El componente técnico utilizará datasets públicos de investigación y se ejecutará fuera de línea en la estación de trabajo del investigador.

---

## 20. Criterio de finalización de la fase metodológica

La metodología se considerará lista para ejecución cuando:

- cada objetivo tenga actividades, evidencias y métricas asociadas;
- datasets y particiones estén identificados;
- la auditoría tenga criterios de exclusión predefinidos;
- el preprocesamiento evite fuga de información;
- los comparadores y la métrica principal estén fijados;
- el modelo se seleccione sin utilizar el test ni CICIDS2017;
- exista un plan de trazabilidad de cada experimento;
- el instrumento de usabilidad tenga plan de validación y piloto;
- amenazas y consideraciones éticas estén documentadas.

**Pregunta de control:** si el estudio comenzara mañana, ¿podría ejecutarse sin decidir después qué métrica, dato, modelo, criterio de exclusión o evidencia conviene utilizar? La respuesta esperada con esta metodología revisada es **sí**.
