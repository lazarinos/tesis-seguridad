# CAPÍTULO II: REVISIÓN DE LA LITERATURA

---

## 2.1 Antecedentes de la Investigación

La presente revisión consolida los estudios previos que fundamentan técnica y metodológicamente esta investigación. Se han seleccionado 23 estudios de alto rigor científico —15 internacionales, 7 nacionales y 1 local—, estructurados en función de su relevancia sobre sistemas de detección de intrusiones (IDS) y la aplicabilidad de la Inteligencia Artificial Explicable (XAI).

---

### 2.1.1 Antecedentes Internacionales

La literatura internacional converge en dos grandes líneas de investigación: la evaluación comparativa de técnicas XAI aplicadas a IDS, y el estudio del rendimiento de modelos de machine learning bajo entornos de recursos variables.

En la primera línea, Gaspar et al. (2024) evaluaron la aplicabilidad de LIME y SHAP sobre un modelo de Perceptrón Multicapa para la detección de intrusiones, utilizando el dataset ADFA-LD y validando las explicaciones mediante análisis riguroso de perturbación. Sus resultados evidencian que SHAP mantiene una fidelidad superior para justificar anomalías de red, sustentando la viabilidad técnica de implementar XAI post-hoc en entornos IDS. Complementando este hallazgo, Arreche et al. (2024a) desarrollaron el framework E-XAI para evaluar cuantitativamente la explicabilidad de cajas negras, aplicando LIME y SHAP sobre siete modelos predictivos y midiendo métricas como exactitud descriptiva y estabilidad; comprobaron que SHAP es significativamente más robusto temporalmente que LIME. Este hallazgo justifica la elección de SHAP como motor de explicabilidad para garantizar alertas confiables en PyMES. En una profundización de dicho framework, Arreche et al. (2024b) propusieron el framework XAI-IDS en el cual compararon siete modelos sobre tres conjuntos de datos (NSL-KDD, UNSW-NB15 y CICIDS2017) integrando SHAP y LIME para evaluar la carga computacional en tiempo real, concluyendo que clasificadores basados en ensamble como Random Forest superan el 96% de exactitud y ofrecen una latencia óptima para despliegues prácticos, aportando la base arquitectónica de explicabilidad que esta tesis adaptará para pequeñas y medianas empresas.

Profundizando en el análisis forense, Hermosilla et al. (2025a) realizaron una comparativa entre SHAP y LIME aplicando XGBoost, evidenciando mediante índices de Jaccard que SHAP posee mayor consistencia para justificar intrusiones en auditorías legales. Esto se alinea con la necesidad de entregar reportes fiables a los administradores de red. Asimismo, Hermosilla et al. (2025b) demostraron que es posible traducir los pesos matemáticos generados por SHAP en justificaciones operativas claras, constituyendo la base central del diseño de "playbooks" para PyMES propuesto en esta investigación. En esa misma dirección metodológica, Mia et al. (2024) diseñaron una metodología visual utilizando gráficos SHAP para diagnosticar errores de clasificación en algoritmos de ensamble, demostrando que el análisis visual permite corregir sesgos del dataset; técnica que se empleará para validar empíricamente el modelo entrenado.

En la segunda línea, centrada en el rendimiento bajo entornos restringidos, Corea et al. (2024) ejecutaron un análisis comparativo de seis modelos —incluyendo SVM, KNN y Random Forest— sobre el dataset UNSW-NB15, entrenándolos hasta alcanzar un límite de parada del 90% de exactitud. Su análisis aplicó la técnica de sensibilidad a la oclusión (Occlusion Sensitivity) para estimar la importancia de las características de entrada, descubriendo que Random Forest destaca por su robustez y eficiencia temporal al depender de muy pocas variables críticas, lo cual sustenta la propuesta de utilizar modelos eficientes sobre hardware modesto. Wang et al. (2020), por su parte, desarrollaron un marco de machine learning explicable sobre el dataset NSL-KDD, validando que SHAP puede mapear exitosamente la relación causal entre características del tráfico y tipos de ataque específicos, aportando la base teórica para la traducción semántica de alertas propuesta en esta tesis.

En el ámbito del aprendizaje profundo, Alabdulatif (2025) propuso un ensamble híbrido que combina redes neuronales artificiales (ANN) y máquinas de vectores de soporte (SVM) con Random Forest como meta-clasificador, asistido por SHAP sobre el dataset NSL-KDD. Logró una exactitud del 99.40% y diseñó una interfaz basada en Flask en AWS EC2 para la visualización en tiempo real de las explicaciones de red, trabajo que fundamenta la importancia de reducir la ceguera por alertas mediante interfaces visuales interactivas para analistas de seguridad. En el contexto IoT, Alabbadi et al. (2025) implementaron un sistema IDS basado en aprendizaje profundo mediante redes neuronales convolucionales unidimensionales (1-D CNN) y DNN sobre el dataset TON_IoT. En su metodología, aplicaron SHAP y LIME de forma post-hoc para justificar las predicciones del modelo y explicar las características de las clases en tiempo real, alcanzando exactitudes del 99.24% en datos de red y hasta un 100% en telemetría IoT.

