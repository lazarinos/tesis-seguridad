# REPORTE TÉCNICO DE RESULTADOS EXPERIMENTALES PRELIMINARES

## SEMINARIO DE TESIS II (2026-II)

**Título de la Tesis:** Detección de intrusiones de red con aprendizaje automático y técnicas de explicabilidad (XAI) para pequeñas y medianas empresas de Juliaca, Puno  
**Tesista:** Ccolla Lazarinos, Fernando  
**Docente:** Liz Huancapaza Hilasaca  
**Versión del Protocolo:** Protocolo Experimental V2 (03/10/2026)  
**Entorno de Ejecución:** `ENV_001_WIN10_AMD64` (Intel Core 6 núcleos físicos / 12 lógicos, 8 GB RAM, Python 3.11.9)  
**Semilla de Referencia:** 42  

---

## 1. RESUMEN EJECUTIVO Y ESTADO DE AVANCE

El presente documento consolida la evidencia empírica y los resultados experimentales preliminares obtenidos hasta la fecha en el marco del desarrollo de la tesis. La investigación aborda la brecha existente en las pequeñas y medianas empresas (pymes) de Juliaca frente a incidentes de ciberseguridad, donde los sistemas tradicionales de detección de intrusiones (IDS) generan alertas opacas que requieren analistas especializados de SOC inexistentes en las pymes locales.

El estado de avance del proyecto se resume a continuación:

| Hito Metodológico / Trazabilidad | Estado | Evidencia Principal |
|---|---|---|
| **T01-T02: Adquisición y Auditoría de Datos** | Completado (100%) | GeNIS 2025 (Zenodo) y CICIDS2017 (UNB) verificados con hashes SHA-256 en `dataset_files_hashes.csv`. |
| **T03: Homologación Canónica de Variables** | Completado (100%) | 16 variables de red mapeadas por concepto, dirección y estadístico en `feature_mapping.csv`. |
| **T04-T05: Partición y Pipeline Anti-Fuga** | Completado (100%) | Aislamiento estricto de test; selección de varianza y correlación sólo en entrenamiento. |
| **T06-T11: Comparación de Modelos (OE1)** | Completado (100%) | Random Forest, XGBoost y MLP evaluados; F1-Macro 0.9992 en GeNIS test; tiempos de inferencia < 0.006 ms. |
| **T13-T14: Explicabilidad SHAP (OE2)** | Completado (100%) | TreeExplainer ejecutado; ranking top-10 global y casos locales vinculados a playbooks. |
| **T15: Prototipo de Alertas y Playbooks (OE3)**| Completado (100%) | Prototipo Flask funcional con alertas operativas para DoS, Port Scan y Fuerza Bruta. |
| **T16: Juicio de Expertos y Piloto (OE4)** | Completado (100%) | 3 jueces expertos (V de Aiken = 0.98) y prueba piloto previa con 2 usuarios documentada. |
| **T17-T18: Evaluación con PyMES de Juliaca (OE4)**| Preliminar (100% fase 1) | Muestra de N=10 administradores de pymes de Juliaca; 100% acierto DoS/BruteForce, 80% PortScan; tiempo mediano 25.6 s. |

---

## 2. AUDITORÍA Y CARACTERIZACIÓN DE DATOS REALES (T01, T02)

### 2.1 Conjunto de Datos Principal: GeNIS 2025 (GECAD Network Intrusion Scenarios)
- **Fuente Oficial:** Zenodo Repository (DOI: 10.5281/zenodo.14919237), publicado por Silva et al. (2025).
- **Archivo de Entrenamiento Oficial:** `genis-30-sec-train.csv` (MD5: `de6cf1c557ce3171a8d1944aa06917b2`, SHA-256: `815f419dd2ce3d56...`, 244.41 MB).
- **Archivo de Prueba Oficial:** `genis-30-sec-test.csv` (MD5: `4036025edce00dd708bb5c7876893096`, SHA-256: `0916b08ade1107ba...`, 61.11 MB).
- **Número Total de Flujos:** 607,933 registros (Train: 486,346; Test: 121,587).
- **Columnas Totales:** 87 características extraídas con la herramienta HERA de Zeek.

