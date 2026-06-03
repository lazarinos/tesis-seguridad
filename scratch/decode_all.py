import os
import base64

nuevos_dir = r"c:\Users\LAZARINOS\Downloads\tesis-seguridad\bibliography\nuevos"

targets = [
    ("P05_computers_xai_analyzing_ids_2025.base64", "P05_computers_xai_analyzing_ids_2025.pdf"),
    ("P08_jcp_generalization_gaps_dos_2025.base64", "P08_jcp_generalization_gaps_dos_2025.pdf"),
    ("P10_future_internet_fed_xai_ids_2025.base64", "P10_future_internet_fed_xai_ids_2025.pdf"),
    ("P11_appsci_posthoc_categorization_2024.base64", "P11_appsci_posthoc_categorization_2024.pdf"),
    ("P12_electronics_fed_xai_vehicles_2025.base64", "P12_electronics_fed_xai_vehicles_2025.pdf"),
    ("P13_zero_trust_marine_sensors_2024.base64", "P13_zero_trust_marine_sensors_2024.pdf"),
    ("P14_alabdulatif_ensemble_dl_xai_appsci_2025.base64", "P14_alabdulatif_ensemble_dl_xai_appsci_2025.pdf"),
    ("L01_coyla_ids_iso27001_upeu_juliaca_2019.base64", "L01_coyla_ids_iso27001_upeu_juliaca_2019.pdf"),
    ("N01_figueroa_ml_pymes_lima_2024.base64", "N01_figueroa_ml_pymes_lima_2024.pdf"),
    ("N02_huamani_snort_pymes_ayacucho_2020.base64", "N02_huamani_snort_pymes_ayacucho_2020.pdf"),
    ("N03_tineo_suricata_corporativo_ayacucho_2020.base64", "N03_tineo_suricata_corporativo_ayacucho_2020.pdf"),
    ("N05_quispe_scada_mineria_upc_2021.base64", "N05_quispe_scada_mineria_upc_2021.pdf"),
    ("N06_sanchez_snort_ml_colegios_lima_2025.base64", "N06_sanchez_snort_ml_colegios_lima_2025.pdf"),
    ("N07_perez_ml_iot_revision_sistemica_2026.base64", "N07_perez_ml_iot_revision_sistemica_2026.pdf")
]

print("Iniciando la decodificación masiva de los 14 archivos base64...")

for b64_name, pdf_name in targets:
    b64_path = os.path.join(nuevos_dir, b64_name)
    pdf_path = os.path.join(nuevos_dir, pdf_name)
    
    if os.path.exists(b64_path):
        print(f"Decodificando {b64_name} a {pdf_name}...")
        with open(b64_path, "r", encoding="utf-8", errors="ignore") as f:
            data = f.read()
            
        if "," in data:
            data = data.split(",")[1]
            
        try:
            decoded_bytes = base64.b64decode(data.strip())
            with open(pdf_path, "wb") as f_out:
                f_out.write(decoded_bytes)
            print(f"  [OK] Escrito {pdf_name} ({len(decoded_bytes)} bytes)")
            # Eliminar el archivo .base64
            os.remove(b64_path)
            print(f"  [OK] Eliminado {b64_name}")
        except Exception as e:
            print(f"  [ERROR] Falló decodificación de {b64_name}: {e}")
    else:
        print(f"[AVISO] Archivo {b64_name} no existe (quizás ya decodificado).")

print("Decodificación masiva completada.")