Sobre la adaptabilidad y resiliencia de los modelos, Jameel et al. (2025) midieron las brechas de generalización del IDS frente a variantes no entrenadas de ataques DoS sobre CICIDS2017, determinando que la exactitud puede caer drásticamente ante variaciones del ataque pero que SHAP permite aislar el origen causal del error. Este hallazgo justifica metodológicamente el uso de un dataset moderno como GeNIS y su contraste con benchmarks para evaluar capacidad de generalización real.

Finalmente, en arquitecturas distribuidas y perimetrales, Fatema et al. (2025) aplicaron un enfoque de aprendizaje federado (FedAvg) combinado con SHAP sobre el dataset CICIoT2023, logrando una exactitud global del 94.2% mientras se preserva la privacidad de los datos locales mediante explicaciones unificadas globales. Larriva-Novo et al. (2024) combinaron aprendizaje por refuerzo y SHAP para categorizar niveles de gravedad en ataques de red, lo que se relaciona con el propósito de asignar prioridades a las notificaciones generadas. Por su parte, Nkoro et al. (2024) diseñaron un marco de ciberdefensa Zero Trust para el Internet de las Cosas (IoT) marítimo aplicando XGBoost y SHAP sobre CICIDS2017, alcanzando una precisión del 97.4% y demostrando la capacidad de SHAP para aislar variables no informativas. Asimismo, Taheri et al. (2025) evaluaron el impacto computacional de SHAP en entornos de aprendizaje federado para dispositivos de borde en vehículos conectados, logrando una exactitud del 95.3% y validando que las explicaciones locales pueden ejecutarse eficientemente sin latencias críticas, garantizando la factibilidad de uso de hardware de bajo costo.

---

### 2.1.2 Antecedentes Nacionales

La literatura peruana evidencia una marcada transición desde las auditorías perimetrales estáticas hacia la adopción empírica del Machine Learning aplicado a la seguridad.

En el ámbito del uso de algoritmos de clasificación para la detección de intrusiones, Figueroa Dextre y Cañihua Ccapa (2024) desarrollaron un IDS enfocado en empresas de Lima evaluando Random Forest y Regresión Logística sobre el dataset CICIDS2017, hallando que Random Forest proporciona la mayor exactitud (95%) mientras que la Regresión Logística destacó en velocidad de inferencia. Esta tesis valida la viabilidad operativa de estos modelos dentro del sector empresarial peruano, sustentando directamente las elecciones algorítmicas de la presente investigación. En el sector minero, Ore Huacles y Donaire Arbieto (2021) utilizaron telemetría SCADA para detectar ciberataques industriales mediante árboles de decisión, logrando un 93.6% de precisión sobre variables de red continuas, confirmando la pertinencia de algoritmos ligeros para entornos productivos con presupuestos y capacidades de procesamiento limitados.

En la optimización de la seguridad perimetral, Torres Valle y Abensur Rojas (2025) diseñaron un IDS híbrido en colegios privados de Lima Metropolitana integrando el motor de firmas Snort con un clasificador XGBoost, determinando que este enfoque disminuye los falsos negativos en un 15%. Este resultado aporta el concepto metodológico de que el Machine Learning es el complemento ideal para infraestructuras que anteriormente dependían exclusivamente de reglas estáticas. Manrique Huamaní y Santiváñez Guarniz (2021), al analizar el rendimiento de múltiples motores IDS en redes SDN, alertaron sobre los cuellos de botella en el procesamiento, lo cual advierte sobre la necesidad de asegurar que el algoritmo propuesto no degrade el ancho de banda comercial de la PyME objetivo.

A nivel de estrategias defensivas estructurales, Hernandez Legua (2025) diseñó un modelo de seguridad Zero Trust con DLP para el sector eléctrico, comprobando la eficacia de segmentar las redes estrictamente. Su investigación aporta la visión metodológica de asumir que cualquier red interna opera bajo un nivel de riesgo por defecto, lo cual justifica la implementación de monitoreo inteligente continuo como el propuesto en esta tesis.

Respecto a la usabilidad e interacción con los administradores, Yauri Lozano (2017) creó la aplicación móvil SnorUNI acoplada a Snort para notificar eventos de seguridad con latencias menores a 1.5 segundos, demostrando la factibilidad técnica de canalizar alertas hacia interfaces sencillas; concepto paralelo al objetivo de usabilidad de alertas de esta investigación. En la misma línea de accesibilidad tecnológica, Jiménez Alegría (2016) desplegó un IDS/IPS open source sobre hardware embebido (Raspberry Pi) para blindar la red del Ministerio Público de Puno, documentando el bloqueo del 40% de los intentos de intrusión y confirmando que en regiones fuera de la capital es imperativo concebir arquitecturas de seguridad sobre hardware comercial de bajo costo.

---

### 2.1.3 Antecedentes Locales

