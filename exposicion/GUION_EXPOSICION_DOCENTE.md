# GUION MAESTRO DE EXPOSICIÓN PARA SEMINARIO DE TESIS II

## EVALUACIÓN DE AVANCE Y RESULTADOS PRELIMINARES

- **Curso:** Seminario de Tesis II (2026-II)  
- **Docente:** Mg. Liz Huancapaza Hilasaca  
- **Tesista / Expositor:** Fernando Ccolla Lazarinos  
- **Título de la Tesis:** *Detección de intrusiones de red con aprendizaje automático y técnicas de explicabilidad (XAI) para pequeñas y medianas empresas de Juliaca, Puno*  
- **Tiempo estimado de exposición:** 10 a 12 minutos (+ ronda de preguntas)  
- **Estrategia pedagógica:** Estructura alineada al 100% con la Rúbrica Oficial de Evaluación (Puntaje Máximo Esperado: 10/10).

---

## MAPA DE NAVEGACIÓN Y RÚBRICA DE EVALUACIÓN

| Criterio de la Docente | Puntos | Secciones del Guión | Estrategia de Blindaje |
|---|:---:|---|---|
| **1. Presentación** | **0 – 2** | Diapositivas 1 y 2 | Declaración nítida del problema real, Objetivos (OG, OE1–OE4), porcentaje global de avance y orden lógico impecable. |
| **2. Protocolo / Metodología** | **0 – 3** | Diapositivas 3, 4 y 5 | Explicación del flujo experimental V2, datasets reales (GeNIS 2025 y CICIDS2017), control de fuga de datos, validación de instrumentos por expertos y etapas del piloto. |
| **3. Evidencias** | **0 – 2** | Diapositiva 4 y demostración | Exhibición de hashes criptográficos SHA-256/MD5, logs congelados, `environment_id`, hardware profile y matriz de trazabilidad. |
| **4. Resultados** | **0 – 2** | Diapositivas 6, 7, 8 y 9 | Métricas reales vinculadas a objetivos: F1-macro (0.9992), latencia (0.0024 ms), ranking SHAP top-10, prototipo Flask y tasas de acierto n/N con pymes de Juliaca. |
| **5. Análisis y Ajustes** | **0 – 1** | Diapositiva 10 y 11 | Reconocimiento explícito de dificultades (desbalance 1:29, latencia en MLP, sesgo en port scan), interpretación no sobregeneralizada y plan inmediato. |

---

## GUION PASO A PASO: DIAPOSITIVA POR DIAPOSITIVA

---

### DIAPOSITIVA 1: PORTADA Y PRESENTACIÓN FORMAL
- **Tiempo sugerido:** 0:00 – 0:45 min (45 segundos)
- **Criterio evaluado:** Presentación (Claridad y organización)
- **Contenido visual proyectado:**
  - Título oficial de la tesis.
  - Nombre del tesista: Fernando Ccolla Lazarinos.
  - Docente del curso: Mg. Liz Huancapaza Hilasaca.
  - Versión formal: Protocolo Experimental V2 (Fecha: Octubre 2026).
  - Línea de investigación: Ciberseguridad, Machine Learning aplicado y XAI.

#### Palabras del expositor:
> *"Buenos días estimada docente Mg. Liz Huancapaza Hilasaca y presentes. Mi nombre es Fernando Ccolla Lazarinos y el día de hoy vengo a presentar el avance experimental, los resultados preliminares y las evidencias técnicas de mi proyecto de tesis titulado: **'Detección de intrusiones de red con aprendizaje automático y técnicas de explicabilidad (XAI) para pequeñas y medianas empresas de Juliaca, Puno'**.*
> 
> *Esta sustentación está articulada estrictamente bajo el **Protocolo Experimental Versión 2**, garantizando total trazabilidad, reproducibilidad computacional y datos reales obtenidos de nuestra infraestructura de laboratorio."*

---

### DIAPOSITIVA 2: PLANTEAMIENTO, OBJETIVOS Y ESTADO DE AVANCE GLOBAL
- **Tiempo sugerido:** 0:45 – 2:00 min (1 minuto 15 segundos)
- **Criterio evaluado:** Presentación (Claridad del objetivo y avance)
- **Contenido visual proyectado:**
  - Problema central: La brecha de ciberseguridad en pymes de Juliaca (alertas complejas, sin personal especializado de SOC).
  - Objetivo General y los 4 Objetivos Específicos (OE1 a OE4).
  - Semáforo / Barra de Avance Cuantitativo del proyecto: **85% completado**.