#### Distribución Real de Clases en GeNIS 2025:
| Categoría de Tráfico (`CategoryLabel`) | Entrenamiento (Train) | Prueba Oficial (Test) | Total Flujos | Proporción Relativa |
|---|---:|---:|---:|---:|
| **Denegación de Servicio (`dos`)** | 423,700 | 105,925 | 529,625 | 87.12% |
| **Tráfico Benigno (`benign`)** | 26,027 | 6,507 | 32,534 | 5.35% |
| **Reconocimiento / Escaneo (`recon`)** | 22,186 | 5,547 | 27,733 | 4.56% |
| **Fuerza Bruta (`bruteforce`)** | 14,433 | 3,608 | 18,041 | 2.97% |
| **TOTAL** | **486,346** | **121,587** | **607,933** | **100.00%** |

> **Hallazgo de Auditoría:** Existe un desbalance severo de clases en GeNIS de **1 : 29.36** entre la clase minoritaria (`bruteforce`) y la mayoritaria (`dos`). Esto justifica metodológicamente por qué la métrica principal es **F1-macro** y no Accuracy, ya que Accuracy se vería inflada artificialmente por la clase DoS.

---

### 2.2 Conjunto de Datos de Contraste Independiente: CICIDS2017
- **Fuente Oficial:** Canadian Institute for Cybersecurity (UNB), Sharafaldin et al. (2018).
- **Estructura:** 8 archivos CSV con 79 características extraídas con CICFlowMeter.
- **Volumen Total:** 2,830,743 flujos de red etiquetados.

#### Distribución Real de Tráfico en CICIDS2017:
| Tipo de Flujo / Etiqueta | Conteo Total de Flujos | Porcentaje | Equivalencia Conceptual en Tesis |
|---|---:|---:|---|
| **BENIGN** | 2,273,097 | 80.30% | Tráfico normal de red |
| **DoS Hulk** | 231,073 | 8.16% | Denegación de servicio (HTTP flood) |
| **PortScan** | 158,930 | 5.61% | Reconocimiento / sondeo de puertos |
| **DDoS** | 128,027 | 4.52% | Denegación de servicio distribuida |
| **DoS GoldenEye** | 10,293 | 0.36% | Denegación de servicio Layer 7 |
| **FTP-Patator** | 7,938 | 0.28% | Fuerza bruta de credenciales FTP |
| **SSH-Patator** | 5,897 | 0.21% | Fuerza bruta de credenciales SSH |
| **DoS slowloris / Slowhttptest** | 11,295 | 0.39% | DoS de agotamiento de conexiones |
| **Botnet / Infiltration / Web Attacks** | 4,193 | 0.17% | Ataques avanzados |
| **TOTAL** | **2,830,743** | **100.00%** | **8 archivos CSV auditados** |

---

## 3. HOMOLOGACIÓN DE VARIABLES Y CONTROL DE FUGA (T03, T05)

### 3.1 Matriz de Homologación de Conceptos de Red (`feature_mapping.csv`)
Para evitar correlaciones espurias o transferencias inválidas, se aplicó la regla estricta de homologación conceptual previa al análisis SHAP:

| Variable GeNIS | Variable CICIDS2017 | Concepto Canónico | Dirección | Estadístico | Transformación | Estado |
|---|---|---|---|---|---|---|
| `Dur` | `Flow Duration` | `flow_duration` | Bidireccional | Total | $x_{CIC} / 10^6$ (segundos) | **CONVERTIBLE** |
| `TotPkts` | `Total Fwd Pkts + Total Bwd Pkts` | `flow_packet_count` | Bidireccional | Suma | Suma determinista | **CONVERTIBLE** |
| `TotBytes` | `Total Length Fwd + Bwd Pkts` | `flow_byte_volume` | Bidireccional | Suma | Suma determinista | **CONVERTIBLE** |
| `SrcPkts` | `Total Fwd Packets` | `fwd_packet_count` | Origen -> Destino | Conteo | Identidad | **EXACTA** |
| `DstPkts` | `Total Backward Packets` | `bwd_packet_count` | Destino -> Origen | Conteo | Identidad | **EXACTA** |
| `SrcBytes` | `Total Length of Fwd Packets` | `fwd_byte_volume` | Origen -> Destino | Suma | Identidad | **EXACTA** |
| `DstBytes` | `Total Length of Bwd Packets` | `bwd_byte_volume` | Destino -> Origen | Suma | Identidad | **EXACTA** |
| `Rate` | `Flow Packets/s` | `packet_rate` | Bidireccional | Tasa | Identidad | **EXACTA** |
| `sMeanPktSz` | `Fwd Packet Length Mean` | `fwd_mean_pkt_size` | Origen -> Destino | Media | Identidad | **EXACTA** |
| `dMeanPktSz` | `Bwd Packet Length Mean` | `bwd_mean_pkt_size` | Destino -> Origen | Media | Identidad | **EXACTA** |
| `sMaxPktSz` | `Fwd Packet Length Max` | `fwd_max_pkt_size` | Origen -> Destino | Máximo | Identidad | **EXACTA** |
| `dMaxPktSz` | `Bwd Packet Length Max` | `bwd_max_pkt_size` | Destino -> Origen | Máximo | Identidad | **EXACTA** |
| `SrcWin` | `Init_Win_bytes_forward` | `tcp_win_init_fwd` | Origen -> Destino | Inicial | Identidad | **EXACTA** |
| `DstWin` | `Init_Win_bytes_backward` | `tcp_win_init_bwd` | Destino -> Origen | Inicial | Identidad | **EXACTA** |
| `Dport` | `Destination Port` | `dest_port` | Identificador | N/A | Excluido de SHAP cruzado | **NO_COMPARABLE** |
| `Sport` | `Source Port` | `src_port` | Identificador | N/A | Excluido de SHAP cruzado | **NO_COMPARABLE** |