En el contexto específico de la ciudad de Puno, Zanabria Ticona (2023) desarrolló una evaluación exhaustiva de seguridad informática en la plataforma virtual del Vicerrectorado de Investigación de la Universidad Nacional del Altiplano. Empleando la normativa ISO 17799 y técnicas de pentesting, identificó severas vulnerabilidades de exposición y confirmó accesos no autorizados dentro de la red de la institución. Su investigación concluyó que las redes locales en el altiplano sufren de un profundo déficit de políticas de monitoreo activo, exponiendo la información crítica de forma continua.

Este estudio constituye el justificante regional directo de la presente tesis, pues comprueba empíricamente que la región Puno carece de visibilidad estructurada sobre sus propias amenazas cibernéticas. Ante este escenario, la implementación de un IDS con aprendizaje automático y notificaciones explicables emerge como una solución crítica y urgente, especialmente diseñada para salvaguardar a las PyMES comerciales de Juliaca que adolecen de soporte técnico especializado.

---

## 2.2 Estado del Arte

### 2.2.1 Tendencias Actuales en IDS con XAI

La convergencia entre los sistemas de detección de intrusiones y la Inteligencia Artificial Explicable representa la tendencia dominante en la literatura científica reciente (2024–2025). Esta línea de investigación responde a una limitación estructural reconocida: los modelos de alta precisión predictiva —ensambles de árboles, redes neuronales profundas— operan como cajas negras cuya lógica interna resulta inaccesible para el operador humano. La comunidad científica ha respondido consolidando a SHAP como el estándar de facto para la explicabilidad post-hoc en entornos IDS (Gaspar et al., 2024; Arreche et al., 2024a; Hermosilla et al., 2025a), mientras que LIME ocupa un rol secundario y complementario.

Una segunda tendencia emergente es la integración de XAI en arquitecturas distribuidas, incluyendo aprendizaje federado (Fatema et al., 2025) e implementaciones en dispositivos de borde con restricciones computacionales (Nkoro et al., 2024; Taheri et al., 2025). Esta dirección confirma que la explicabilidad algorítmica ya no es exclusiva de entornos con alta capacidad de cómputo, lo cual es particularmente relevante para el contexto de PyMES con hardware modesto como el de Juliaca.

Una tercera tendencia es el diseño de interfaces orientadas al usuario no técnico. Trabajos como el de Alabdulatif (2025) y el framework E-XAI de Arreche et al. (2024a) no solo evalúan la exactitud matemática del modelo, sino también la comprensibilidad de las explicaciones generadas, desplazando el foco desde el rendimiento puro hacia la utilidad práctica del sistema para el operador.

### 2.2.2 Comparación de Investigaciones y Métodos Relevantes

Al comparar los estudios revisados, se identifican tres patrones metodológicos predominantes. El primero es el uso de datasets de referencia consolidados: CICIDS2017, NSL-KDD y UNSW-NB15 concentran la mayoría de experimentos, lo que facilita la comparabilidad entre modelos pero limita la representatividad de escenarios de red emergentes. El segundo patrón es la preferencia por algoritmos de ensamble —particularmente Random Forest y XGBoost— sobre modelos de aprendizaje profundo cuando se prioriza la eficiencia computacional (Corea et al., 2024; Figueroa Dextre & Cañihua Ccapa, 2024). El tercero es la evaluación del rendimiento clasificatorio exclusivamente sobre métricas de exactitud y F1-Score, sin incorporar métricas de usabilidad del operador.

Esta última observación constituye una diferencia sustancial entre los estudios previos y la presente investigación, que incorpora explícitamente indicadores de comprensión y tiempo de reacción del usuario como dimensiones medibles de la variable dependiente.

### 2.2.3 Resultados Relevantes Consolidados

| Estudio | Dataset | Modelo | Exactitud | Uso de XAI |
|---|---|---|---|---|
| Alabdulatif (2025) | NSL-KDD | Ensamble híbrido (ANN+SVM) con RF meta-clasificador | 99.40% | SHAP post-hoc + Flask |
| Arreche et al. (2024b) | Múltiple (NSL-KDD / UNSW-NB15 / CICIDS2017) | 7 modelos de ML (incl. Random Forest) | >96% | Framework XAI-IDS (SHAP/LIME) |
| Corea et al. (2024) | UNSW-NB15 | Random Forest / Multi-clasificador | 90% | Occlusion Sensitivity |
| Alabbadi et al. (2025) | TON_IoT | 1-D CNN / DNN | 99.24% (red) / 100% (IoT) | SHAP/LIME post-hoc |
| Figueroa Dextre & Cañihua Ccapa (2024) | CICIDS2017 | Random Forest | 95% | Sin XAI |
| Fatema et al. (2025) | CICIoT2023 | Aprendizaje Federado (MLP) | 94.2% | SHAP federado |
| Mia et al. (2024) | UNSW-NB15 / Edge-IIoTset | Ensamble (RF/XGBoost) | N/A | Gráficos SHAP visuales |
| Wang et al. (2020) | NSL-KDD | XGBoost / Random Forest / MLP | >99% | SHAP causalidad |

