# Inventario y Control de Calidad de Datos (P02 - Tesis II)

**Fecha de actualizacion:** 2026-09-21 10:40:02
**Investigador:** Fernando Ccolla Lazarinos
**Protocolo:** V1.0 (P02 - Adquisicion e inventario)

## 1. Resumen de Conjuntos de Datos

| Dataset | Rol en Tesis | Fuente | Archivos | Tamano Total |
|---|---|---|---|---:|
| **GeNIS 2025** | Dataset Principal | Zenodo (Record 14919237) | 2 | 305.52 MB |
| **CICIDS2017** | Contraste Independiente | UNB CIC / HuggingFace Mirror | 8 | 843.66 MB |

## 2. Detalle de Archivos y Hashes Criptograficos

| Dataset | Archivo | Tamano (MB) | MD5 | SHA-256 |
|---|---|---:|---|---|
| GeNIS 2025 | `genis-30-sec-test.csv` | 61.11 | `4036025edce00dd708bb5c7876893096` | `0916b08ade1107ba...` |
| GeNIS 2025 | `genis-30-sec-train.csv` | 244.41 | `de6cf1c557ce3171a8d1944aa06917b2` | `815f419dd2ce3d56...` |
| CICIDS2017 | `Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv` | 73.55 | `b2b2764e4c8a4c390506de7ee81c32ee` | `6ff1580f5f81c0ae...` |
| CICIDS2017 | `Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv` | 73.34 | `4892380364f9c7ef297d3094d19f26bf` | `ca1824c51bfbb7b3...` |
| CICIDS2017 | `Friday-WorkingHours-Morning.pcap_ISCX.csv` | 55.62 | `134224ec64782709ae1078379f72c4fa` | `53a41c24d570ea83...` |
| CICIDS2017 | `Monday-WorkingHours.pcap_ISCX.csv` | 168.73 | `12ca72e319041856f6410e9a14d40581` | `852c4beb34eda186...` |
| CICIDS2017 | `Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv` | 79.25 | `29ab45bfe378d983552a801d0a90cac8` | `6bcda3857c250467...` |
| CICIDS2017 | `Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv` | 49.61 | `13e1c70d2b380bf5d90f82e60e7befb1` | `d67066211fb1689c...` |
| CICIDS2017 | `Tuesday-WorkingHours.pcap_ISCX.csv` | 128.82 | `df16dccfd59a4ee126690fd6b71ee0a4` | `52b8692ae8c7d2ed...` |
| CICIDS2017 | `Wednesday-workingHours.pcap_ISCX.csv` | 214.74 | `bf0dd7e9d991987df4e13ea58a1b409c` | `893c27dc968bf7a8...` |

## 3. Estado de Cumplimiento del Hito P02

- [x] Particiones oficiales de GeNIS 2025 (30s) adquiridas y aisladas.
- [x] Flujos etiquetados de CICIDS2017 adquiridos.
- [x] Hashes de integridad registrados para reproducibilidad.
