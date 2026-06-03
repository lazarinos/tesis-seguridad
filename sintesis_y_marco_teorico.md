# Síntesis Comparativa y Estructura del Marco Teórico

Este documento consolida la **Síntesis Comparativa** y la **Estructura Inicial del Marco Teórico** para la tesis: *"Detección de intrusiones de red con aprendizaje automático y técnicas de explicabilidad (XAI) para pequeñas y medianas empresas de Juliaca, Puno"*.

---

## PARTE I: SÍNTESIS COMPARATIVA DE ANTECEDENTES

A partir de la revisión de los 22 antecedentes (14 internacionales, 7 nacionales, 1 local) se han identificado las siguientes tendencias, diferencias y vacíos en la literatura científica:

### 1. Tendencias Identificadas

*   **Transición Hacia la Inteligencia Artificial (ML/DL):** Existe una clara evolución metodológica desde la ciberseguridad convencional basada puramente en firmas y auditoría de vulnerabilidades estáticas (representadas en los antecedentes nacionales de Yauri 2017 y el local Zanabria 2019) hacia arquitecturas dinámicas basadas en aprendizaje automático, Zero Trust o detección de anomalías en flujos de red (Figueroa 2024, Hernandez 2025, Torres 2025).
*   **Adopción Dominante de SHAP y LIME:** En el plano internacional, el uso de explicabilidad post-hoc mediante valores de Shapley (SHAP) y explicaciones agnósticas locales (LIME) se ha consolidado como el estándar para resolver la opacidad de los clasificadores de "caja negra" como Random Forest, XGBoost y Redes Neuronales (Gaspar 2024, Arreche 2024, Hermosilla 2025).
*   **Enfoque en Entornos Distribuidos e IoT:** Investigaciones muy recientes (2024-2025) orientan la explicabilidad a entornos perimetrales y de Internet de las Cosas (IoT), implementando Aprendizaje Federado (Federated Learning) para mantener la privacidad de los datos locales a la par de explicaciones globales agregadas (Larriva-Novo 2025, Taheri 2025).

### 2. Diferencias Clave entre Enfoques

*   **Granularidad de Características (Features):** Los estudios internacionales varían desde análisis de secuencias de llamadas del sistema (ADFA-LD en Gaspar 2024) hasta flujos de red de alta dimensionalidad con más de 80 atributos (CICIDS2017 en Bilal 2025 y Alabdulatif 2025). Las investigaciones nacionales peruanas suelen concentrarse en escenarios controlados de tráfico real o en la simplificación de variables para hardware limitado como Raspberry Pi (Jiménez 2016).
*   **Evaluación de la Explicabilidad:** Mientras que algunos autores evalúan XAI de forma cualitativa mediante encuestas de satisfacción perceptual, los frameworks más avanzados proponen métricas cuantitativas como estabilidad, fidelidad por perturbación, robustez, completitud y similitud Jaccard (Arreche 2024, Hermosilla 2025).
*   **Modelos Evaluados:** Los antecedentes demuestran disparidad entre clasificadores tradicionales eficientes (Random Forest, Regresión Logística) y modelos secuenciales complejos (LSTM, GRU) o tabulares especializados (TabNet), evidenciando que los modelos más simples son preferibles en hardware con recursos limitados (Corea 2024).

### 3. Vacíos Científicos Detectados (Gap)

*   **Falta de Traducción Práctica del XAI para Usuarios No Técnicos:** La literatura internacional sobre XAI en IDS se enfoca de manera casi exclusiva en el rendimiento matemático de SHAP/LIME o en brindar interpretaciones complejas dirigidas a científicos de datos y analistas expertos de centros de operaciones de seguridad (SOC). No se identificaron estudios que aborden la **traducción semántica** de estas métricas técnicas a alertas legibles y accionables para administradores de negocios sin conocimientos previos en ciberseguridad.
*   **Validación Local en PyMES del Altiplano:** A nivel nacional peruano, las investigaciones de ML aplicado a IDS se limitan a Lima (Figueroa 2024, Torres 2025) u otros entornos urbanos consolidados, dejando de lado la realidad de las PyMES en ciudades comerciales intermedias con infraestructura digital precaria y limitado ancho de banda, como Juliaca, Puno.
*   **Evaluación Multidataset con GeNIS 2025:** Al ser un conjunto de datos publicado en 2025, GeNIS carece de estudios complementarios de validación cruzada y contraste con benchmarks tradicionales como CICIDS2017 para analizar su comportamiento explicable y capacidad de generalización en entornos reales de red corporativa pyme.