---

## 2.3 Análisis Crítico de la Literatura

### 2.3.1 Limitaciones Encontradas en los Estudios Previos

A pesar del avance consolidado en la literatura, los estudios revisados presentan limitaciones recurrentes que abren espacios de contribución científica directa. En primer lugar, la mayoría de investigaciones internacionales emplea exclusivamente datasets de benchmarking clásicos —CICIDS2017, NSL-KDD, UNSW-NB15— cuya composición de tráfico refleja entornos de red de laboratorio o de grandes infraestructuras corporativas, lo que reduce su representatividad para redes pequeñas y heterogéneas como las de las PyMES de Juliaca. En segundo lugar, los estudios que incorporan XAI se enfocan predominantemente en la evaluación matemática de las métricas de explicabilidad —consistencia, estabilidad, fidelidad— sin contrastar empíricamente si dichas explicaciones son comprensibles para usuarios no especializados. Trabajos como Arreche et al. (2024a) y Hermosilla et al. (2025b) constituyen excepciones parciales, pero no incluyen estudios de usabilidad con administradores reales. En tercer lugar, los estudios nacionales peruanos, aunque técnicamente sólidos, no incorporan herramientas XAI en sus propuestas, operando los modelos como cajas negras sin mecanismo de justificación de alertas para el operador.

### 2.3.2 Brechas Científicas Identificadas

Del análisis crítico de la literatura emergen tres brechas científicas relevantes que justifican la originalidad de esta investigación. La primera es la **brecha de contextualización regional**: no existe ningún estudio que evalúe un IDS basado en Machine Learning con explicabilidad XAI en el contexto específico de PyMES peruanas, y menos aún en la región Puno o la ciudad de Juliaca. La segunda es la **brecha de usabilidad orientada al operador no técnico**: la literatura existente mide la calidad de las explicaciones desde la perspectiva matemática, pero carece de evidencia experimental sobre cómo estas explicaciones impactan la toma de decisiones de un administrador de red sin formación en ciencias de la computación. La tercera es la **brecha de dataset moderno y contextualizado**: el uso del dataset GeNIS (Silva et al., 2025) —publicado en 2025 y diseñado con tráfico modular y actualizado— no ha sido explorado en combinación con SHAP y un framework de usabilidad como NEAT.

### 2.3.3 Oportunidades de Investigación

Las brechas identificadas configuran tres oportunidades concretas que esta tesis aborda. La primera es diseñar y validar un IDS con XAI entrenado sobre el dataset GeNIS y evaluado en condiciones representativas del entorno de red de PyMES comerciales de Juliaca. La segunda es desarrollar y testear un mecanismo de traducción semántica basado en SHAP y el marco NEAT que transforme los valores matemáticos de explicabilidad en alertas comprensibles y accionables para usuarios sin perfil técnico especializado. La tercera es aportar evidencia empírica peruana sobre la relación entre la calidad de las explicaciones XAI y la eficacia de respuesta del operador, contribuyendo a llenar el vacío de investigación aplicada en ciberseguridad en el contexto andino.

---

## 2.4 Bases Teóricas

El marco teórico no se limita a compilar herramientas informáticas, sino que expone los mecanismos causales y científicos que enlazan la captura matemática de intrusiones con la posterior toma de decisiones del usuario, fusionando la teoría del aprendizaje estadístico, la teoría de juegos y el diseño centrado en el ser humano.

### 2.4.1 Aprendizaje Automático en la Clasificación de Flujos de Red

El aprendizaje automático (Machine Learning) se sustenta en un enfoque probabilístico y conexionista que contrasta fundamentalmente con el paradigma determinista de la ciberseguridad tradicional. Las medidas de seguridad clásicas operan bajo un enfoque simbólico: evalúan reglas estrictas y cotejan firmas binarias exactas frente a un flujo de datos. Este mecanismo resulta eficaz para amenazas conocidas y catalogadas, pero es estructuralmente incapaz de detectar variantes no registradas o patrones emergentes de ataque.

El paradigma del Machine Learning supera esta limitación permitiendo a los algoritmos inferir patrones latentes en repositorios de datos masivos sin depender de reglas codificadas previamente. Desde la perspectiva estadística, los algoritmos de ensamble —como Random Forest o XGBoost— combinan y ponderan múltiples modelos predictivos de aprendizaje débil, lo que incrementa la capacidad de generalización del sistema frente a datos no vistos durante el entrenamiento. Según Goodfellow et al. (2016), este paradigma computacional capacita a los IDS para calcular relaciones no lineales entre variables multivariadas del tráfico —como la varianza de inter-llegada de paquetes o la densidad de bytes— permitiendo identificar variaciones sutiles de ataques de día cero y ataques polimórficos que serían completamente invisibles para los enfoques estáticos por firmas.

