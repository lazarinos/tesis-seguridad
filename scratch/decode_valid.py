import os
import base64

nuevos_dir = r"c:\Users\LAZARINOS\Downloads\tesis-seguridad\bibliography\nuevos"

targets = [
    ("P03_hermosilla_xai_forensics_appsci_2025.base64", "P03_hermosilla_xai_forensics_appsci_2025.pdf"),
    ("N04_jimenez_ids_raspberry_puno_2016.base64", "N04_jimenez_ids_raspberry_puno_2016.pdf")
]

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
        print(f"[ERROR] Archivo {b64_name} no existe.")
