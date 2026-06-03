import os
import base64
import glob

nuevos_dir = r"c:\Users\LAZARINOS\Downloads\tesis-seguridad\bibliography\nuevos"
base64_files = glob.glob(os.path.join(nuevos_dir, "*.base64"))

for b64_path in base64_files:
    print(f"\nAnalizando {os.path.basename(b64_path)}...")
    with open(b64_path, "r", encoding="utf-8", errors="ignore") as f:
        data = f.read()
    
    if "," in data:
        data = data.split(",")[1]
        
    try:
        decoded = base64.b64decode(data.strip())
        header = decoded[:20]
        print(f"  Tamaño decodificado: {len(decoded)} bytes")
        print(f"  Cabecera decodificada: {header}")
        if header.startswith(b"%PDF"):
            print("  -> ¡VÁLIDO! Es un PDF real.")
        else:
            print("  -> ¡INVÁLIDO! Es HTML o texto.")
    except Exception as e:
        print("  -> Error al decodificar:", e)

