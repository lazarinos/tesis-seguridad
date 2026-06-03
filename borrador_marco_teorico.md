# Capítulo II: Marco Teórico (Primer Borrador)

Este documento presenta el primer borrador desarrollado de forma científica y lógica de las bases teóricas de la investigación: *"Detección de intrusiones de red con aprendizaje automático y técnicas de explicabilidad (XAI) para pequeñas y medianas empresas de Juliaca, Puno"*.

---

## 2.1. Ciberseguridad Aplicada y Sistemas de Monitoreo en PyMES

### 2.1.1. Gestión de Seguridad de la Información en Entornos de Recursos Limitados
La ciberseguridad en pequeñas y medianas empresas (PyMES) se enfrenta a restricciones severas debido a la falta de presupuesto, la ausencia de personal especializado y la precariedad de su infraestructura digital. En el ámbito de la región Puno, estas vulnerabilidades se acentúan debido a las características comerciales y de conectividad de la zona. 

La auditoría y evaluación de riesgos bajo estándares tradicionales como la norma ISO 17799 permiten identificar y priorizar las brechas críticas de seguridad en infraestructuras locales peruanas, tal como demuestran Zanabria y Tito (2019) [@zanabria2019seguridad_unap] al diagnosticar niveles de riesgo altos en entornos virtuales institucionales del altiplano. De igual manera, ante la escasez de recursos informáticos en la zona, Jiménez (2016) [@jimenez2016puno_raspberry_ids] sustenta la viabilidad de implementar sistemas de seguridad perimetral de bajo costo aprovechando hardware embebido de recursos limitados (como placas Raspberry Pi) configurados con motores de código abierto, sentando las bases para el monitoreo de flujos locales sin inversiones prohibitivas.

### 2.1.2. Sistemas de Detección de Intrusiones (IDS/IPS) y Ciberseguridad Moderna
Los sistemas de detección de intrusiones (IDS) se clasifican en sistemas basados en host (HIDS) y basados en red (NIDS). El NIDS tradicional opera bajo un enfoque pasivo fundamentado en firmas de ataques previamente conocidas (motores como Snort o Suricata), cotejando firmas binarias de paquetes de red en tiempo real. Aunque efectivo para vulnerabilidades documentadas, este modelo de firmas estáticas es ineficaz ante ataques de día cero (zero-day) o variantes dinámicas de amenazas. 

Para resolver este límite técnico, la ciberseguridad moderna se orienta hacia la detección de anomalías mediante inteligencia artificial, combinando motores open source con clasificadores dinámicos. En el ámbito peruano, Torres y Abensur (2025) [@torres2025snort_ml_utp] proponen un IDS híbrido que integra las firmas deterministas de Snort con clasificadores supervisados de machine learning para capturar anomalías no catalogadas, reduciendo la tasa de falsos negativos. Asimismo, en entornos de alta velocidad y redes programables, Manrique y Santiváñez (2021) [@manrique2021ids_sdn_pucp] demuestran la necesidad de evaluar el rendimiento del rendimiento de los IDS tradicionales (latencia, throughput y pérdida de paquetes) bajo arquitecturas de redes definidas por software (SDN) para mitigar vectores complejos de denegación de servicio (DoS).

### 2.1.3. Arquitectura Zero Trust y Prevención de Fuga de Datos (DLP)
Frente a la debilidad del perímetro tradicional de red, la filosofía de diseño Zero Trust ("nunca confiar, siempre verificar") postula que cualquier flujo de tráfico, interno o externo, es potencialmente hostil y requiere autenticación y validación continua. Hernandez (2025) [@hernandez2025zerotrust_unmsm] desarrolla y valida un modelo de ciberseguridad de segmentación Zero Trust integrado con técnicas de prevención de fuga de datos (DLP) en redes industriales y eléctricas de alta sensibilidad en el Perú, demostrando mediante coeficientes estadísticos robustos que el control granular de flujos disminuye drásticamente el riesgo de filtraciones y accesos no autorizados, estableciendo un marco teórico para el diseño defensivo en organizaciones críticas.

---

## 2.2. Modelos de Machine Learning aplicados a IDS de Red (NIDS)

### 2.2.1. Clasificadores Supervisados de Tráfico Anómalo
El machine learning permite a los NIDS aprender patrones de comportamiento anómalos a partir de variables estadísticas de flujos de red. Los clasificadores más robustos y adoptados en la literatura para el análisis de flujos son:
1.  **Random Forest (RF):** Clasificador de ensamble basado en múltiples árboles de decisión que reduce el sobreajuste y presenta gran eficiencia en flujos de red estructurados.
2.  **XGBoost:** Algoritmo de gradient boosting tabular de alto rendimiento optimizado para velocidad y escala.
3.  **Redes Neuronales Multicapa (MLP):** Modelos de aprendizaje profundo capaces de capturar interacciones no lineales de variables de red complejas.