---

## PARTE II: ESTRUCTURA LOGICIAL Y CIENTÍFICA DEL MARCO TEÓRICO

A continuación, se define el primer borrador estructurado del Marco Teórico, organizado de forma científica y lógica:

### CAPÍTULO II: MARCO TEÓRICO

#### 2.1. Seguridad en Redes y Sistemas de Monitoreo
*   **2.1.1. Fundamentos de Ciberseguridad en Pequeñas y Medianas Empresas (PyMES):** Infraestructura digital en PyMES, vulnerabilidades comunes en redes comerciales, limitaciones presupuestarias e impactos operacionales de incidentes de seguridad.
*   **2.1.2. Sistemas de Detección de Intrusiones (IDS):** Clasificación de IDS (NIDS y HIDS), mecanismos de detección basados en firmas frente a detección de anomalías.
*   **2.1.3. Motores Tradicionales Open Source:** Funcionamiento, configuración y límites técnicos de Snort y Suricata en el monitoreo perimetral.

#### 2.2. Aprendizaje Automático (Machine Learning) en IDS
*   **2.2.1. Clasificación Supervisada de Tráfico de Red:** Regresión Logística, Árboles de Decisión, Random Forest, XGBoost y Redes Neuronales Artificiales.
*   **2.2.2. Métricas de Evaluación de Modelos:** Matriz de confusión, Accuracy, Precision, Recall, F1-Score, Curva ROC y Área Bajo la Curva (AUC).
*   **2.2.3. Conjunto de Datos Principal - GeNIS (2025):** Escenarios de CyberRange, flujos de tráfico empresarial benigno y clasificaciones de ataques (DoS, Brute Force, Reconnaissance).
*   **2.2.4. Conjunto de Datos de Validación - CICIDS2017:** Arquitectura del dataset, flujos etiquetados y representatividad de amenazas modernas como benchmark de contraste.

#### 2.3. Inteligencia Artificial Explicable (XAI) en Ciberseguridad
*   **2.3.1. El Problema de la "Caja Negra" (Black-Box Model):** Opacidad en modelos de ML/DL, desconfianza del usuario no especializado y necesidad de transparencia en alertas críticas.
*   **2.3.2. Métodos de Explicación Post-Hoc Agnósticos del Modelo:** Principio de interpretabilidad local frente a global.
*   **2.3.3. Explicaciones Aditivas de Shapley (SHAP):** Teoría de juegos cooperativos, cálculo de valores de Shapley, consistencia, aditividad local, y diagramas de resumen (Summary plots) e importancia de características.
*   **2.3.4. Explicaciones Locales Subrogadas Interpretables (LIME):** Perturbaciones locales, aproximación lineal y contrastes teóricos frente a SHAP.

#### 2.4. Usabilidad e Interpretabilidad en la Respuesta a Alertas
*   **2.4.1. Diseño de Interfaces de Seguridad Centradas en el Usuario (Sec-UX):** Usabilidad de alertas de ciberseguridad, fatiga por alertas y criterios de interpretabilidad para personal administrativo.
*   **2.4.2. Traducción de Explicaciones Técnicas a Acciones Operativas:** Mapeo de la contribución de variables (puertos, tasas de bits, bytes) a lenguaje natural ("Intento de saturación de red", "Pruebas de puertos abiertos", "Fuerza bruta de contraseñas").
*   **2.4.3. Protocolos de Respuesta Rápida (Playbooks) en PyMES:** Aislamiento de host, reporte a soporte externo y bloqueo de tráfico IPs como respuestas accionables recomendadas por el sistema.
*   **2.4.4. Contexto Tecnológico y Comercial en Juliaca, Puno:** Dinámica de las PyMES en Juliaca, oferta local de ciberseguridad, retos de conectividad e infraestructura de red local.