Desde la perspectiva conexionista, los modelos de aprendizaje profundo —como las redes LSTM y GRU— extienden esta capacidad hacia el análisis de secuencias temporales de tráfico, capturando dependencias a largo plazo entre eventos de red. Esta dualidad entre el enfoque estadístico-ensamblado y el conexionista-profundo constituye la base algorítmica que sustenta las propuestas híbridas más recientes en el campo (Alabdulatif, 2025), y define el espacio de selección de modelos de esta investigación.

### 2.4.2 Teoría de Juegos y Explicabilidad Computacional (SHAP)

Pese a su gran exactitud predictiva, la arquitectura compleja de los ensambles de árboles de decisión y las redes neuronales desencadena el problema cognitivo de la "caja negra": el algoritmo entrega un dictamen preciso pero humanamente opaco. Para abordar formalmente este problema, Lundberg y Lee (2017) formularon el modelo SHAP (SHapley Additive exPlanations), fundamentado en la Teoría de Juegos Cooperativos desarrollada por el matemático Lloyd Shapley (1953).

Aplicado al paradigma de un IDS, esta teoría considera que cada variable o característica del tráfico de red —como la frecuencia de bytes, los puertos de transmisión o las banderas TCP— opera como un "jugador" dentro de una coalición, mientras que la predicción de la alerta actúa como la "ganancia" del juego. SHAP efectúa permutaciones exhaustivas para calcular el impacto marginal exacto que aporta cada variable individual al resultado final. Este modelo cumple axiomáticamente con tres principios irrenunciables: *eficiencia* —las contribuciones siempre suman la predicción total del modelo—, *simetría* —variables con impacto idéntico reciben puntuaciones iguales— y *consistencia* —un cambio algorítmico que acentúe la importancia de un atributo nunca decrecerá su valor SHAP—. Esta coherencia teórica certifica que la emisión de una alerta anómala no es probabilística al azar, sino que posee un desglose causal matemáticamente irrefutable.

La superioridad de SHAP sobre métodos alternativos como LIME ha sido consistentemente demostrada en la literatura: Arreche et al. (2024a) comprobaron su mayor robustez temporal, mientras que Hermosilla et al. (2025a) evidenciaron su mayor consistencia para auditorías legales mediante índices de Jaccard. Este consenso científico fundamenta la elección de SHAP como único motor de explicabilidad en la presente propuesta.

### 2.4.3 Diseño Centrado en el Usuario: Usabilidad de Seguridad y Prevención de Fatiga por Alertas

La eficacia de un IDS no se agota en su exactitud clasificatoria; su verdadero impacto operativo depende de la calidad de la interacción entre el sistema y el operador humano. La teoría del factor cognitivo en entornos de estrés identifica el fenómeno de "ceguera de advertencias" o fatiga por alertas (*warning blindness*): cuando un administrador inexperto recibe cientos de alertas técnicas con lenguaje cifrado e incomprensible, desarrolla una habituación subconsciente que lo lleva a ignorar advertencias potencialmente críticas (Reeder et al., 2011). Este mecanismo psicológico representa el principal punto de falla en la cadena de seguridad de las PyMES, donde la figura del administrador de red suele ser un empleado polivalente sin formación técnica especializada.

Para subvertir esta barrera, se emplea el modelo heurístico NEAT (*Necessary, Explained, Actionable, Tested*). Este marco metodológico dicta que una notificación de seguridad efectiva debe cumplir cuatro condiciones: (1) emitirse solo cuando sea vitalmente necesaria, evitando la saturación informativa; (2) explicar el peligro sin sobrecarga léxica, utilizando lenguaje comprensible para el destinatario; (3) ofrecer una operación accionable —denominada "playbook"— que el usuario pueda ejecutar sin conocimientos avanzados; y (4) ser evaluada con su usuario destinatario real antes de ser desplegada. En esta investigación, el marco NEAT actúa como el componente decodificador semántico que toma los valores abstractos extraídos por SHAP y los traduce en recomendaciones operativas directas.

---

## 2.5 Marco Conceptual (Definición de Términos Básicos)

Con la finalidad de dotar de rigurosidad terminológica al presente estudio, se exponen las siguientes definiciones operacionales fundamentadas en la literatura científica especializada:

**Alerta de Seguridad Accionable:** Notificación interactiva producida por una herramienta de ciberseguridad cuyo propósito no solo es describir fehacientemente un incidente de riesgo, sino incorporar secuencialmente una orden o procedimiento inicial de contención —playbook— ejecutable incluso por usuarios de bajo perfil técnico (Reeder et al., 2011).

**Aprendizaje Automático (Machine Learning):** Disciplina de la inteligencia artificial orientada a la construcción de modelos estadísticos predictivos que proveen a un sistema la capacidad de inferir y asimilar patrones de comportamiento a partir de datos empíricos de entrenamiento, sin depender de programación deductiva basada en reglas (Mitchell, 1997).