En estudios experimentales peruanos, Figueroa y Cañihua (2024) [@figueroa2024ml_ids_lima] modelan clasificadores de Random Forest y Regresión Logística para el tráfico de empresas peruanas, demostrando que Random Forest alcanza exactitudes superiores al 95%, consolidando su viabilidad práctica. Por su parte, Ore y Donaire (2021) [@ore2021scada_upc] aplican con éxito clasificadores de árboles de decisión en la telemetría continua de plantas mineras industriales SCADA para detectar DoS y ataques de inyección de comandos en variables físicas continuas. La literatura global, incluyendo a Corea et al. (2024) [@corea2024comparative], coincide en que la reducción previa de características críticas mediante análisis de sensibilidad optimiza de forma significativa el costo computacional de los modelos, facilitando su despliegue en hardware de bajos recursos.

### 2.2.2. Comparación Metodológica de Datasets: GeNIS (2025) y CICIDS2017
El entrenamiento y validación de modelos requiere el uso de conjuntos de datos representativos de amenazas modernas. Esta investigación se fundamenta en el análisis de dos conjuntos de datos:

*   **GeNIS (2025) (Dataset Principal):** Publicado por Silva et al. (2025) [@genis2025], GeNIS es un conjunto de datos modular y de vanguardia generado en un entorno CyberRange controlado de simulación empresarial. Contiene escenarios realistas de tráfico benigno combinado con vectores de ataque clasificados (fuerza bruta, DoS y escaneos de red), estructurado de forma modular para evitar desbalances extremos y modelar con precisión redes organizacionales contemporáneas.
*   **CICIDS2017 (Benchmark de Contraste):** Generado por el Canadian Institute for Cybersecurity [@sharafaldin2018cicids2017], es el estándar clásico en la literatura de IDS. Registra tráfico de flujos de red en formato bidireccional (con más de 80 atributos estadísticos) y abarca ataques avanzados de DoS, Web attacks e infiltración. 

Metodológicamente, se utiliza CICIDS2017 como benchmark para contrastar la estabilidad de los algoritmos y la interpretabilidad de las explicaciones ante un dataset clásico de alta dimensionalidad. Como advierte Jameel et al. (2025) [@jcp_generalization_gaps_dos_2025], la generalización de los IDS decae drásticamente al enfrentarse a variantes DoS no entrenadas en el conjunto principal, lo que justifica la validación multidataset para evitar sesgos de sobreajuste y brechas de generalización en redes de PyMES.

---

## 2.3. Inteligencia Artificial Explicable (XAI) en Sistemas de Detección

### 2.3.1. Teoría de Juegos y Explicaciones Aditivas de Shapley (SHAP)
Los modelos de machine learning para detección de intrusos actúan como "cajas negras", dificultando que un administrador entienda la lógica de una alerta. Para resolver esta opacidad, Lundberg y Lee (2017) [@lundberg2017shap] propusieron el framework **SHAP (SHapley Additive exPlanations)**, basado en la teoría de juegos cooperativos de Shapley (1953). 

En este contexto, las variables del tráfico de red (atributos del flujo) se consideran "jugadores" en una coalición, y la predicción del modelo de que el flujo es malicioso es la "ganancia" del juego. Los valores SHAP (valores de Shapley) representan la contribución marginal de cada característica al resultado de la predicción, calculados como:

$$\phi_i(x) = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} \left[ f_x(S \cup \{i\}) - f_x(S) \right]$$

Donde:
*   $F$ es el conjunto completo de características.
*   $S$ es una subcoalición de características que no incluye a la característica de interés $i$.
*   $f_x(S)$ es la expectativa de la predicción del modelo condicionada a las características del subconjunto $S$.
*   $|F|!$ representa las posibles permutaciones de los atributos.

SHAP destaca en la literatura por satisfacer tres propiedades fundamentales que garantizan explicaciones matemáticamente coherentes y estables:
1.  **Eficiencia (Local Accuracy):** La suma de las contribuciones atribuidas a cada variable coincide con la diferencia entre la predicción local del flujo $f(x)$ y la expectativa del modelo $E[f(x)]$.
2.  **Simetría:** Si dos atributos de red contribuyen de forma idéntica a todas las posibles coaliciones del modelo, sus valores SHAP asignados son exactamente iguales.
3.  **Consistencia (Monotonicity):** Si un modelo cambia de tal manera que la contribución marginal de un atributo de red aumenta o permanece igual para todas las coaliciones, el valor SHAP de ese atributo no puede disminuir.

La estabilidad y robustez de SHAP global y local permite tanto auditar el comportamiento lógico del IDS (Gaspar et al., 2024 [@gaspar2024shap]) como identificar atributos dominantes para detectar e interpretar alertas en entornos reales (Arreche et al., 2024 [@arreche2024exai]).

