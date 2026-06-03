import os
import urllib.request

theory_dir = r"c:\Users\LAZARINOS\Downloads\tesis-seguridad\bibliography\teoria"

targets = [
    {
        "url": "https://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions.pdf",
        "filename": "T01_lundberg_shap_neurips_2017.pdf"
    },
    {
        "url": "https://aclanthology.org/N16-3020.pdf",
        "filename": "T02_ribeiro_lime_kdd_2016.pdf"
    },
    {
        "url": "http://cups.cs.cmu.edu/soups/2011/posters/soups_posters-Reeder.pdf",
        "filename": "T03_reeder_neat_warnings_soups_2011.pdf"
    }
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print("Iniciando la descarga de PDFs teóricos de ciberseguridad y XAI...")

for target in targets:
    url = target["url"]
    filename = target["filename"]
    out_path = os.path.join(theory_dir, filename)
    
    print(f"Descargando {filename} desde {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as response:
            with open(out_path, 'wb') as out_file:
                out_file.write(response.read())
        
        size = os.path.getsize(out_path)
        print(f"  [OK] Descargado {filename} con éxito. Tamaño: {size} bytes.")
    except Exception as e:
        print(f"  [ERROR] Falló la descarga de {filename}: {e}")

print("Proceso de descarga finalizado.")
