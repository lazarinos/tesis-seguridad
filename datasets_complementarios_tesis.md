# Datasets Complementarios para la Tesis

> [!IMPORTANT]
> **Decisión Definitiva Congelada en Protocolo V1.0 (Seminario de Tesis II - 2026-II):**  
> Conforme al Protocolo de Ejecución V1.0 y la Matriz de Trazabilidad Técnica, la tesis ha formalizado la adopción de:
> - **Dataset Principal:** **GeNIS 2025** (particiones oficiales preprocesadas de ventana de 30 segundos: `genis-30-sec-train.csv` y `genis-30-sec-test.csv`).
> - **Dataset de Contraste Independiente:** **CICIDS2017** (subconjunto estratificado reproducible de 100 000 flujos con semilla 42, derivado de `MachineLearningCSV`).
>
> Los demás datasets evaluados (UNSW-NB15, TON_IoT, CSE-CIC-IDS2018) quedan como antecedentes bibliográficos de referencia y no forman parte de la experimentación principal para mantener la viabilidad dentro del cronograma de 17 semanas.

---

## Idea central

La investigación **no se basa únicamente en GeNIS**. Se emplea:

- **GeNIS 2025** como dataset principal.
- **CICIDS2017** como validación y contraste externo independiente.

---

## Propuesta recomendada

### Opción mínima y realista

- **Dataset principal:** GeNIS 2025
- **Dataset complementario:** CICIDS2017

Esta opción ya te permite decir que no trabajaste con un solo dataset y que además validaste el enfoque con un benchmark ampliamente usado.

### Opción más sólida para tesis

- **Dataset principal:** GeNIS 2025
- **Dataset complementario 1:** CICIDS2017
- **Dataset complementario 2:** UNSW-NB15

Esta opción es mejor si deseas mostrar:

- comparación entre escenarios de tráfico;
- mayor robustez metodológica;
- evaluación en datasets recientes y clásicos de referencia.

### Opción opcional si deseas reforzar IoT o recursos limitados

- **Dataset adicional opcional:** TON_IoT

Este dataset es útil si quieres conectar tu trabajo con escenarios heterogéneos o con restricciones de recursos, algo que puede acercarse a ciertas realidades de PyMES.

---

## 1. GeNIS 2025

**Rol en la tesis:** dataset principal.

**Por qué sí conviene usarlo:**

- Es reciente.
- Es abierto.
- Está orientado a escenarios empresariales.
- Se alinea bien con la motivación de proteger PyMES.

**Fuente principal:**

- Paper: *GeNIS: A modular dataset for network intrusion detection and classification*  
  https://doi.org/10.1016/j.dib.2025.111487
- Dataset: Zenodo  
  https://zenodo.org/records/14919237

---

## 2. CICIDS2017

**Rol recomendado:** validación externa o benchmark complementario.

**Por qué conviene:**

- Es uno de los datasets más usados en IDS con machine learning.
- Incluye tráfico benigno y ataques comunes actualizados.
- Tiene PCAP y flujos etiquetados.
- Permite comparar tus resultados con muchos antecedentes.

**Qué aporta a tu tesis:**

- Fortalece la defensa metodológica.
- Permite mostrar que el modelo no funciona solo en GeNIS.
- Ayuda a comparar rendimiento y explicabilidad en otro entorno.

**Fuente oficial:**

- Página oficial UNB CIC  
  https://www.unb.ca/cic/datasets/ids-2017.html
- Paper base del dataset  
  https://doi.org/10.5220/0006639801080116

---

## 3. UNSW-NB15

**Rol recomendado:** segundo benchmark o validación adicional.

**Por qué conviene:**

- Es un dataset de referencia muy citado en investigación IDS.
- Fue generado con tráfico normal moderno y ataques contemporáneos.
- Incluye nueve tipos de ataques.
- Tiene 49 características ya estructuradas para modelado.

**Qué aporta a tu tesis:**

- Sirve para evaluar generalización.
- Te ayuda a comparar algoritmos sobre un benchmark muy conocido.
- Ya aparece en uno de los papers que seleccionaste en tu revisión bibliográfica.

**Fuente oficial:**

- Página oficial UNSW  
  https://research.unsw.edu.au/projects/unsw-nb15-dataset
- Paper base del dataset  
  https://doi.org/10.1109/MilCIS.2015.7348942

---

## 4. TON_IoT

**Rol recomendado:** apoyo opcional si decides incluir un escenario IoT o de recursos limitados.

**Por qué conviene:**

- Es un dataset más heterogéneo.
- Incluye tráfico de red, telemetría y registros de sistemas IoT e IIoT.
- Fue diseñado para validar aplicaciones de ciberseguridad basadas en IA.

**Qué aporta a tu tesis:**

- Te permite argumentar robustez en escenarios más variados.
- Puede servir para discutir similitudes entre IoT y pequeñas empresas con infraestructura limitada.

**Fuente oficial:**

- Página oficial UNSW  
  https://research.unsw.edu.au/projects/toniot-datasets
- Paper de red TON_IoT  
  https://doi.org/10.1016/j.scs.2021.102994

---

## 5. CSE-CIC-IDS2018

**Rol recomendado:** alternativa a CICIDS2017 si deseas un dataset CIC más amplio.

**Por qué conviene:**

- Amplía el ecosistema CICIDS con más infraestructura y más volumen.
- Incluye siete escenarios de ataque.
- Tiene más de 80 características extraídas con CICFlowMeter.

**Qué aporta a tu tesis:**

- Puede usarse como alternativa o extensión si quieres una validación más grande.
- Es útil si decides trabajar con más volumen de datos.

**Fuente oficial:**

- Página oficial UNB CIC  
  https://www.unb.ca/cic/datasets/ids-2018.html

---

## Recomendación concreta para tu tesis

Si quieres algo **viable y defendible**, te recomiendo decir esto:

> La tesis utilizará GeNIS 2025 como dataset principal, por su pertinencia y actualidad, y lo complementará con al menos un dataset de referencia, preferentemente CICIDS2017 o UNSW-NB15, para fortalecer la validación del modelo y evitar depender de un único escenario experimental.

Si quieres algo **más fuerte**, di esto:

> La tesis empleará GeNIS 2025 como base principal y realizará validación comparativa adicional con CICIDS2017 y UNSW-NB15, con el fin de evaluar desempeño, interpretabilidad y consistencia del modelo en diferentes entornos de tráfico.

---

## Qué deberías evitar decir

- “Voy a usar solo GeNIS y ya”.
- “La tesis consiste en implementar un sistema”.
- “Si funciona en un dataset, ya queda validado”.

Eso suena débil metodológicamente.

---

## Qué sí conviene decir

- “GeNIS será el dataset principal, pero no el único referente experimental”.
- “Se incorporará al menos un benchmark adicional para validación externa”.
- “La tesis no solo plantea un prototipo, sino también comparación, evaluación y explicabilidad”.