#### Palabras del expositor:
> *"Para situarnos en el contexto: en Juliaca, las pymes comerciales, de servicios y textiles operan hoy interconectadas a Internet, pero carecen de áreas dedicadas de ciberseguridad o centros de operaciones de red (SOC). Las herramientas IDS comerciales emiten alertas crudas e incomprensibles para un administrador general de negocio.*
> 
> *Frente a este problema, nuestro **Objetivo General** es desarrollar y evaluar un sistema de detección de intrusiones de red basado en Machine Learning integrado con explicabilidad SHAP —usando **GeNIS 2025** como conjunto principal y **CICIDS2017** como contraste independiente— orientando sus salidas a alertas comprensibles y playbooks accionables para administradores de pymes.*
> 
> *Para lograrlo, definimos 4 Objetivos Específicos:
> 1. **OE1:** Comparar Random Forest, XGBoost y MLP bajo un mismo esquema de F1-macro.
> 2. **OE2:** Identificar las variables dominantes mediante valores SHAP y homologar conceptos de red.
> 3. **OE3:** Implementar el prototipo interactivo en Flask que traduzca SHAP en lenguaje operativo.
> 4. **OE4:** Evaluar la usabilidad y comprensión en una muestra intencional de administradores de pymes de Juliaca.
> 
> *Al día de hoy, el proyecto registra un **avance cuantitativo superior al 85%**: los modelos están entrenados y evaluados con datos reales, la explicabilidad calculada, el prototipo funcional y la primera fase de evaluación con usuarios en Juliaca completada exitosamente."*

---

### DIAPOSITIVA 3: PROTOCOLO EXPERIMENTAL Y PROCEDIMIENTO EJECUTADO
- **Tiempo sugerido:** 2:00 – 3:30 min (1 minuto 30 segundos)
- **Criterio evaluado:** Protocolo / Metodología (Procedimiento ejecutado y etapas)
- **Contenido visual proyectado:**
  - Diagrama de flujo del Protocolo V2:
    `Fuentes Oficiales` ➔ `Inventario Hashes` ➔ `Auditoría` ➔ `Partición Aislada` ➔ `Pipeline sin Fuga` ➔ `Comparación CV` ➔ `Test Final` ➔ `SHAP` ➔ `Prototipo Flask` ➔ `Piloto Expertos/Usuarios` ➔ `Evaluación Usabilidad`.
  - Matriz de Trazabilidad Técnica (actividades T01 a T20).

#### Palabras del expositor:
> *"Entrando al **Protocolo y Metodología**: la investigación no se basó en ejecuciones improvisadas, sino en un diseño experimental riguroso, formalizado en nuestro Protocolo V2 y en la Matriz de Trazabilidad Técnica con 20 actividades controladas (T01 a T20).*
> 
> *El procedimiento ejecutado sigue una cadena metodológica estricta:
> Primero, adquisición desde repositorios oficiales y congelamiento de hashes criptográficos.
> Segundo, auditoría de calidad de datos y detección de desbalances.
> Tercero, homologación canónica de variables antes de cualquier cálculo cruzado.
> Cuarto, partición estratificada con aislamiento absoluto del conjunto de prueba.
> Quinto, construcción de un pipeline anti-fuga (anti-leakage) donde el filtrado de varianza, correlación y escalado se ajustan únicamente con datos de entrenamiento.
> Sexto, optimización por validación cruzada estratificada de 5 pliegues bajo la métrica F1-macro.
> Y finalmente, despliegue del prototipo, validación del instrumento con juicio de expertos y prueba piloto."*

---

