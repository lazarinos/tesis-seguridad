# Cuaderno de demostración

`Tesis_Deteccion_Intrusiones_XAI.ipynb` reproduce el procedimiento de la tesis sobre una **muestra estratificada de GeNIS 2025** (20,000 flujos de train y 5,000 de test, semilla 42), sin necesidad de los datasets completos.

- `data/`: muestra comprimida (≈3 MB). Se regenera con `python scripts/make_notebook_sample.py` desde la raíz del repositorio si se dispone de GeNIS completo.
- `resultados_oficiales/`: copias de los resultados de la corrida `RUN_REPRO_V2_03_CLEANROOM` (GeNIS completo y CICIDS2017) que el cuaderno lee en la parte 8.

El cuaderno ya incluye las salidas ejecutadas. Para volver a correrlo:

```bash
pip install -r requirements.txt
jupyter notebook Tesis_Deteccion_Intrusiones_XAI.ipynb
```

Los valores de la muestra pueden diferir de los oficiales; los oficiales (partes 7–8) son los que sustentan la tesis. OE4 (usuarios) está pendiente.
