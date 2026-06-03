# Estructura del Marco Teórico (Capítulo II)

Este documento define la estructura lógica, jerárquica y la fundamentación bibliográfica del **Capítulo II: Marco Teórico** para la tesis: *"Detección de intrusiones de red con aprendizaje automático y técnicas de explicabilidad (XAI) para pequeñas y medianas empresas de Juliaca, Puno"*.

---

## ESTRUCTURA SISTEMÁTICA Y FUNDAMENTADA

### 2.1. Ciberseguridad Aplicada y Sistemas de Monitoreo en PyMES
*   **2.1.1. Gestión de Seguridad de la Información en Entornos de Recursos Limitados**
    *   *Fundamentación:* Análisis de los riesgos informáticos y la implementación de controles estándar bajo la norma ISO 17799 y seguridad perimetral para blindar plataformas de información crítica local en la región Puno.
    *   *Fuentes:* Zanabria & Tito (2019) [@zanabria2019seguridad_unap], Jiménez (2016) [@jimenez2016puno_raspberry_ids].
*   **2.1.2. Sistemas de Detección de Intrusiones (IDS/IPS)**
    *   *Fundamentación:* Clasificación de los IDS (basados en host y basados en red), comparación entre la detección tradicional por firmas frente a la detección de anomalías.
    *   *Fuentes:* Torres & Abensur (2025) [@torres2025snort_ml_utp], Manrique & Santiváñez (2021) [@manrique2021ids_sdn_pucp].
*   **2.1.3. Arquitectura Zero Trust y Prevención de Fuga de Datos (DLP)**
    *   *Fundamentación:* Principios de "nunca confiar, siempre verificar", segmentación lógica de red, control de acceso estricto y prevención de fuga de datos (DLP) ante la telemetría del tráfico de datos industrial perimetral.
    *   *Fuentes:* Hernandez (2025) [@hernandez2025zerotrust_unmsm].

### 2.2. Modelos de Machine Learning aplicados a IDS de Red (NIDS)
*   **2.2.1. Clasificadores Supervisados de Tráfico Anómalo**
    *   *Fundamentación:* Algoritmos de clasificación supervisada para flujos de red: Random Forest, XGBoost y Redes Neuronales Artificiales (MLP). Rendimiento métrico comparativo en entornos de recursos computacionales limitados.
    *   *Fuentes:* Figueroa & Cañihua (2024) [@figueroa2024ml_ids_lima], Ore & Donaire (2021) [@ore2021scada_upc], Corea et al. (2024) [@corea2024comparative].
*   **2.2.2. Conjuntos de Datos de Tráfico (Datasets) para IDS**
    *   *Fundamentación:* Análisis del dataset principal **GeNIS (2025)** (construido sobre CyberRange y flujos de red empresarial moderna) y el dataset clásico de benchmark **CICIDS2017** (Universidad de Brunswick), analizando sus variables y capacidad de generalización.
    *   *Fuentes:* Silva et al. (2025) [@genis2025], Sharafaldin et al. (2018) [@sharafaldin2018cicids2017], Jameel et al. (2025) [@jcp_generalization_gaps_dos_2025].

### 2.3. Inteligencia Artificial Explicable (XAI) en Sistemas de Detección
*   **2.3.1. Teoría de Juegos y Valores de Shapley (SHAP)**
    *   *Fundamentación:* Fundamento matemático de las explicaciones aditivas de Shapley (SHAP) basadas en la teoría de juegos cooperativos para asignar pesos y contribuciones de características a las alertas de ciberseguridad.
    *   *Fuentes:* Lundberg & Lee (2017) [@lundberg2017shap], Gaspar et al. (2024) [@gaspar2024shap], Arreche et al. (2024) [@arreche2024exai].
*   **2.3.2. Explicaciones Locales Subrogadas Interpretables (LIME)**
    *   *Fundamentación:* Lógica de perturbación local y modelos lineales locales para aproximar explicaciones agnósticas del modelo en tiempo real.
    *   *Fuentes:* Ribeiro et al. (2016) [@ribeiro2016lime], Hermosilla et al. (2025) [@hermosilla2025xai_forensics].

### 2.4. Usabilidad e Interfaces de Alertas Comprensibles (Sec-UX)
*   **2.4.1. Framework NEAT para el Diseño de Alertas de Seguridad**
    *   *Fundamentación:* Criterios de diseño de alertas usables basados en que sean Necesarias, Explicadas, Accionables y Testeadas (NEAT), evitando la habituación y la fatiga por falsos positivos.
    *   *Fuentes:* Reeder et al. (2011) [@reeder2011neat], Alabdulatif (2025) [@ensemble_dl_ids_xai_appsci_2025].
*   **2.4.2. Respuesta Rápida (Playbooks) y Contexto Comercial en Juliaca**
    *   *Fundamentación:* Mapeo de puertos e IPs técnicas a alertas legibles y playbooks de mitigación operativa (aislamiento de hosts, bloqueo de puertos) aplicados al contexto socio-económico de las PyMES comerciales en Juliaca, Puno.
    *   *Fuentes:* Jiménez (2016) [@jimenez2016puno_raspberry_ids], Zanabria & Tito (2019) [@zanabria2019seguridad_unap].