### DIAPOSITIVA 4: DATOS REALES Y EVIDENCIAS DE INTEGRIDAD CRIPTOGRÁFICA
- **Tiempo sugerido:** 3:30 – 4:45 min (1 minuto 15 segundos)
- **Criterio evaluado:** Metodología y Evidencias (Datos reales y verificación)
- **Contenido visual proyectado:**
  - Tabla de Datasets con Hashes SHA-256 y MD5 verificados.
  - GeNIS 2025: 607,933 flujos (Train: 486,346; Test: 121,587). DOI oficial Zenodo: 10.5281/zenodo.14919237.
  - CICIDS2017: 2,830,743 flujos (8 archivos CSV). Fuente oficial UNB.
  - Gráfico de Desbalance de Clases: DoS (87.1%), Benigno (5.3%), Reconocimiento (4.6%), Fuerza Bruta (3.0%).
  - Captura del Entorno: Perfil de Hardware `hardware_profile.txt` (Intel Core 6 núcleos físicos / 12 lógicos, Windows 10, Python 3.11.9).

#### Palabras del expositor:
> *"Pasando a las **Evidencias y Datos Reales**: aquí no hay datos simulados ni estimaciones teóricas. Contamos con los archivos completos en disco.*
> 
> *Para el dataset principal, **GeNIS 2025**, descargamos desde Zenodo las particiones oficiales de 30 segundos: `genis-30-sec-train.csv` con 486,346 flujos y `genis-30-sec-test.csv` con 121,587 flujos, totalizando **607,933 flujos de red**. Ambos archivos fueron auditados con sus hashes criptográficos MD5 y SHA-256 registrados en `dataset_files_hashes.csv`.*
> 
> *Para el contraste independiente, auditamos los 8 archivos de **CICIDS2017** con más de **2.83 millones de flujos**.*
> 
> *En la auditoría identificamos un hallazgo crítico: un severo desbalance de clases de **1 a 29.36** en GeNIS, donde el tráfico DoS acapara el 87% y la fuerza bruta apenas el 3%. Esto respaldó técnicamente nuestra decisión P01: **la métrica de selección debe ser F1-macro**, ya que una métrica como Accuracy daría un falso 87% de efectividad incluso si el modelo fallara en detectar todos los demás ataques.*
> 
> *Toda ejecución está sellada bajo el identificador de entorno `ENV_001`, ejecutado en un procesador Intel Core de 6 núcleos físicos y 12 hilos lógicos con Python 3.11.9, garantizando mediciones temporales válidas."*

---

### DIAPOSITIVA 5: INSTRUMENTOS, JUICIO DE EXPERTOS Y ETAPAS DEL PILOTO
- **Tiempo sugerido:** 4:45 – 6:00 min (1 minuto 15 segundos)
- **Criterio evaluado:** Metodología (Instrumentos y etapas del piloto)
- **Contenido visual proyectado:**
  - Panel de 3 Jueces Expertos: Ciberseguridad (UNA Puno), Ingeniero de SOC (Telecomunicaciones) y Metodólogo. Coeficiente V de Aiken = **0.98**.
  - Etapa del Piloto con 2 usuarios: Dificultades iniciales detectadas y ajustes realizados.
  - Matriz de Homologación de Variables (`feature_mapping.csv`): 16 conceptos canónicos (duración, tasas, tamaños de segmento, ventanas TCP).

#### Palabras del expositor:
> *"Respecto a los **Instrumentos y el Piloto**: para evaluar el componente de usabilidad en pymes no improvisamos preguntas. Diseñamos un instrumento estructurado que evalúa tres dimensiones: comprensión del incidente, selección del playbook correcto y tiempos de reacción, además de una escala Likert de 4 factores (Claridad, Utilidad, Confianza y Adopción).*
> 
> *Este instrumento fue sometido a **Juicio de 3 Expertos**: un especialista en seguridad de redes de UNA Puno, un ingeniero de operaciones de SOC y un metodólogo de investigación. El coeficiente de validez de contenido **V de Aiken alcanzó 0.98**, confirmando una pertinencia y coherencia excelente.*
> 
> *Siguiendo el protocolo, ejecutamos una **prueba piloto previa con 2 usuarios** encargados de negocios. Este piloto fue fundamental porque reveló que los usuarios se desconcertaban con nombres técnicos como 'DstWin' o 'sMeanPktSz'. En base a ello, ajustamos el prototipo para traducir esos valores a lenguaje cotidiano como 'Paquetes anormalmente pesados' o 'Ventana de tráfico saturada', e incorporamos un cronómetro milimétrico en el backend de Flask para capturar los tiempos de reacción reales."*

---

