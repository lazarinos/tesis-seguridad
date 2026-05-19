# Planteamiento del Problema

**Tema de investigación:**  
Detección de intrusiones de red con aprendizaje automático y técnicas de explicabilidad (XAI) para pequeñas y medianas empresas de Juliaca, Puno.

---

## 1. Contexto (¿Dónde ocurre?)

Juliaca es la ciudad más poblada de la región Puno y uno de los principales centros comerciales del altiplano peruano. Su dinamismo económico, oferta de servicios y capacidad de atracción regional favorecen la concentración de numerosas pequeñas y medianas empresas (PyMES) en rubros como comercio, transporte y servicios [@pdu_juliaca2016].

Estas empresas manejan cada vez más información digital: cobros por transferencia, sistemas de caja, correos y archivos compartidos en red. Esta necesidad de conectividad no es aislada, sino parte de un entorno nacional en el que la infraestructura digital continúa expandiéndose: al cierre de 2025, el Perú registró 214 856 conexiones de internet fijo en el segmento comercial, mientras que la fibra óptica alcanzó el 82.47% del total de conexiones fijas [@osiptel2025internet]. Pese a ello, muchas PyMES carecen de personal especializado en ciberseguridad y de herramientas de protección adecuadas. Mordor Intelligence reporta que las PyMES constituyen el segmento empresarial de mayor crecimiento en demanda de ciberseguridad en el Perú [@mordor2025peru].

A nivel nacional, Perú recibe más de un millón de ciberataques al año, por encima del promedio mundial per cápita [@mordor2025peru]. Además, Kaspersky reportó 123 intentos de ataque por malware por minuto durante los primeros ocho meses de 2022, ubicando al país entre los más atacados de Latinoamérica [@kaspersky2022latam]. En mayo de 2025, el grupo de ransomware Rhysida afirmó haber comprometido la plataforma digital del gobierno peruano `gob.pe` y exigió 5 bitcoin como rescate; el gobierno peruano negó la afectación del portal central y confirmó un incidente separado en el SAT de Piura [@mordor2025peru; @scmedia2025rhysida_peru].

---

## 2. Situación problemática (¿Qué está fallando?)

Muchas PyMES de Juliaca carecen de mecanismos de monitoreo que adviertan oportunamente sobre ataques o comportamientos anómalos en su red.

Las herramientas tradicionales de detección de intrusiones (IDS), como Snort o Suricata, comparan el tráfico de red con una base de reglas conocidas. Este enfoque es útil para amenazas previamente catalogadas, pero pierde eficacia frente a ataques nuevos, variantes no registradas o comportamientos anómalos no cubiertos por reglas [@xai_review2025]. Además, exige personal técnico especializado para configurar, ajustar y mantener dichas reglas, un recurso que la mayoría de las PyMES no puede costear [@latam_csec2024].

En el contexto académico local y regional, Coyla Jarita [@coyla2019juliaca_ids] implementó un IDS/IPS con Snort e ISO 27001 para el monitoreo perimetral de la red de la Universidad Peruana Unión -- Filial Juliaca. De forma complementaria, Jiménez Alegria [@jimenez2016puno_raspberry_ids] propuso un IDS/IPS open source basado en Raspberry para la red del Ministerio Público sede Puno. Estos antecedentes muestran que la detección de intrusiones ya ha sido considerada una necesidad técnica en la región, aunque desde enfoques tradicionales basados en reglas, herramientas open source y monitoreo perimetral.

Los enfoques modernos basados en aprendizaje automático, una rama de la inteligencia artificial, pueden mejorar la detección de ataques. No obstante, con frecuencia producen alertas opacas para usuarios no especializados: indican "ataque detectado", pero no explican qué variable del tráfico influyó en la decisión ni qué acción inicial conviene tomar. Esta falta de interpretabilidad limita su adopción en entornos reales [@xai_ids2024].

Como resultado, ante un ataque de denegación de servicio (DoS) o un intento de acceso no autorizado, el administrador del negocio podría no comprender lo ocurrido, reaccionar tarde y sufrir pérdidas económicas u operativas. El problema no es únicamente detectar el evento, sino traducir la alerta técnica en información comprensible y útil para una acción inicial por parte de usuarios sin formación especializada.

---

## 3. Vacío de conocimiento (¿Qué no se sabe aún?)

La literatura reciente sobre sistemas de detección de intrusiones con aprendizaje automático y explicabilidad ya ha demostrado que es posible combinar modelos de clasificación con técnicas como SHAP para interpretar sus predicciones. Sin embargo, la mayor parte de estos estudios se concentra en el rendimiento técnico del modelo, la comparación entre algoritmos o la interpretación de variables desde la perspectiva de investigadores y analistas especializados, más que en la comprensión práctica de las alertas por parte de usuarios no técnicos.