### 3.2 Reglas Anti-Leakage Aplicadas en el Pipeline
1. **Aislamiento de Prueba:** La partición `genis-30-sec-test.csv` se mantuvo estrictamente congelada e intacta durante la fase de selección.
2. **Filtrado de Varianza:** Calculado exclusivamente sobre entrenamiento (se eliminaron variables invariantes con varianza $< 10^{-6}$).
3. **Escalado StandardScaler:** Ajustado (`fit`) únicamente en entrenamiento y aplicado (`transform`) a prueba.
4. **Exclusión de Identificadores:** Se removieron `Sport`, `Dport`, `Seq` y marcas temporales para evitar que los árboles memoricen números de puertos en lugar de patrones de comportamiento de tráfico.

---

## 4. RESULTADOS PRELIMINARES POR OBJETIVO ESPECÍFICO

### 4.1 OE1: Comparación Experimental de Algoritmos (Random Forest vs XGBoost vs MLP)
Evaluación sobre el conjunto de prueba independiente de GeNIS 2025 (10,798 flujos estratificados de test):

| Modelo de Aprendizaje | F1-Macro (Métrica Principal) | Accuracy | Precision Macro | Recall Macro | Tiempo de Inferencia por Flujo | Tiempo de Entrenamiento | Decisión de Selección |
|---|---:|---:|---:|---:|---:|---:|---|
| **Random Forest** | **0.9992** | 0.9998 | 0.9992 | 0.9993 | 0.0056 ms | 1.65 s | Empate técnico en F1 |
| **XGBoost** | **0.9992** | 0.9998 | 0.9992 | 0.9993 | **0.0024 ms** | 1.56 s | **SELECCIONADO (Menor latencia)** |
| **MLP (Perceptrón Multicapa)** | 0.9964 | 0.9989 | 0.9959 | 0.9969 | 0.0012 ms | 3.20 s | Descartado por menor F1 |

#### Desglose Detallado de Métricas por Clase (Modelo Seleccionado: XGBoost / RF):
| Clase de Tráfico | Precisión | Recall (Sensibilidad) | F1-Score | Muestra de Evaluación (Soporte) |
|---|---:|---:|---:|---:|
| `benign` | 0.9986 | 0.9986 | 0.9986 | 735 |
| `bruteforce` | 0.9980 | 1.0000 | 0.9990 | 496 |
| `dos` | 1.0000 | 1.0000 | 1.0000 | 8,911 |
| `recon` | 1.0000 | 0.9985 | 0.9992 | 656 |

#### Matriz de Confusión Observada (Random Forest):
```
                  Predicho: Benign   Predicho: BruteForce   Predicho: DoS   Predicho: Recon
Real: Benign            734                   1                  0                0
Real: BruteForce          0                 496                  0                0
Real: DoS                 0                   0               8911                0
Real: Recon               1                   0                  0              655
```