**Ceguera de Alertas (Warning Blindness):** Sesgo de comportamiento humano evidenciado en la Interacción Humano-Computadora (HCI) mediante el cual los individuos, tras una sobreexposición sostenida a advertencias técnicas abrumadoras o de baja relevancia, insensibilizan su respuesta cognitiva e ignoran subconscientemente notificaciones informáticas vitales (Reeder et al., 2011).

**Exactitud (Accuracy):** Métrica de rendimiento en clasificación supervisada que evalúa la fracción de predicciones correctas sobre el total de casos analizados, utilizada como indicador del éxito predictivo global del modelo en datasets de tráfico de red (Mitchell, 1997).

**F1-Score:** Promedio armónico balanceado entre la precisión y la sensibilidad que cuantifica el desempeño de un algoritmo de clasificación, siendo de particular relevancia técnica en entornos de ciberseguridad caracterizados por datasets de tráfico de red altamente desbalanceados (Goodfellow et al., 2016).

**Inteligencia Artificial Explicable (XAI):** Conjunto estructurado de metodologías, marcos matemáticos e interfaces que permiten hacer comprensibles y auditables las lógicas internas, los ponderadores y el razonamiento estadístico que utiliza un algoritmo avanzado —caja negra— para emitir sus decisiones, fomentando la confianza del usuario final (Arreche et al., 2024a).

**Pequeña y Mediana Empresa (PyME):** Estructura organizacional caracterizada por escalas operativas moderadas y presupuesto comercial acotado. Tecnológicamente, presentan niveles crecientes de digitalización mientras padecen una aguda ausencia de profesionales o departamentos internos dedicados a la seguridad de la información.

**Precisión (Precision):** Proporción de predicciones positivas que son verdaderamente correctas, cuya función en un sistema de detección de intrusiones es cuantificar la confiabilidad de las alertas emitidas y medir la tasa de falsos alarmas para evitar la fatiga del operador (Arreche et al., 2024b).

**Sensibilidad (Recall):** Proporción de casos positivos reales que son identificados exitosamente por el clasificador, cuya función en ciberdefensa es medir la capacidad de un IDS para detectar intrusiones sin incurrir en ceguera o falsos negativos ante incidentes críticos (Gaspar et al., 2024).

**SHAP (SHapley Additive exPlanations):** Modelo unificado de atribución matemática basado en la teoría de juegos cooperativos, cuya función es cuantificar de forma algorítmica y aditiva el peso exacto que cada variable independiente de entrada transfiere sobre la predicción total del modelo (Lundberg & Lee, 2017).

**Sistema de Detección de Intrusiones (IDS):** Herramienta técnica —de software o hardware— que tiene por misión supervisar de manera continua los vectores de tráfico entrantes o salientes de una red corporativa para reconocer y advertir irregularidades sistémicas, firmas de ataques conocidos y violaciones de los protocolos de ciberseguridad (Figueroa Dextre & Cañihua Ccapa, 2024).

**Tráfico de Red:** Conglomerado de datos encapsulados que circulan mediante estándares y protocolos de internet. Se analiza a nivel estadístico extrayendo metadatos como la varianza de inter-llegada, direcciones IP, enrutamiento de puertos y densidad global de bytes.

---

## 2.6 Operacionalización de Variables

La operacionalización constituye el nexo metodológico que permite transitar desde las abstracciones teóricas hacia la medición empírica en el contexto de las PyMES de Juliaca. La variable independiente (VI) es el **Sistema Híbrido de Machine Learning con XAI**: modelo computacional basado en algoritmos de aprendizaje automático integrados con el marco de explicabilidad SHAP para clasificar anomalías en flujos de red y extraer la contribución matemática de las variables causales. Esta variable se estructura en tres dimensiones: rendimiento clasificatorio, explicabilidad matemática y eficiencia computacional; evaluadas mediante indicadores como la tasa de exactitud (Accuracy, %), la puntuación F1-Score (%), la consistencia de los valores SHAP según sus axiomas teóricos, el tiempo de inferencia en milisegundos y el tiempo de generación de explicaciones en segundos.

La variable dependiente (VD) es la **Comprensión y Utilidad de Alertas**: nivel de entendimiento y capacidad de acción inicial por parte de administradores de red no especializados frente a una alerta de seguridad semánticamente traducida por el sistema. Esta variable se organiza en tres dimensiones: claridad semántica, utilidad percibida bajo el modelo NEAT y capacidad accionable; evaluadas mediante el porcentaje de aciertos al identificar el tipo de ataque, el nivel de satisfacción en la interfaz medido mediante escala Likert, la tasa de elección correcta del playbook defensivo y el tiempo de reacción del usuario ante la alerta.

| Tipo de Variable | Nombre | Dimensiones | Indicadores Clave |
|---|---|---|---|
| **Variable Independiente (VI)** | Sistema Híbrido de ML con XAI | 1. Rendimiento Clasificatorio 2. Explicabilidad Matemática 3. Eficiencia Computacional | Accuracy (%), F1-Score (%), Consistencia SHAP (axiomas), Tiempo de inferencia (ms), Tiempo de generación de explicaciones (s) |
| **Variable Dependiente (VD)** | Comprensión y Utilidad de Alertas | 1. Claridad Semántica 2. Utilidad Percibida (NEAT) 3. Capacidad Accionable | % de aciertos en identificar el tipo de ataque, Satisfacción en interfaz (Likert), Tasa de elección correcta del playbook, Tiempo de reacción ante la alerta (s) |