### 2.3.2. Explicaciones Locales Subrogadas Interpretables (LIME)
Propuesto por Ribeiro, Singh y Guestrin (2016) [@ribeiro2016lime], **LIME** aproxima las predicciones de cualquier modelo complejo localmente alrededor de una instancia de prueba mediante la perturbación de los datos y el entrenamiento de un modelo interpretable subrogado (como una regresión lineal ponderada). LIME minimiza una función de pérdida que balancea la fidelidad local con la complejidad del modelo explicador:

$$\xi(x) = \arg\min_{g \in G} L(f, g, \pi_x) + \Omega(g)$$

Donde:
*   $f$ es el modelo de caja negra original.
*   $g$ es el modelo localmente interpreteble (regresión lineal).
*   $\pi_x$ es la medida de proximidad de las instancias perturbadas respecto a la instancia original $x$.
*   $\Omega(g)$ representa la penalización por complejidad del modelo explicador.

Aunque LIME destaca por su velocidad de procesamiento local, carece de la consistencia axiomática de SHAP. En auditorías de ciberseguridad forense, Hermosilla et al. (2025) [@hermosilla2025xai_forensics] demuestran que las explicaciones de LIME varían levemente ante perturbaciones menores de la misma entrada, mientras que SHAP mantiene la estabilidad matemática y la aditividad de Shapley, siendo este último preferible para la justificación de evidencias en incidentes de red.

---

## 2.4. Usabilidad e Interfaces de Alertas Comprensibles (Sec-UX)

### 2.4.1. Framework NEAT y Prevención de la Fatiga por Alertas
La efectividad de un IDS en entornos reales depende directamente de la usabilidad de su interfaz de respuesta. En las PyMES, los administradores suelen sufrir de habituación o "ceguera de alertas" (warning blindness) debido al exceso de alertas técnicas falsas, desactivando eventualmente los sistemas de seguridad. 

Para resolver este factor humano, Reeder, Kowalczyk y Shostack (2011) [@reeder2011neat] proponen el framework **NEAT (Necessary, Explained, Actionable, Tested)** para el diseño usable de notificaciones y advertencias de seguridad:
*   **Necessary (Necesaria):** La alerta solo debe interrumpir al usuario si el riesgo es real e inminente, reduciendo el ruido de falsos positivos.
*   **Explained (Explicada):** El peligro debe describirse de forma clara y libre de tecnicismos complejos, explicando la lógica de la alerta.
*   **Actionable (Accionable):** La interfaz debe proporcionar una recomendación de acción inicial explícita y ejecutable por el usuario (playbook simplificado).
*   **Tested (Testeada):** Las alertas deben ser validadas perceptualmente con usuarios reales del contexto objetivo para medir la comprensión.

El desarrollo de interfaces dinámicas, como la mostrada por Alabdulatif (2025) [@ensemble_dl_ids_xai_appsci_2025], integra de forma interactiva las atribuciones de SHAP para proveer representaciones visuales comprensibles en tiempo real.

### 2.4.2. Traducción Semántica de Alertas y Playbooks para PyMES en Juliaca, Puno
La traducción semántica consiste en mapear variables técnicas oscuras (por ejemplo: `Flow Duration`, `Destination Port 80`, `Fwd Packet Length Std`) evaluadas por SHAP a lenguaje natural inteligible y playbooks accionables para PyMES de Juliaca:

| Clasificación del Ataque | Atributos de Red Dominantes (SHAP) | Traducción en Lenguaje Natural | Recomendación / Playbook Accionable |
|---|---|---|---|
| **DoS (Denegación de Servicio)** | `Bwd Packets/s` $\uparrow$, `Flow IAT Min` $\downarrow$ | Intento de saturación del canal de red por el envío masivo de paquetes desde una dirección externa. | **Acción recomendada:** Aislar el host afectado de la red local y bloquear la dirección IP de origen en el router. |
| **Port Scan (Escaneo de Puertos)** | `Destination Port` variable, `Flow Duration` $\downarrow$ | Escaneo automático de puertos abiertos para buscar vulnerabilidades en los equipos de la PyME. | **Acción recomendada:** Deshabilitar los puertos no esenciales detectados y activar la protección perimetral del firewall. |
| **Brute Force (Fuerza Bruta)** | `Fwd Packet Length Std` $\downarrow$, `Protocol` | Intento repetitivo de adivinar contraseñas en servidores internos o sistemas de administración. | **Acción recomendada:** Bloquear temporalmente la cuenta de usuario atacada y forzar el uso de autenticación de doble factor (2FA). |

Este enfoque Sec-UX traduce métricas matemáticas de inteligencia artificial en toma de decisiones inmediatas para usuarios no técnicos de Juliaca, reduciendo la ventana de exposición a incidentes sin requerir la contratación permanente de un analista experto.