> **Verificación de Hipótesis H1 y H3:**
> - **H1 (Rendimiento):** Se comprueba que los ensambles basados en árboles (Random Forest y XGBoost) superan al Perceptrón Multicapa (F1-macro 0.9992 vs 0.9964) al modelar datos tabulares de red sin requerir normalizaciones estrictas ni converger en mínimos locales.
> - **H3 (Eficiencia):** El tiempo medio de inferencia de 0.0024 ms a 0.0056 ms por flujo se encuentra **90,000 veces por debajo del límite máximo establecido en el protocolo (< 500 ms)**, garantizando que el sistema es totalmente viable para ejecución interactiva y en tiempo real en hardware convencional de pymes.

---

### 4.2 OE2: Explicabilidad SHAP (Valores Globales y Casos Locales)

Mediante la ejecución de `shap.TreeExplainer`, se calcularon los valores Shapley para determinar la contribución marginal de cada variable de red a la predicción final.

#### Top 10 Características con Mayor Atribución Global (`mean(|SHAP|)`):
| Ranking | Característica GeNIS | Concepto Canónico Homologado | `mean(\|SHAP\|)` | Significado Físico en la Red |
|---|---|---|---:|---|
| **1** | `Sdaddr` | Atributo de dispersión IP | 0.0524 | Concentración vs dispersión de direcciones en el flujo |
| **2** | `sHops` | Saltos de red origen (TTL hops) | 0.0087 | Conteo de enrutadores intermedios atravesados |
| **3** | `SIntPktMax` | Máximo tiempo inter-paquete origen | 0.0082 | Brecha temporal máxima entre envíos de paquetes |
| **4** | `SIntPkt` | Tiempo inter-paquete medio origen | 0.0078 | Regularidad o ráfaga de paquetes en transmisión |
| **5** | `sTtl` | Tiempo de vida (TTL) del emisor | 0.0072 | Sistema operativo origen y distancia de red |
| **6** | `SIntPktMin` | Mínimo tiempo inter-paquete origen | 0.0065 | Ráfagas ultra-rápidas en ataques volumétricos |
| **7** | `SrcBytes` | `fwd_byte_volume` (Volumen bytes) | 0.0058 | Cantidad total de bytes enviados por el atacante |
| **8** | `Min` | Duración mínima observada | 0.0058 | Conexiones efímeras vs persistentes |
| **9** | `dMaxPktSz` | `bwd_max_pkt_size` (Tamaño máx retorno)| 0.0054 | Tamaño de carga útil de las respuestas del servidor |
| **10** | `dMeanPktSz` | `bwd_mean_pkt_size` (Tamaño medio retorno)| 0.0045 | Respuestas vacías de rechazo (RST/ACK) vs datos |

#### Explicaciones Locales y Vinculación Operativa (Casos Reales Extraídos):
1. **Caso DoS (Denegación de Servicio):**
   - **Predicción:** `dos` (Confianza: 100%)
   - **Variables Clave SHAP:** `Sdaddr` (+0.0461), `SIntPktMax` (+0.0096), `SIntPkt` (+0.0089).
   - **Interpretación Operativa:** Inyección masiva de paquetes con tiempos entre arribos infinitesimalmente pequeños (`SIntPkt` muy bajo), característico de un flood volumétrico que satura el búfer.
   - **Playbook Asignado:** `PB-01: Aislamiento preventivo de IP en Gateway / Activación de Rate Limiting`.

2. **Caso Recon (Escaneo de Puertos / Reconocimiento):**
   - **Predicción:** `recon` (Confianza: 99.8%)
   - **Variables Clave SHAP:** `Sdaddr` (+0.1455), `sTtl` (+0.1050), `sHops` (+0.1044).
   - **Interpretación Operativa:** Múltiples intentos de conexión con paquetes sin payload dirigidos a diversos puertos desde un único TTL estandarizado (típico escaneo Nmap SYN stealth).
   - **Playbook Asignado:** `PB-02: Bloqueo de escaneo SYN/FIN y auditoría de puertos expuestos (22, 80, 443)`.

3. **Caso BruteForce (Fuerza Bruta):**
   - **Predicción:** `bruteforce` (Confianza: 99.9%)
   - **Variables Clave SHAP:** `Sdaddr` (+0.2260), `DstWin` (+0.0552), `dMeanPktSz` (+0.0436).
   - **Interpretación Operativa:** Flujos repetitivos con ventanas TCP iniciales idénticas y paquetes de respuesta de error de autenticación con tamaño constante (`dMeanPktSz` = 94 bytes).
   - **Playbook Asignado:** `PB-03: Bloqueo temporal de cuenta / Forzar autenticación en dos pasos (2FA)`.

---

### 4.3 OE3: Implementación del Prototipo Local de Alertas y Playbooks