### 2.6.1 Relación Causal entre Variables

El Sistema Híbrido de Machine Learning con XAI (VI) impacta de manera causal, positiva y directa sobre la Comprensión y Utilidad de Alertas para PyMES (VD). Este fenómeno se produce a través de un mecanismo de tres etapas encadenadas.

En la primera etapa, el algoritmo de clasificación —Random Forest o XGBoost— analiza las características estadísticas del tráfico de red en tiempo real, calculando la probabilidad de que un flujo determinado corresponda a un ataque conocido. Sin embargo, este resultado por sí solo es una sentencia opaca: el modelo emite un dictamen binario o probabilístico sin revelar su fundamento lógico, lo que lo hace estéril para un usuario no técnico.

En la segunda etapa, la superposición del framework SHAP sobre la capa de predicción transforma esta opacidad en transparencia cuantificable. Sustentado en la teoría de juegos cooperativos (Shapley, 1953; Lundberg & Lee, 2017), SHAP descompone matemáticamente la predicción en contribuciones individuales por variable —revelando, por ejemplo, que el parámetro `Bwd Packets/s` generó el 94% de la activación de alerta—. Este desglose causal convierte el dictamen abstracto en evidencia trazable.

En la tercera etapa, la integración con el marco NEAT (Reeder et al., 2011) somete esta evidencia a un proceso de traducción semántica: los pesos matemáticos son codificados en enunciados descriptivos comprensibles —por ejemplo, "Tráfico entrante anómalo detectado: posible ataque de denegación de servicio"— y en prescripciones operativas directas —playbooks— ejecutables por el operador sin conocimientos avanzados. Este proceso causal neutraliza la barrera técnica entre el sistema y el usuario, reduciendo el tiempo de reacción, incrementando la tasa de identificación correcta del ataque y disminuyendo la fatiga por alertas; fenómenos que han sido evidenciados previamente en los estudios de Gaspar et al. (2024), Hermosilla et al. (2025b) y Reeder et al. (2011).

---

## Referencias Bibliográficas

Alabbadi, A., & Bajaber, F. (2025). An Intrusion Detection System over the IoT Data Streams Using explainable Artificial Intelligence (XAI). *Sensors*, *25*(3), 847. https://doi.org/10.3390/s25030847

Alabdulatif, A. (2025). A Novel Ensemble of Deep Learning Approach for Cybersecurity Intrusion Detection with Explainable Artificial Intelligence. *Applied Sciences*, *15*(14), 7984. https://doi.org/10.3390/app15147984

Arreche, O., Guntur, T. R., Roberts, J. W., & Abdallah, M. (2024a). E-XAI: Evaluating Black-Box Explainable AI Frameworks for Network Intrusion Detection. *IEEE Access*, *12*, 23954–23988. https://doi.org/10.1109/ACCESS.2024.3365140

Arreche, O., Guntur, T., & Abdallah, M. (2024b). XAI-IDS: Toward Proposing an Explainable Artificial Intelligence Framework for Enhancing Network Intrusion Detection Systems. *Applied Sciences*, *14*(10), 4170. https://doi.org/10.3390/app14104170

Corea, P. M., Liu, Y., Wang, J., Niu, S., & Song, H. (2024). Explainable AI for Comparative Analysis of Intrusion Detection Models. En *2024 IEEE International Mediterranean Conference on Communications and Networking (MeditCom)*. https://doi.org/10.1109/MeditCom61057.2024.10621339

Fatema, K., Dey, S. K., Anannya, M., Khan, R. T., Rashid, M. M., Su, C., & Mazumder, R. (2025). Federated XAI IDS: An Explainable and Safeguarding Privacy Approach to Detect Intrusion Combining Federated Learning and SHAP. *Future Internet*, *17*(6), 234. https://doi.org/10.3390/fi17060234

Figueroa Dextre, B. S., & Cañihua Ccapa, J. (2024). *Sistema de intrusión de tráfico de red basado en Machine Learning para la protección de datos en la empresa, Lima, 2024* [Tesis de licenciatura, Universidad Tecnológica del Perú]. https://hdl.handle.net/20.500.12867/11959

Gaspar, D., Silva, P., & Silva, C. (2024). Explainable AI for Intrusion Detection Systems: LIME and SHAP Applicability on Multi-Layer Perceptron. *IEEE Access*, *12*, 30164–30175. https://doi.org/10.1109/ACCESS.2024.3368377

Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.

Hernandez Legua, A. F. (2025). *Modelo de ciberseguridad basado en Zero Trust con DLP para fortalecer la seguridad de Información sensible en el sector eléctrico* [Tesis de maestría, Universidad Nacional Mayor de San Marcos]. https://hdl.handle.net/20.500.12672/28948

