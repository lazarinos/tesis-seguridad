# UNIVERSIDAD NACIONAL DE JULIACA
## Facultad de Ciencias de la Ingeniería
### Escuela Profesional de Ingeniería de Software y Sistemas

**Curso:** Seminario de Tesis II — 2026-II  
**Docente:** Liz Huancapaza Hilasaca  
**Autor:** Ccolla Lazarinos, Fernando  
**Título:** *Detección de intrusiones de red con aprendizaje automático y técnicas de explicabilidad (XAI) para pequeñas y medianas empresas de Juliaca, Puno*

# MATRIZ DE TRAZABILIDAD TÉCNICA

## 1. Finalidad

La matriz demuestra que los objetivos de la investigación están conectados con actividades concretas, procedimientos ejecutables, evidencias verificables, métricas previamente definidas y una forma explícita de análisis.

La trazabilidad esperada es:

**Objetivo → actividad → procedimiento → evidencia → métrica/criterio → análisis → conclusión.**

---

## 2. Matriz principal

| Objetivo | Actividad | Evidencia verificable | Procedimiento | Métrica / criterio | Análisis |
|---|---|---|---|---|---|
| **OE1. Comparar el rendimiento de al menos tres algoritmos de aprendizaje automático en GeNIS 2025 y mediante la repetición independiente del experimento en CICIDS2017.** | Auditar datasets; homologar clases; preprocesar; entrenar RF, XGBoost y MLP; validar; seleccionar; evaluar GeNIS-test; repetir de forma independiente en CICIDS2017. | `dataset_audit_*.csv`, `feature_mapping.csv`, splits, pipeline serializado, configuraciones, `cv_results_*.csv`, modelos, predicciones, métricas, matrices de confusión y reporte de contraste. | **P02–P10.** Particiones congeladas; preprocesamiento solo con entrenamiento; SMOTE solo en entrenamiento; validación cruzada estratificada de 5 pliegues; semilla 42; selección por F1 macro; test aislado; CICIDS2017 después del congelamiento. | Métrica principal: **F1 macro**. Secundarias: Accuracy, Precision macro, Recall macro, F1 por clase, matriz de confusión. **H1:** Accuracy ≥ 90 % en GeNIS y F1 macro ≥ 0.85 en CICIDS2017. | Comparación de media y variabilidad en validación; evaluación final en test; comparación descriptiva del desempeño entre datasets; análisis de matriz de confusión y errores por clase. |
| **OE2. Identificar las variables con mayor contribución a las predicciones del modelo seleccionado mediante los valores SHAP.** | Generar explicaciones globales y locales; ordenar variables; calcular contribución acumulada top 10; homologar rankings entre datasets; calcular Jaccard. | `shap_global.csv`, `shap_top10.csv`, gráficos SHAP, casos locales, `shap_jaccard.json`, tabla de equivalencias. | **P11.** TreeExplainer para RF/XGBoost; KernelExplainer para MLP con 100 instancias de referencia y 500 de prueba estratificadas, semilla 42. | `mean(|SHAP|)`, contribución acumulada de top 10 e índice de Jaccard. **H2:** contribución top 10 ≥ 70 % y Jaccard ≥ 0.40. | Ranking global; análisis de casos locales; comparación de variables dominantes homologadas entre GeNIS 2025 y CICIDS2017. |
| **OE3. Implementar un prototipo que traduzca las atribuciones generadas por SHAP en alertas comprensibles, útiles y accionables para usuarios no técnicos.** | Integrar predicción, explicación SHAP, traducción semántica y playbooks en una interfaz; medir eficiencia; ejecutar piloto. | Código fuente, versión del prototipo, capturas, `prototype_changelog.md`, reporte técnico, tiempos de inferencia y piloto. | **P12–P13.** Construcción en Flask/Tkinter; tres escenarios: DoS, Port Scan/Reconocimiento y Brute Force; prueba piloto con 2 usuarios; registro de observaciones. | Tiempo de inferencia por flujo; tiempo de explicación; funcionamiento completo del flujo detección → explicación → alerta → playbook. **H3:** inferencia < 500 ms/flujo. | Verificación funcional; estadística descriptiva de tiempos; análisis de incidencias del prototipo y del piloto. |
| **OE4. Evaluar la comprensibilidad, utilidad percibida y capacidad de respuesta inicial asociada a las alertas del prototipo en una muestra intencional de 8 a 12 administradores de pymes sin formación especializada en ciberseguridad.** | Validar instrumento; reclutar participantes; obtener consentimientos; aplicar tres escenarios; registrar respuesta y tiempo; analizar cuestionario. | Fichas de expertos, matriz de validación, consentimientos, base anonimizada, `usability_responses.csv`, `reaction_times.csv`, reporte de resultados. | **P13–P15.** Juicio de 3 expertos; piloto de 2 usuarios; muestra intencional de 8–12 participantes; una sesión por participante; tres escenarios; cuestionario estructurado. | % ataque correcto; % playbook correcto; tiempo de reacción; claridad, utilidad, confianza e intención de adopción. **H4:** ataque correcto ≥ 70 % y playbook correcto ≥ 60 %. | Frecuencias, porcentajes, medias, desviaciones; análisis descriptivo de Likert; alfa de Cronbach exploratorio; sin inferencia poblacional. |
| **Objetivo general. Desarrollar y evaluar el sistema completo.** | Integrar resultados técnicos, XAI, prototipo y usabilidad; contrastar hipótesis; discutir limitaciones y conclusiones. | Matriz de contrastación, capítulo de resultados/discusión, repositorio de evidencias, README y versión final de tesis. | **P15–P16.** Consolidación de evidencias; verificación de trazabilidad; contrastación con criterios fijados; registro de incidencias; cierre reproducible. | Cumplimiento documentado de H1–H4 y trazabilidad completa de resultados. | Integración de hallazgos sin modificar criterios después de observar resultados; discusión de fortalezas, limitaciones y alcance. |