### DIAPOSITIVA 6: RESULTADOS OE1 - COMPARACIÓN DE ALGORITMOS (RF, XGBOOST, MLP)
- **Tiempo sugerido:** 6:00 – 7:30 min (1 minuto 30 segundos)
- **Criterio evaluado:** Resultados (Resultados definitivos vinculados a OE1)
- **Contenido visual proyectado:**
  - Tabla de Validación Cruzada (5-fold CV sobre Train Oficial de 486,346 flujos):
    - Random Forest: F1-Macro = 0.999973 +- 0.000054 | DE = 0.000054.
    - XGBoost: F1-Macro = 0.999957 +- 0.000050 | DE = 0.000050 (**SELECCIONADO POR MENOR DE**).
    - MLP: F1-Macro = 0.999648 +- 0.000186.
  - Aplicación de la Regla de Selección Normativa del Protocolo V2 (Sección 3.10):
    - Diferencia F1 entre RF y XGBoost: 0.000016 (<= 0.005, empate estadístico).
    - Desempate por menor desviación estándar: XGBoost (0.000050) vs Random Forest (0.000054). Decisión congelada en `selected_model_decision.json`.
  - Evaluación Ciega sobre Test Oficial Sellado (121,587 flujos — 5 Semillas):
    - XGBoost: F1-Macro = **0.999947 +- 0.000022** | Exactitud = **0.999990 +- 0.000003**.
  - Matriz de Confusión Oficial en Test (XGBoost S42): 121,586 aciertos de 121,587 flujos (99.9992% de exactitud; 1 solo error en 121,587 registros).
  - Trazabilidad y Latencia H3:
    - Inferencia media individual: **2.6865 ms/flujo** (Percentil 95: 3.80 ms; P99: 4.78 ms).
    - Cumplimiento normativo H3 (< 500 ms): **186.1 veces más rápido que el umbral máximo**.

#### Palabras del expositor:
> *"Ingresamos a los **Resultados Oficiales y Definitivos del Objetivo Específico 1**: la comparación rigurosa entre Random Forest, XGBoost y el Perceptrón Multicapa (MLP) ejecutada conforme al Protocolo V2.*
> 
> *En la validación cruzada estratificada sobre los 486,346 flujos de entrenamiento, tanto Random Forest (0.999973) como XGBoost (0.999957) alcanzaron niveles de F1-macro extraordinarios. Al ser la diferencia de apenas **0.000016**, se configuró un empate estadístico según la Sección 3.10 de nuestro protocolo.*
> 
> *Aplicando estrictamente la regla de desempate por menor dispersión de fold, **XGBoost resultó seleccionado como el modelo ganador**, con una desviación estándar menor (**0.000050** frente a 0.000054 de Random Forest), garantizando mayor robustez general. Esta decisión se congeló formalmente en disco antes de desbloquear el test.*
> 
> *Al abrir el conjunto de prueba oficial de **121,587 flujos ciegos**, evaluamos a XGBoost sobre 5 semillas distintas para garantizar reproducibilidad total, obteniendo un **F1-macro promedio de 0.999947** y una **exactitud de 0.999990**.*
> 
> *La matriz de confusión en test confirma que de los 121,587 registros de prueba, **121,586 fueron clasificados con precisión milimétrica**, cometiendo un único falso positivo en Reconocimiento.*
> 
> *Asimismo, medimos la latencia individual flujo a flujo registrada en el CSV de predicciones y realizamos el benchmark formal H3: con un tiempo de **2.68 milisegundos por flujo**, el sistema es **186 veces más veloz que el límite normativo de 500 ms**, confirmando categóricamente la **Hipótesis H1 y la Hipótesis H3**."*

---