Hermosilla, P., Berríos, S., & Allende-Cid, H. (2025a). Explainable AI for Forensic Analysis: A Comparative Study of SHAP and LIME in Intrusion Detection Models. *Applied Sciences*, *15*(13), 7329. https://doi.org/10.3390/app15137329

Hermosilla, P., Díaz, M., Berríos, S., & Allende-Cid, H. (2025b). Use of Explainable Artificial Intelligence for Analyzing and Explaining Intrusion Detection Systems. *Computers*, *14*(5), 160. https://doi.org/10.3390/computers14050160

Jameel, R., et al. (2025). Evaluating the Generalization Gaps of Intrusion Detection Systems Across DoS Attack Variants. *Journal of Cybersecurity and Privacy*.

Jiménez Alegría, L. C. (2016). *Implementación de un sistema de Seguridad (IDS/IPS) Open Source basado en Raspberry para Red del Ministerio Público Sede Puno* [Tesis de licenciatura, Universidad Católica de Santa María]. https://repositorio.ucsm.edu.pe/handle/20.500.12920/5898

Larriva-Novo, X., et al. (2024). Post-Hoc Categorization Based on Explainable AI and Reinforcement Learning for Improved Intrusion Detection. *Applied Sciences*.

Lundberg, S. M., & Lee, S.-I. (2017). A Unified Approach to Interpreting Model Predictions. *Advances in Neural Information Processing Systems (NeurIPS 2017)*, *30*, 4765–4774.

Manrique Huamaní, R. E., & Santiváñez Guarniz, C. A. (2021). *Estudio del rendimiento de sistemas de detección de intrusos (IDS) en redes SDN* [Trabajo de investigación de bachillerato, Pontificia Universidad Católica del Perú]. https://repositorio.pucp.edu.pe/index/handle/123456789/171542

Mia, M. S. R., Pritom, M. M. A., Islam, T., & Hasan, K. (2024). Visually Analyze SHAP Plots to Diagnose Misclassifications in ML-Based Intrusion Detection. En *2024 IEEE International Conference on Data Mining Workshops (ICDMW)*. https://doi.org/10.1109/ICDMW65004.2024.00088

Mitchell, T. M. (1997). *Machine Learning*. McGraw-Hill.

Nkoro, E. C., Njoku, J. N., Nwakanma, C. I., Lee, J.-M., & Kim, D.-S. (2024). Zero-Trust Marine Cyberdefense for IoT-Based Communications: An Explainable Approach. *Electronics*, *13*(2), 276. https://doi.org/10.3390/electronics13020276

Ore Huacles, J. P., & Donaire Arbieto, I. E. (2021). *Sistemas de control de supervisión y adquisición de datos para la deteccion de ciberataques en la industria minera* [Trabajo de investigación de bachillerato, Universidad Peruana de Ciencias Aplicadas]. http://hdl.handle.net/10757/656083

Reeder, R., Kowalczyk, E. C., & Shostack, A. (2011). Helping Engineers Design NEAT Security Warnings. *Proceedings of the 2011 Symposium on Usable Privacy and Security*.

Shapley, L. S. (1953). A value for n-person games. *Contributions to the Theory of Games*, *2*(28), 307–317.

Silva, M., Pinto, D., Vitorino, J., Gonçalves, J., Maia, E., & Praça, I. (2025). GeNIS: A modular dataset for network intrusion detection and classification. *Data in Brief*, *60*, 111487. https://doi.org/10.1016/j.dib.2025.111487

Taheri, R., Jafari, R., Gegov, A., Arabikhan, F., & Ichtev, A. (2025). Explainable AI for Federated Learning-Based Intrusion Detection Systems in Connected Vehicles. *Electronics*, *14*(22), 4508. https://doi.org/10.3390/electronics14224508

Torres Valle, L. A., & Abensur Rojas, Y. D. (2025). *Implementación de un IDS basado en Snort y técnicas de Machine Learning para redes perimetrales en colegios privados de Lima Metropolitana* [Tesis de licenciatura, Universidad Tecnológica del Perú]. https://hdl.handle.net/20.500.12867/11959

Wang, M., Zheng, K., Yang, Y., & Wang, X. (2020). An Explainable Machine Learning Framework for Intrusion Detection Systems. *IEEE Access*, *8*, 73127–73141. https://doi.org/10.1109/ACCESS.2020.2988359

Yauri Lozano, E. (2017). *SnorUNI: aplicación móvil para sistemas de detección y prevención de intrusiones basados en Snort* [Tesis de licenciatura, Universidad Nacional de Ingeniería]. http://cybertesis.uni.edu.pe

Zanabria Ticona, E. D. (2023). *Seguridad informática en la plataforma virtual del Vicerrectorado de Investigación de la Universidad Nacional del Altiplano de Puno - 2019* [Tesis de maestría, Universidad Nacional del Altiplano]. https://repositorio.unap.edu.pe/handle/20.500.14082/21081