En ese marco, el dataset GeNIS [@genis2025; @genis_zenodo2025], publicado en 2025 y construido sobre escenarios de simulación avanzada en CyberRange, es uno de los conjuntos de datos más recientes y pertinentes para entrenar modelos de detección de intrusiones orientados a escenarios empresariales. Sin embargo, en investigación de IDS no es metodológicamente suficiente depender de un solo dataset, porque ello limita la comparación del desempeño y la discusión sobre la generalización del enfoque.

Por esa razón, además de GeNIS, resulta necesario considerar al menos un dataset de referencia ampliamente usado en la literatura. En esta investigación se adopta **UNSW-NB15** [@moustafa2015unswnb15; @unswnb15_dataset] como benchmark complementario para contrastar el comportamiento de los algoritmos y la estrategia de explicabilidad en un escenario clásico de IDS. Esta comparación se plantea a nivel de enfoque y familias de modelos, no como una validación directa del mismo modelo entrenado en GeNIS sobre UNSW-NB15, debido a las diferencias de estructura y características entre datasets.

A nivel peruano existen trabajos cercanos sobre IDS tradicional en PyMES, como la implementación de Snort open source para PyMES del Perú [@huamani2020snort_pymes] y el uso de Suricata como mecanismo de seguridad corporativa [@tineo2020suricata]. También se identificó una tesis reciente en Lima que desarrolla detección de intrusiones con aprendizaje automático usando CICIDS2017 [@figueroa2024ml_ids_lima]. Sin embargo, no se encontró una investigación en la región Puno que aborde de manera conjunta:

- aprendizaje automático aplicado a IDS;
- un dataset principal reciente como GeNIS;
- contraste complementario con un dataset de referencia;
- técnicas de explicabilidad como SHAP;
- traducción de las explicaciones del modelo a alertas comprensibles y accionables para usuarios no técnicos;
- e interfaz orientada a administradores de PyMES.

En consecuencia, el vacío no radica en demostrar nuevamente que SHAP puede aplicarse técnicamente a un IDS, sino en verificar empíricamente si las explicaciones del modelo pueden transformarse en alertas comprensibles y utilizadas por administradores de PyMES sin formación técnica para apoyar decisiones iniciales ante una alerta de seguridad, dentro de un contexto local como Juliaca.

---

## 4. Justificación (¿Por qué importa?)

Una alerta explicable ayudaría a que un administrador sin formación técnica avanzada comprenda el tipo de ataque detectado y tome decisiones iniciales. La técnica SHAP (SHapley Additive Explanations) permite descomponer la decisión del modelo según la contribución de cada variable del tráfico, lo que facilita la interpretación de sus predicciones [@gaspar2024shap]. En ese sentido, SHAP no se plantea como una novedad técnica en sí misma, sino como una herramienta para investigar si las explicaciones generadas por el modelo pueden traducirse en mensajes comprensibles, útiles y accionables en un entorno real de PyMES.

Esto es importante porque:

- Muchas PyMES no pueden pagar herramientas comerciales ni contratar especialistas: Perú enfrenta un déficit del 30% de profesionales certificados en ciberseguridad [@mordor2025peru].
- Un sistema de código abierto, entrenado con datos realistas y con una interfaz simple, podría apoyar la protección de negocios de Juliaca que hoy carecen de monitoreo especializado.
- El mercado de ciberseguridad en Perú está valorado en USD 170.22 millones en 2025 y crece a una tasa anual compuesta de 8.52%; sin embargo, el segmento de PyMES es el de mayor crecimiento (12.65% CAGR) y uno de los menos cubiertos [@mordor2025peru].
- Contribuye al área de ciberseguridad accesible en ciudades intermedias del Perú, donde la investigación aplicada sobre IDS con XAI aún es limitada.
- Permite evaluar no solo la precisión técnica del sistema, sino también la comprensibilidad y utilidad práctica de sus alertas para usuarios no técnicos.

---

## 5. Delimitación

La investigación se delimita al diseño y evaluación de un prototipo de detección de intrusiones orientado a pequeñas y medianas empresas de Juliaca, Puno, principalmente de los rubros de comercio, transporte y servicios, que utilicen infraestructura digital básica para sus operaciones, como acceso a internet, red local, sistemas de caja, correo electrónico o intercambio de archivos. El estudio se enfoca en eventos de tráfico de red representados en el dataset **GeNIS 2025** y contrastados con **UNSW-NB15** como benchmark complementario. Asimismo, la evaluación de comprensibilidad se realizará con una muestra intencional de entre **8 y 12 administradores o responsables operativos de PyMES**, con uso habitual de herramientas digitales y sin formación especializada en ciberseguridad. Los resultados de esta evaluación tendrán alcance exploratorio y no pretenden generalizar estadísticamente a todas las PyMES de Juliaca.