### DIAPOSITIVA 7: RESULTADOS OE2 - EXPLICABILIDAD SHAP GLOBAL, LOCAL Y CONTRASTE CRUZADO
- **Tiempo sugerido:** 7:30 – 8:45 min (1 minuto 15 segundos)
- **Criterio evaluado:** Resultados (Resultados vinculados a OE2 y contrastación H2)
- **Contenido visual proyectado:**
  - Top 5 Características SHAP Globales (`TreeExplainer` sobre XGBoost):
    1. `Sdaddr` (2.5372, 31.9% acum.): Concentración de tráfico IP origen.
    2. `sHops` (1.2857, 48.0% acum.): Saltos de red y enrutamiento perimetral.
    3. `DstWin` (0.5573, 55.0% acum.): Tamaño de ventana TCP destino.
    4. `AckDat` (0.2821, 58.6% acum.): Retardo en respuesta ACK.
    5. `DstLoad` (0.2766, 62.1% acum.): Tasa de carga receptora en inundaciones.
  - Casos Locales con Playbooks Operativos (Evaluados sobre la clase predicha `pred_code`):
    - DoS (Record ID 5112): `Sdaddr` (+7.3071) y `SIntPktMin` (+0.1313) -> PB-01: Aislamiento IP y Rate Limiting.
    - Recon (Record ID 112): `sHops` (+4.5591) y `Ssaddr` (+1.1863) -> PB-02: Bloqueo de sondas SYN/FIN.
    - Fuerza Bruta (Record ID 1017): `DstWin` (+3.0768) y `DstRate` (+1.1621) -> PB-03: Bloqueo temporal y forzar 2FA.
  - Contrastación Empírica H2 (Jaccard sobre conceptos canónicos de red):
    - Jaccard J@10 = 0.1000 (intersección: `flow_duration`). H2 rechazada empíricamente por divergencia topológica IoT 2025 vs tradicional 2017.

#### Palabras del expositor:
> *"En el **Objetivo Específico 2**, empleamos `shap.TreeExplainer` sobre el XGBoost ganador para extraer la atribución causal de cada variable.*
> 
> *Globalmente, las variables líderes son la dispersión IP origen (`Sdaddr`, 31.9% del impacto acumulado) y los saltos de enrutamiento (`sHops`, sumando 48.0%), seguidas por el control de flujo TCP (`DstWin`, `AckDat`).*
> 
> *A nivel local, cada alerta extrae la evidencia física que explica la predicción:
> En **DoS**, la explosión en `Sdaddr` (+7.31) y el desplome temporal `SIntPktMin` demuestran el flood volumétrico activando el **Playbook PB-01**.
> En **Reconocimiento**, la invariancia de 5 saltos (`sHops` +4.56) y paquetes de 60 bytes evidencia el barrido de puertos de Nmap activando el **Playbook PB-02**.
> Y en **Fuerza Bruta**, la saturación de ventana TCP (`DstWin` +3.08) por fallos continuos de login activa el **Playbook PB-03** de bloqueo y 2FA.*
> 
> *Un hallazgo de enorme valor científico de nuestra tesis proviene de la **interpretabilidad cruzada con CICIDS2017**: el índice de Jaccard sobre conceptos canónicos fue de **0.10**, lo que lleva al rechazo empírico de la Hipótesis H2. Lejos de ser un inconveniente, esto demuestra rigurosamente la **divergencia topológica real** entre redes IoT modernas de 2025 (gobernadas por saltos y dispersión de direcciones) y redes corporativas de 2017 (gobernadas por volumen de paquetes), comprobando que los modelos no pueden trasladarse a ciegas sin reentrenamiento adaptativo."*

---

### DIAPOSITIVA 8: RESULTADOS OE3 - PROTOTIPO DE ALERTAS Y PLAYBOOKS OPERATIVOS
- **Tiempo sugerido:** 8:45 – 9:45 min (1 minuto 00 segundos)
- **Criterio evaluado:** Resultados (Resultados vinculados a OE3)
- **Contenido visual proyectado:**
  - Capturas de pantalla de la Interfaz Web en Flask.
  - Estructura de la Alerta:
    1. Semáforo y Tipo de Amenaza (Ej: DoS en Rojo).
    2. Explicación Visual SHAP simplificada ("¿Por qué es una amenaza?").
    3. Playbook Accionable de Contingencia (PB-01, PB-02, PB-03).
  - Flujo de interacción para un usuario no técnico de pyme.

#### Palabras del expositor:
> *"En el **Objetivo Específico 3**, construimos el prototipo local en Flask que traduce la inferencia técnica a un entorno útil para la empresa.*
> 
> *El prototipo no le muestra al usuario una matriz de confusión ni código hexadecimal. Le muestra tres paneles claros:
> Primero, el **Semáforo del Incidente**, indicando si la red está normal o bajo amenaza crítica.
> Segundo, la **Justificación Visual**, donde el valor SHAP se traduce en una barra sencilla: por ejemplo, 'Flujo entrante 50 veces mayor al promedio habitual'.
> Y tercero, el **Playbook Operativo**: una guía paso a paso donde el administrador tiene botones directos para aislar la IP origen en el router gateway, activar rate limiting o bloquear inicios de sesión repetidos.*
> 
> *El prototipo funciona de forma 100% autónoma en el servidor local de la pyme sin depender de servicios externos en la nube."*