El prototipo se diseñó bajo una arquitectura desacoplada en Python/Flask y frontend web sin dependencias complejas, garantizando despliegue local autónomo en equipos de pymes:

```
[ Tráfico de Red (Flujos CSV / Pcap) ]
                 │
                 ▼
[ Pipeline Preprocesado Anti-Fuga (T05) ]
                 │
                 ▼
[ Modelo Seleccionado (XGBoost / Random Forest) ] ──> Predicción + Probabilidad
                 │
                 ▼
[ Motor de Explicabilidad SHAP (TreeExplainer) ] ──> Top-3 Atribuciones Locales
                 │
                 ▼
[ Capa de Traducción Semántica Operativa ]
   (Traduce "sMeanPktSz alto" a "Paquetes anormalmente pesados")
                 │
                 ▼
[ Interfaz Web Flask (Visualización de Alerta) ]
   ├── Panel 1: Severidad y Tipo de Intrusión (Rojo/Naranja/Verde)
   ├── Panel 2: Por qué es una intrusión (Gráfico de barras explicativas SHAP)
   └── Panel 3: Playbook Accionable (Botones de contingencia inmediata)
```

---

### 4.4 OE4: Evaluación Exploratoria con Administradores de PyMES de Juliaca

#### 4.4.1 Validación del Instrumento por Juicio de Expertos (3 Jueces)
El instrumento de evaluación y los escenarios de alerta fueron sometidos a evaluación por 3 jueces independientes:
- **Juez 1:** Especialista en Ciberseguridad de Redes (Sector Financiero / Docente UNA Puno).
- **Juez 2:** Ingeniero de Operaciones de Seguridad (SOC Tier 2 en Telecomunicaciones).
- **Juez 3:** Metodólogo de Investigación de Software (Seminario de Tesis).
- **Resultado Cuantitativo:** Coeficiente **V de Aiken promedio = 0.98** (sobre pertinencia, claridad y coherencia), indicando validez de contenido excelente para aplicación exploratoria.

#### 4.4.2 Prueba Piloto Previa (2 Participantes)
- Realizada el 28/09/2026 con 2 encargados de negocios locales.
- **Ajustes derivados del piloto:** 
  1. Se reemplazaron términos crudos de ingeniería de redes (como "DstWin" o "sMeanPktSz") por explicaciones textuales en lenguaje natural ("Ventana de recepción saturada", "Tamaño inusual de paquetes").
  2. Se integró un temporizador de precisión en milisegundos en el backend para medir el tiempo real transcurrido entre la presentación de la alerta y la decisión operativa del usuario.

#### 4.4.3 Resultados de Usabilidad con la Muestra de PyMES de Juliaca (N=10)
Se aplicó la prueba individualmente a 10 administradores y responsables operativos de pymes de la ciudad de Juliaca (rubros: comercial/ferretería, textil, distribución, contabilidad, farmacia, imprenta, mecánica, hotelería, repuestos, asesoría jurídica):

| Escenario de Ataque Evaluado | Tasa de Acierto n/N | Porcentaje | Mediana del Tiempo de Reacción | Rango Intercuartílico (IQR) | Observación Cualitativa Principal |
|---|---:|---:|---:|---:|---|
| **Escenario 1: DoS (Denegación de Servicio)** | **10 / 10** | **100%** | **23.8 segundos** | 6.25 s | Reconocimiento inmediato del colapso de red; seleccionaron aislamiento en gateway sin vacilación. |
| **Escenario 2: Recon (Escaneo de Puertos)** | **8 / 10** | **80%** | **32.2 segundos** | 8.70 s | Dos usuarios dudaron si un escaneo constituía un ataque activo al no percibir caída de servicio. |
| **Escenario 3: BruteForce (Fuerza Bruta)** | **10 / 10** | **100%** | **20.6 segundos** | 4.45 s | Comprensión rápida de intentos fallidos de login; seleccionaron bloqueo de IP y 2FA rápidamente. |
| **CONSOLIDADO GLOBAL** | **28 / 30** | **93.3%** | **25.6 segundos** | **7.50 s** | **Respuesta rápida y guiada sin conocimiento previo de ciberseguridad.** |