---

## 6. Preguntas de investigación (¿Qué queremos responder?)

**Pregunta general:**  
¿En qué medida un sistema de detección de intrusiones basado en aprendizaje automático e integrado con técnicas de explicabilidad (XAI), entrenado principalmente con el dataset GeNIS y contrastado con un dataset de referencia, puede generar alertas comprensibles, útiles y accionables para administradores no especializados de PyMES de Juliaca, Puno?

**Preguntas específicas:**

1. ¿Qué algoritmo de aprendizaje automático detecta mejor los ataques en GeNIS y muestra un comportamiento competitivo al contrastarse con el benchmark UNSW-NB15?
2. ¿Qué variables del tráfico explican con mayor peso las predicciones del modelo seleccionado mediante SHAP?
3. ¿Es posible construir un prototipo funcional con interfaz simple que presente dichas alertas de manera clara y opere sobre hardware convencional?
4. ¿En qué medida los administradores de PyMES pueden comprender las alertas emitidas por el prototipo y asociarlas con acciones iniciales básicas de respuesta?

---

## 7. Objetivos

**Objetivo general:**  
Desarrollar y evaluar un sistema de detección de intrusiones de red basado en aprendizaje automático e integrado con técnicas de explicabilidad (XAI), entrenado principalmente con el dataset GeNIS 2025, contrastado con un dataset de referencia y orientado a la generación de alertas comprensibles para administradores de PyMES de Juliaca, Puno.

**Objetivos específicos:**

1. Analizar y preprocesar el dataset GeNIS para identificar las características más relevantes en la detección de ataques.
2. Incorporar el dataset **UNSW-NB15** como referencia complementaria para contrastar el comportamiento de los algoritmos y del enfoque de explicabilidad.
3. Comparar al menos tres algoritmos de aprendizaje automático y seleccionar el de mejor desempeño y mayor consistencia entre datasets.
4. Diseñar una estrategia de traducción de las explicaciones generadas por SHAP a alertas claras, comprensibles y accionables para usuarios no técnicos.
5. Implementar un prototipo con interfaz simple que muestre las alertas y sus explicaciones de manera clara.
6. Evaluar la comprensibilidad, utilidad percibida y capacidad de acción inicial asociada a las alertas del prototipo en una muestra intencional de 8 a 12 administradores o responsables operativos de PyMES sin formación especializada en ciberseguridad.

---

## Datasets propuestos

**Nombre:** GeNIS — GECAD Network Intrusion Scenarios [@genis2025; @genis_zenodo2025]  
**Publicado por:** Politécnico de Oporto, Portugal (2025)  
**Descarga:** [https://zenodo.org/records/14919237](https://zenodo.org/records/14919237)  
**Licencia:** Creative Commons BY 4.0 (libre para investigación)

**Rol metodológico:** dataset principal.

**¿Por qué este dataset principal?**

- Es reciente y de acceso abierto (publicado en Zenodo el 24 de febrero de 2025).
- Fue diseñado para representar redes empresariales vulnerables similares a las de PyMES, simuladas en infraestructura CyberRange.
- Contiene tráfico benigno y ataques clasificados principalmente en DoS, Brute Force y Reconnaissance, con más de 2.8 millones de flujos etiquetados.
- Incluye flujos preprocesados en ventanas de 5, 10, 30 y 60 segundos. Para este estudio se usará la ventana de 30 segundos por ofrecer un equilibrio entre detalle del tráfico y costo computacional.
- Sus etiquetas permiten trabajar la detección binaria (`BinaryLabel`), la categoría general del evento (`CategoryLabel`) y, de forma complementaria, el subtipo de ataque (`SubCategoryLabel`).

**Archivos a utilizar:**

| Archivo | Uso | Tamaño |
|---|---|---|
| `genis-30-sec-train.csv` | Entrenamiento del modelo | 256 MB aprox. |
| `genis-30-sec-test.csv` | Evaluación del modelo | 64 MB aprox. |

### Dataset complementario de validación

**UNSW-NB15** [@moustafa2015unswnb15; @unswnb15_dataset]

- Se considera como benchmark de referencia por su amplia adopción en la literatura.
- Permite contrastar el comportamiento de los algoritmos en un dataset clásico con nueve tipos de ataques y 49 características.
- Su inclusión fortalece la solidez metodológica de la tesis al evitar depender de un único escenario experimental.

### Estrategia de uso

- **GeNIS 2025** se empleará como dataset principal de entrenamiento, selección de variables y construcción del prototipo.
- **UNSW-NB15** se empleará como benchmark complementario para contrastar el comportamiento de los algoritmos y la estrategia de explicabilidad.

---

*Juliaca, Puno — Mayo 2026*