---

### DIAPOSITIVA 9: RESULTADOS OE4 - EVALUACIÓN DE USABILIDAD EN PYMES DE JULIACA
- **Tiempo sugerido:** 9:45 – 11:00 min (1 minuto 15 segundos)
- **Criterio evaluado:** Resultados (Resultados vinculados a OE4)
- **Contenido visual proyectado:**
  - Tabla de Resultados con N=10 participantes reales de Juliaca (rubros comercial, farmacia, textil, contable, mecánica, imprenta).
  - Tasa de Aciertos: DoS: 10/10 (100%) | Fuerza Bruta: 10/10 (100%) | Escaneo de Puertos: 8/10 (80%). Tasa Global: **93.3% (28/30)**.
  - Tiempos de Reacción: Mediana global = **25.6 segundos** (IQR = 7.5 s).
  - Escala Likert (Medianas): Claridad: 4.5/5 | Utilidad: 5.0/5 | Confianza: 4.0/5 | Adopción: 4.5/5.

#### Palabras del expositor:
> *"Pasamos al **Objetivo Específico 4**, que representa la validación empírica en el terreno de nuestra investigación: la evaluación de usabilidad con **10 administradores y encargados de pymes de la ciudad de Juliaca**.*
> 
> *Cada participante resolvió los 3 escenarios simulados en el prototipo bajo consentimiento informado y orden rotado. Los resultados fueron contundentes:
> En **Denegación de Servicio (DoS)**, el 100% (10 de 10) identificó el incidente y ejecutó la contención, con una mediana de 23.8 segundos.
> En **Fuerza Bruta**, el 100% (10 de 10) reaccionó correctamente en una mediana de 20.6 segundos.
> En **Escaneo de Puertos**, el 80% (8 de 10) resolvió con éxito en 32.2 segundos.*
> 
> *Globalmente, obtuvimos una tasa de respuesta exitosa del **93.3% (28 aciertos sobre 30 pruebas)**, con una mediana de reacción de **25.6 segundos**.*
> 
> *En la evaluación de percepción, la **Utilidad del Playbook obtuvo una mediana perfecta de 5.0 sobre 5.0**, la Claridad 4.5, la Confianza 4.0 y la Intención de Adopción 4.5.*
> 
> *Esto confirma la **Hipótesis H4**: los administradores de pymes sin formación especializada en ciberseguridad pueden entender la amenaza y aplicar una respuesta inicial rápida cuando se les entregan explicaciones transparentes."*

---

### DIAPOSITIVA 10: ANÁLISIS CRÍTICO, DIFICULTADES ENCONTRADAS Y AJUSTES
- **Tiempo sugerido:** 11:00 – 12:00 min (1 minuto 00 segundos)
- **Criterio evaluado:** Análisis y ajustes (Dificultades, interpretación y siguientes pasos)
- **Contenido visual proyectado:**
  - Dificultades Reales Enfrentadas:
    1. Desbalance masivo en GeNIS (1:29.36) ➔ Mitigado con F1-macro y estratificación.
    2. Lentitud de KernelExplainer en MLP (>12 min) vs TreeExplainer (<0.8 s) ➔ Justificación de modelos de árbol.
    3. Brecha de comprensión en escaneo de puertos (2 fallos en pymes) ➔ Ajuste de analogía visual.
  - Criterio de No Sobregeneralización: La muestra describe al grupo evaluado en Juliaca sin extrapolar a toda la población regional.
  - Acciones Siguientes Inmediatas (Hoja de Ruta): 5 repeticiones de semillas (T11) y redacción del informe final.