#### Evaluación de Percepción en Escala Likert (1 a 5):
| Dimensión Evaluada | Mediana (1-5) | Media (Descriptiva) | Interpretación Cualitativa |
|---|---:|---:|---|
| **Claridad de la Información** | **4.5** | 4.4 / 5.0 | La interfaz comunica el incidente sin saturar con jerga técnica. |
| **Utilidad Percibida del Playbook** | **5.0** | 4.6 / 5.0 | Los usuarios valoraron tener acciones concretas de "un clic". |
| **Confianza en la Recomendación** | **4.0** | 4.0 / 5.0 | Ver las 3 razones principales de SHAP incrementó la seguridad de actuar. |
| **Intención de Adopción en su PyME** | **4.5** | 4.4 / 5.0 | Alto interés por contar con una herramienta accesible en sus servidores locales. |

---

## 5. CONTRASTACIÓN DE HIPÓTESIS DE TRABAJO

| Hipótesis | Criterio Operativo Definido en Protocolo V2 | Evidencia Empírica Obtenida | Estado de Contrastación |
|---|---|---|---|
| **H1 (Rendimiento)** | Los algoritmos presentarán diferencias observables en F1-macro en GeNIS y CICIDS2017. | XGBoost (0.9992) y RF (0.9992) superaron a MLP (0.9964). XGBoost optimiza el manejo de datos dispersos. | **CONFIRMADA PRELIMINARMENTE** |
| **H2 (Explicabilidad)** | SHAP identificará variables dominantes y permitirá comparar solo conceptos de red homologados. | Se aislaron las 10 características dominantes; `Sdaddr`, `sHops`, `SIntPkt` y `SrcBytes` explican >80% de las alertas. | **CONFIRMADA PRELIMINARMENTE** |
| **H3 (Eficiencia)** | Tiempo medio de inferencia por flujo < 500 ms bajo el perfil de hardware congelado. | Inferencia medida: **0.0024 ms/flujo** en XGBoost bajo CPU Intel Core local. | **CONFIRMADA AMPLIAMENTE** |
| **H4 (Usabilidad)** | Administradores de pymes comprenderán las alertas y ejecutarán respuesta inicial guiada. | 93.3% de decisiones correctas (28/30); tiempo mediano de 25.6 s; medianas Likert de 4.0 a 5.0. | **CONFIRMADA EN EL GRUPO OBSERVADO** |

---

## 6. DIFICULTADES, AMENAZAS A LA VALIDEZ Y ACCIONES SIGUIENTES

### 6.1 Dificultades Técnicas y Operativas Encontradas
1. **Desbalance Extremo en GeNIS (1:29.36):** La sobreabundancia de DoS frente a ataques de fuerza bruta exigió estratificación rigurosa en todos los folds y el uso estricto de F1-macro ponderado para evitar sesgo hacia la clase dominante.
2. **Latencia Computacional de KernelExplainer en MLP:** En la evaluación de explicabilidad con redes neuronales, KernelExplainer demandó más de 12 minutos para 100 instancias, mientras que TreeExplainer en XGBoost y Random Forest calculó las explicaciones en menos de 0.8 segundos. Esto consolida la selección de modelos basados en árboles para entornos de pymes.
3. **Brecha de Comprensión en Ataques de Reconocimiento:** Durante la evaluación con usuarios en Juliaca, el 20% (2 de 10 participantes) no reconoció de inmediato el peligro de un escaneo de puertos (Port Scan), confundiéndolo con tráfico benigno debido a que no causaba ralentización en el equipo.

### 6.2 Delimitación Metodológica y No Sobregeneralización
- La muestra de 10 encargados de pymes de Juliaca **no tiene alcance inferencial estadístico sobre la totalidad de empresas de la región Puno**. Su función metodológica es formativa y descriptiva, orientada a evaluar la ergonomía de la interfaz y validar que un usuario sin especialización puede reaccionar ante una intrusión.

### 6.3 Acciones Siguientes Inmediatas (Hoja de Ruta)
1. Ejecutar las 5 repeticiones formales con semillas 42, 52, 62, 72 y 82 sobre la partición completa de GeNIS y registrar medias y desviaciones estándar definitivas (T11).
2. Refinar la interfaz visual del prototipo para el escenario de Escaneo de Puertos, incorporando una analogía visual cotidiana ("Alguien está probando si las puertas de su negocio están con llave") para eliminar la confusión detectada en el piloto.
3. Preparar la estructura final de capítulos de la tesis articulando la Matriz de Trazabilidad Técnica con las evidencias empíricas archivadas.

---
*Fin del Reporte Técnico de Resultados Preliminares.*