---

## 3. Trazabilidad por semana

| Semana | Objetivo(s) principal(es) | Procedimiento | Producto / evidencia |
|---:|---|---|---|
| 1 | Todos | P01 | Protocolo V1.0 + decision log |
| 2 | OE1, OE4 | P02, preparación P13 | Inventario de datos + cuestionario |
| 3 | OE1, OE2 | P03–P04 | Auditoría + homologación |
| 4 | OE1 | P05–P06 | Splits + pipeline procesado |
| 5 | OE1 | P06–P07 | Configuraciones y datos congelados |
| 6 | Todos | Hito Unidad I | Paquete de evidencias metodológicas |
| 7 | OE1 | P07 | Entrenamiento y CV |
| 8 | OE1 | P08 | Modelo seleccionado y congelado |
| 9 | OE2 | P11 | Explicaciones SHAP |
| 10 | OE3 | P12 | Prototipo v1 |
| 11 | OE1, OE3, OE4 | P09, P13 | Métricas técnicas + piloto |
| 12 | Todos | Hito Unidad II | Sistema funcional + resultados preliminares |
| 13 | OE1, OE2, OE4 | P10 + preparación P14 | Contraste CICIDS2017 + reclutamiento |
| 14 | OE4 | P14 | Base de usabilidad |
| 15 | OE1–OE4 | P15 | Tablas, gráficos y análisis |
| 16 | Todos | P15–P16 | Contrastación, discusión y conclusiones |
| 17 | Todos | Cierre | Tesis consolidada + repositorio/evidencias |

---

## 4. Matriz de hipótesis, indicadores y fuente de evidencia

| Hipótesis | Indicador | Umbral | Fuente primaria |
|---|---|---:|---|
| **H1** | Accuracy GeNIS 2025 | ≥ 90,0 % | `genis_test_metrics.json` |
| **H1** | F1 macro CICIDS2017 | ≥ 0,85 | `cicids_test_metrics.json` |
| **H2** | Contribución acumulada top 10 SHAP | ≥ 70,0 % | `shap_top10.csv` |
| **H2** | Jaccard de variables homologadas | ≥ 0,40 | `shap_jaccard.json` |
| **H3** | Tiempo de inferencia por flujo | < 500 ms | archivo de benchmark / métricas técnicas |
| **H4** | Identificación correcta del ataque | ≥ 70,0 % | `usability_responses.csv` |
| **H4** | Selección correcta del playbook | ≥ 60,0 % | `usability_responses.csv` |

---

## 5. Relación entre variables, dimensiones e indicadores

| Variable | Dimensión | Indicadores principales | Evidencia |
|---|---|---|---|
| **VI: Sistema de detección de intrusiones basado en ML y explicabilidad SHAP** | Rendimiento clasificatorio | Accuracy, Precision macro, Recall macro, F1 macro | métricas y predicciones |
| VI | Explicabilidad matemática | contribución acumulada top 10, Jaccard | artefactos SHAP |
| VI | Eficiencia computacional | tiempo de inferencia y tiempo SHAP | logs/benchmark |
| **VD: Comprensibilidad, utilidad y capacidad de respuesta** | Comprensibilidad | ataque correcto, claridad | cuestionario |
| VD | Utilidad percibida | utilidad, confianza, intención de adopción | cuestionario |
| VD | Capacidad de respuesta | playbook correcto, tiempo de reacción | respuestas y cronometraje |

---

## 6. Controles experimentales vinculados a la trazabilidad

| Riesgo | Control | Evidencia que demuestra el control |
|---|---|---|
| Data leakage | Transformaciones y SMOTE solo con entrenamiento | pipeline, config y split manifests |
| Uso del test para ajustar | Test aislado hasta congelar modelo | `selected_model_manifest.json` con fecha previa al test |
| Cambio oportunista de métrica | F1 macro fijada en protocolo V1.0 | protocolo + decision log |
| Comparación injusta entre datasets | Homologación previa de clases y características | `label_mapping.csv`, `feature_mapping.csv` |
| Variabilidad no registrada | 5-fold CV y semilla 42 | `cv_results_*.csv` |
| Resultados no rastreables | ID único por experimento | logs + nombres de artefactos |
| Fallos ocultos | Registro de incidencias | `incident_log.csv` |
| Sesgo del instrumento | 3 expertos + piloto | fichas y `pilot_report.md` |
| Sobreinterpretación de muestra pequeña | Análisis exploratorio sin generalización | sección de análisis y discusión |

---

## 7. Criterio de completitud de la matriz

La trazabilidad se considerará completa cuando cada resultado reportado pueda responder, sin ambigüedad, a las siguientes preguntas:

1. ¿A qué objetivo responde?
2. ¿Qué actividad lo produjo?
3. ¿Qué procedimiento exacto se ejecutó?
4. ¿Qué datos y partición se usaron?
5. ¿Qué configuración y semilla se utilizaron?
6. ¿Qué evidencia fue guardada?
7. ¿Qué métrica o criterio se aplicó?
8. ¿Cómo se analizó?
9. ¿Qué hipótesis u objetivo sustenta?

Si una cifra final no puede rastrearse hasta estas evidencias, no debe incorporarse como resultado definitivo de la tesis.