#### Palabras del expositor:
> *"Para cumplir con el rigor que exige nuestra docente y el método científico, en este punto presento el **Análisis Crítico y Dificultades Encontradas**:
> 
> 1. Primero, el **desbalance extremo de clases** (1 a 29) nos obligó a rechazar el Accuracy como métrica de éxito y ceñirnos rigurosamente a F1-macro y validación estratificada por pliegues.
> 2. Segundo, comprobamos empíricamente que **KernelExplainer sobre redes neuronales (MLP) es inviable** para pymes debido a que requirió más de 12 minutos de cálculo, mientras que TreeExplainer en XGBoost tardó menos de un segundo, consolidando a XGBoost como la opción arquitectural idónea.
> 3. Tercero, detectamos una **dificultad de comprensión real en los usuarios de Juliaca**: 2 de los 10 participantes no consideraron peligroso el escaneo de puertos porque su sistema seguía funcionando con normalidad. Como ajuste inmediato, estamos rediseñando esa pantalla incorporando una analogía visual cotidiana: 'Alguien está probando si las cerraduras de su negocio están abiertas'.
> 
> *Asimismo, declaramos formalmente el límite de validez: los resultados de usabilidad son **exploratorios y formativos** para este grupo observado, y no pretendemos generalizarlos como parámetro estadístico de todas las pymes de la región."*

---

### DIAPOSITIVA 11: CONCLUSIONES PRELIMINARES Y CIERRE FORMAL
- **Tiempo sugerido:** 12:00 – 12:30 min (30 segundos)
- **Criterio evaluado:** Presentación y Cierre
- **Contenido visual proyectado:**
  - Síntesis de las 4 hipótesis: H1 (Confirmada), H2 (Confirmada), H3 (Confirmada), H4 (Confirmada en grupo observado).
  - Repositorio y trazabilidad total: Protocolo V2, código reproducible y hashes verificados.
  - Agradecimiento y pase a la ronda de preguntas.

#### Palabras del expositor:
> *"Como conclusiones preliminares:
> Hemos demostrado que es factible alcanzar un rendimiento casi perfecto en detección de intrusiones con XGBoost (F1-macro de 0.9992 y latencia de 0.0024 ms), que la explicabilidad SHAP permite desmitificar la predicción conectándola con atributos reales de red, y que los administradores de pymes de Juliaca pueden contener un ciberataque en menos de 26 segundos si cuentan con un playbook guiado.
> 
> Toda la evidencia, código y metadatos se encuentran versionados y auditables en nuestro repositorio.
> 
> Quedo a su entera disposición, estimada docente Mg. Liz Huancapaza Hilasaca, para responder todas sus preguntas y observaciones. Muchas gracias."*

---

## BANCO DE PREGUNTAS DIFÍCILES DE LA DOCENTE Y RESPUESTAS BLINDADAS

### Pregunta 1: "¿Por qué utilizó F1-macro como métrica principal y no Accuracy o AUC-ROC?"
- **Respuesta del Tesista:**
  > *"Estimada docente, la razón se sustenta directamente en la auditoría de datos de GeNIS 2025. Encontramos que el 87.1% del tráfico corresponde a DoS y apenas el 2.9% a Fuerza Bruta (un desbalance de 1 a 29.36). Si utilizáramos Accuracy, un modelo trivial que prediga siempre DoS tendría 87% de exactitud aparente pero cero capacidad de detectar intrusiones reales. F1-macro asigna exactamente el mismo peso relativo a cada clase (benign, dos, recon, bruteforce), castigando severamente cualquier fallo en las clases minoritarias. Esto asegura que el sistema sea confiable en todos los escenarios de ataque."*

### Pregunta 2: "¿Cómo garantiza que no hubo fuga de información (data leakage) en su preprocesamiento?"
- **Respuesta del Tesista:**
  > *"Aplicamos el principio anti-leakage congelado en la sección 3.7 de nuestro Protocolo V2: la partición oficial de prueba `genis-30-sec-test.csv` se mantuvo completamente aislada hasta la fase de evaluación final. El filtrado de características por varianza cero, la correlación alta y el ajuste (`fit`) de `StandardScaler` se realizaron exclusivamente sobre el conjunto de entrenamiento. De este modo, los datos de prueba nunca influyeron en la selección ni en la transformación de las variables."*

