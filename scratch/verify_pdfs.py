import os

BIB_DIR = r"c:\Users\LAZARINOS\Downloads\tesis-seguridad\bibliography"
NUEVOS_DIR = os.path.join(BIB_DIR, "nuevos")

# Clasificación de archivos según su carpeta de destino
files_config = [
    # Originales (en raíz de bibliography/)
    {"filename": "P01_gaspar_shap_lime_mlp_ieee_access_2024.pdf", "path": BIB_DIR},
    {"filename": "P02_arreche_exai_nids_ieee_access_2024.pdf", "path": BIB_DIR},
    {"filename": "P04_corea_xai_comparative_meditcom2024.pdf", "path": BIB_DIR},
    {"filename": "P06_alabbadi_iot_xai_sensors_2025.pdf", "path": BIB_DIR},
    {"filename": "P07_ensemble_dl_ids_xai_appsci_2025.pdf", "path": BIB_DIR},
    {"filename": "P09_arreche_xai_ids_framework_appsci_2024.pdf", "path": BIB_DIR},
    # Nuevos (en bibliography/nuevos/)
    {"filename": "P03_hermosilla_xai_forensics_appsci_2025.pdf", "path": NUEVOS_DIR},
    {"filename": "P05_computers_xai_analyzing_ids_2025.pdf", "path": NUEVOS_DIR},
    {"filename": "P08_jcp_generalization_gaps_dos_2025.pdf", "path": NUEVOS_DIR},
    {"filename": "P10_future_internet_fed_xai_ids_2025.pdf", "path": NUEVOS_DIR},
    {"filename": "P11_appsci_posthoc_categorization_2024.pdf", "path": NUEVOS_DIR},
    {"filename": "P12_electronics_fed_xai_vehicles_2025.pdf", "path": NUEVOS_DIR},
    {"filename": "P13_zero_trust_marine_sensors_2024.pdf", "path": NUEVOS_DIR},
    {"filename": "P14_alabdulatif_ensemble_dl_xai_appsci_2025.pdf", "path": NUEVOS_DIR},
    {"filename": "L01_zanabria_seguridad_unap_2019.pdf", "path": NUEVOS_DIR},
    {"filename": "N01_figueroa_ml_pymes_lima_2024.pdf", "path": NUEVOS_DIR},
    {"filename": "N02_hernandez_zerotrust_unmsm_2025.pdf", "path": NUEVOS_DIR},
    {"filename": "N03_yauri_snort_uni_2017.pdf", "path": NUEVOS_DIR},
    {"filename": "N04_jimenez_ids_raspberry_puno_2016.pdf", "path": NUEVOS_DIR},
    {"filename": "N05_ore_scada_mineria_upc_2021.pdf", "path": NUEVOS_DIR},
    {"filename": "N06_torres_snort_ml_utp_2025.pdf", "path": NUEVOS_DIR},
    {"filename": "N07_manrique_ids_sdn_pucp_2021.pdf", "path": NUEVOS_DIR},
    # Teóricos (en bibliography/teoria/)
    {"filename": "T01_lundberg_shap_neurips_2017.pdf", "path": os.path.join(BIB_DIR, "teoria")},
    {"filename": "T02_ribeiro_lime_kdd_2016.pdf", "path": os.path.join(BIB_DIR, "teoria")},
    {"filename": "T03_reeder_neat_warnings_soups_2011.pdf", "path": os.path.join(BIB_DIR, "teoria")}
]

print("Iniciando auditoría de consistencia de los archivos PDF en subcarpetas separadas...")
all_ok = True
missing_count = 0
invalid_count = 0

for item in files_config:
    filename = item["filename"]
    folder = item["path"]
    file_path = os.path.join(folder, filename)
    
    if not os.path.exists(file_path):
        print(f"[FALTA] El archivo {filename} no existe en {folder}")
        all_ok = False
        missing_count += 1
        continue
        
    # Verificar tamaño mínimo
    size = os.path.getsize(file_path)
    if size < 500:
        print(f"[VACÍO/CORRUPTO] {filename} tiene un tamaño muy pequeño ({size} bytes).")
        all_ok = False
        invalid_count += 1
        continue
        
    # Verificar firma mágica de PDF (%PDF-)
    try:
        with open(file_path, 'rb') as f:
            header = f.read(4)
            if header != b"%PDF":
                print(f"[FIRMA INVÁLIDA] {filename} no empieza con %PDF. Cabecera encontrada: {header}")
                all_ok = False
                invalid_count += 1
                continue
    except Exception as e:
        print(f"[ERROR LECTURA] {filename} no pudo ser abierto: {e}")
        all_ok = False
        invalid_count += 1
        continue

if all_ok:
    print(f"\n[VERIFICACIÓN EXITOSA] Todos los {len(files_config)} PDFs requeridos están físicamente en sus rutas correspondientes (6 originales en la raíz y 16 nuevos en 'nuevos/'), tienen tamaño correcto y la firma de PDF válida.")
else:
    print(f"\n[AUDITORÍA CON ERRORES] Faltan: {missing_count} archivos. Inválidos: {invalid_count} archivos.")
    exit(1)
