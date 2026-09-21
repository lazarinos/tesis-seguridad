# Registro de Problemas Conocidos (KNOWN_ISSUES.md)

## ISS-001: Enlaces de Google Drive inactivos
- **Estado:** Mitigado / Resuelto.
- **Descripción:** Las URLs de Google Drive para `genis-30-sec-train.csv` y `genis-30-sec-test.csv` reportadas en el README original devolvían errores de acceso.
- **Solución:** Reemplazados por el endpoint Zenodo API record 14919237 (`4-preprocessed.zip`) y Hugging Face para CICIDS2017.

## ISS-002: Bloqueo de bot en web scraping directo de Zenodo UI
- **Estado:** Resuelto.
- **Descripción:** Zenodo aplica protecciones Cloudflare/rate limiting a navegadores y llamadas directas sobre `/records/14919237/files/...`.
- **Solución:** Se comprobó que el endpoint `/api/records/14919237/files/.../content` con un User-Agent estándar responde HTTP 200 de forma inmediata y permite streaming de descarga.

## ISS-003: Ausencia de imbalanced-learn en el entorno Python global
- **Estado:** Pendiente para P06 (Preprocesamiento).
- **Descripción:** El paquete `imblearn` no se encuentra instalado en Python 3.11 global.
- **Acción:** Se instalará cuando se ejecute el preprocesamiento con SMOTE en P06. No bloquea la adquisición de datos P02.