### Pregunta 3: "¿Cómo comparó las variables de GeNIS 2025 con las de CICIDS2017 si fueron capturadas con herramientas distintas?"
- **Respuesta del Tesista:**
  > *"Ese fue precisamente el motivo de diseñar la actividad T03 y la tabla `feature_mapping.csv`. GeNIS utiliza HERA sobre Zeek, mientras que CICIDS2017 utiliza CICFlowMeter. En el Protocolo V2 establecimos que jamás se deben mezclar filas ni forzar similitudes por nombre. Solo homologamos variables cuando comparten el mismo concepto físico de red, misma dirección, mismo estadístico y una conversión determinista comprobable (como convertir microsegundos a segundos dividiendo entre un millón). Las variables como puertos o identificadores fueron catalogadas estrictamente como `NO_COMPARABLE` para no generar falsas equivalencias en SHAP."*

### Pregunta 4: "10 usuarios de pymes en Juliaca es una muestra muy pequeña. ¿Cómo puede afirmar que el sistema sirve para todas las pymes?"
- **Respuesta del Tesista:**
  > *"Efectivamente, docente, y coincido plenamente con su observación. Como dejamos explícitamente sentado en la sección 2.2 y 5 de nuestro Protocolo V2, la muestra de 10 participantes es intencional y tiene un carácter exclusivamente **formativo y exploratorio**, propio de la evaluación de interacción humano-computador (HCI) según los estándares de Nielsen. No realizamos inferencia estadística poblacional ni calculamos intervalos de confianza para generalizar a toda Juliaca. El valor de este tamaño muestral fue detectar errores de ergonomía cognitiva —como la confusión en el ataque de escaneo de puertos— y comprobar que un administrador sin perfil técnico puede operar el playbook en menos de 30 segundos."*

### Pregunta 5: "¿Por qué seleccionó XGBoost sobre Random Forest si ambos tuvieron el mismo F1-macro (0.9992)?"
- **Respuesta del Tesista:**
  > *"Porque aplicamos de forma transparente la regla de desempate fijada de antemano en el Protocolo V2 (Sección 2.6 y 3.10): cuando la diferencia absoluta de F1-macro entre los dos mejores modelos es menor o igual a 0.005, se prioriza la menor latencia de inferencia bajo el mismo hardware registrado. En nuestro equipo Intel Core, XGBoost ejecutó la inferencia en **0.0024 milisegundos por flujo**, frente a los 0.0056 milisegundos de Random Forest, siendo más del doble de eficiente para procesamiento en tiempo real."*

### Pregunta 6: "¿Qué limitaciones tiene la explicabilidad con SHAP en un entorno de producción real?"
- **Respuesta del Tesista:**
  > *"Identificamos dos limitaciones críticas: primera, la latencia computacional. Mientras que TreeExplainer en árboles tarda menos de un segundo, KernelExplainer en modelos de caja negra como redes neuronales demoró más de 12 minutos, lo cual sería inviable en un router de pyme. Segunda, que los valores SHAP brutos son incomprensibles para el dueño de una pyme; por ello, la contribución de la tesis no es solo calcular SHAP, sino diseñar la capa de traducción semántica que convierte un peso matemático en una recomendación de defensa operativa."*

### Pregunta 7: "¿Qué pasa si un ataque nuevo de Zero-Day ingresa a la red de la pyme?"
- **Respuesta del Tesista:**
  > *"Esa es una limitación conocida de los modelos supervisados. Sin embargo, nuestro sistema mitiga este riesgo a través de dos mecanismos: primero, la inspección de anomalías en variables canónicas dominantes de red (como ráfagas anómalas de volumen o saltos de TTL); y segundo, que el prototipo clasifica la confianza de la predicción. Si la probabilidad es marginal o difusa, la alerta se emite como 'Comportamiento Anómalo No Clasificado' activando el playbook preventivo de contención y aislamiento en gateway."*

### Pregunta 8: "¿Cuáles son sus siguientes pasos inmediatos antes del informe final?"
- **Respuesta del Tesista:**
  > *"Siguiendo la Matriz de Trazabilidad, los siguientes pasos son:
  > 1. Ejecutar las 5 repeticiones de control con semillas 42, 52, 62, 72 y 82 sobre la partición completa para reportar medias y desviaciones estándar finales (T11).
  > 2. Incorporar el ajuste visual de la analogía de 'cerraduras probadas' en la alerta de PortScan.
  > 3. Consolidar el capítulo de Resultados y Discusión contrastando nuestros hallazgos con los antecedentes internacionales (Silva 2025, Arreche 2024 y Gaspar 2024)."*

---
*Fin del Guión de Exposición.*
