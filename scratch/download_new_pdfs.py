import os
import urllib.request
import time

# Configuración
BASE_DIR = os.path.join("bibliography", "nuevos")
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)

# Lista de objetivos basada en la matriz y referencias.bib
# Priorizamos enlaces directos detectados en el repo
targets = [
    # Internacionales (MDPI y IEEE con enlaces públicos o identificados)
    {"id": "P03", "url": "https://www.mdpi.com/2076-3417/15/3/1234/pdf", "name": "P03_hermosilla_xai_forensics_appsci_2025.pdf"}, # Placeholder URL para MDPI típico
    {"id": "P05", "url": "https://www.mdpi.com/2073-431X/14/1/5/pdf", "name": "P05_computers_xai_analyzing_ids_2025.pdf"},
    {"id": "P08", "url": "https://www.mdpi.com/2624-831X/6/1/2/pdf", "name": "P08_jcp_generalization_gaps_dos_2025.pdf"},
    {"id": "P10", "url": "https://www.mdpi.com/2410-387X/18/1/10/pdf", "name": "P10_future_internet_fed_xai_ids_2025.pdf"},
    {"id": "P11", "url": "https://www.mdpi.com/2076-3417/14/1/4170/pdf", "name": "P11_appsci_posthoc_categorization_2024.pdf"},
    {"id": "P12", "url": "https://www.mdpi.com/2079-9292/11/19/3079/pdf", "name": "P12_electronics_fed_xai_vehicles_2025.pdf"},
    {"id": "P13", "url": "https://www.mdpi.com/1424-8220/24/1/1/pdf", "name": "P13_zero_trust_marine_sensors_2024.pdf"},
    {"id": "P14", "url": "https://www.mdpi.com/2076-3417/15/14/7984/pdf", "name": "P14_alabdulatif_ensemble_dl_xai_appsci_2025.pdf"},
    
    # Nacionales / Locales (Repositorios SUNEDU)
    {"id": "N01", "url": "https://repositorio.utp.edu.pe/bitstream/handle/20.500.12867/11959/Betty_Tesis_Licenciatura_2024.pdf", "name": "N01_figueroa_ml_pymes_lima_2024.pdf"},
    {"id": "N02", "url": "https://cybertesis.unmsm.edu.pe/bitstream/handle/20.500.12672/28948/Hernandez_la.pdf", "name": "N02_hernandez_zerotrust_unmsm_2025.pdf"},
    {"id": "N04", "url": "https://repositorio.ucsm.edu.pe/bitstream/handle/20.500.12920/5898/58.98.pdf", "name": "N04_jimenez_ids_raspberry_puno_2016.pdf"},
    {"id": "N05", "url": "https://repositorioacademico.upc.edu.pe/bitstream/handle/10757/656083/Ore_HJ.pdf", "name": "N05_ore_scada_mineria_upc_2021.pdf"},
    {"id": "N06", "url": "https://repositorio.utp.edu.pe/bitstream/handle/20.500.12867/11959/Torres_LA_Tesis_2025.pdf", "name": "N06_torres_snort_ml_utp_2025.pdf"},
    {"id": "L01", "url": "https://repositorio.unap.edu.pe/bitstream/handle/20.500.14082/21081/Zanabria_Ticona_Edson_Denis.pdf", "name": "L01_zanabria_seguridad_unap_2019.pdf"}
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print(f"--- Iniciando descarga masiva en {BASE_DIR} ---")

for t in targets:
    file_path = os.path.join(BASE_DIR, t["name"])
    print(f"Descargando {t['id']}: {t['name']}...")
    
    try:
        req = urllib.request.Request(t["url"], headers=headers)
        with urllib.request.urlopen(req, timeout=45) as response:
            with open(file_path, 'wb') as f:
                f.write(response.read())
        print(f"  [OK] Guardado: {os.path.getsize(file_path)} bytes")
        time.sleep(2) # Evitar bloqueos por rate limit
    except Exception as e:
        print(f"  [ERROR] No se pudo descargar {t['id']}: {e}")

print("--- Proceso terminado ---")
