#!/usr/bin/env python3
"""
Script de Subida a la Nube (Gofile) - Datasets Tesis II
Sube los archivos comprimidos de GeNIS 2025 y CICIDS2017 a Gofile para acceso rapido en la nube.
"""

import os
import sys
import time
import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "datasets"

FILES_TO_UPLOAD = [
    DATASETS_DIR / "genis_2025_30sec.zip",
    DATASETS_DIR / ".cache" / "MachineLearningCSV.zip"
]

def get_best_server():
    print("[*] Consultando servidores de Gofile...")
    resp = requests.get("https://api.gofile.io/servers", timeout=15)
    resp.raise_for_status()
    data = resp.json()
    server = data["data"]["servers"][0]["name"]
    print(f"[+] Servidor asignado: {server}")
    return server

def upload_file(server: str, file_path: Path):
    if not file_path.exists():
        print(f"[!] Archivo no encontrado: {file_path}")
        return None

    size_mb = file_path.stat().st_size / (1024 * 1024)
    print(f"\n[*] Subiendo {file_path.name} ({size_mb:.2f} MB) a la nube...")
    url = f"https://{server}.gofile.io/contents/uploadfile"
    
    start_time = time.time()
    with open(file_path, "rb") as f:
        res = requests.post(url, files={"file": f}, timeout=600)
    
    res.raise_for_status()
    res_data = res.json()
    elapsed = time.time() - start_time
    avg_speed = size_mb / elapsed if elapsed > 0 else 0
    
    if res_data.get("status") == "ok":
        download_url = res_data["data"]["downloadPage"]
        file_id = res_data["data"]["id"]
        print(f"[+] Subida exitosa en {elapsed:.1f}s ({avg_speed:.2f} MB/s)!")
        print(f"    -> Enlace en la Nube: {download_url}")
        print(f"    -> ID de Archivo: {file_id}")
        return {
            "name": file_path.name,
            "size_mb": round(size_mb, 2),
            "download_url": download_url,
            "file_id": file_id
        }
    else:
        print(f"[!] Error reportado por Gofile: {res_data}")
        return None

def main():
    print("=================================================================")
    print("        SUBIDA DE DATASETS A LA NUBE (ACCESO RAPIDO)            ")
    print("=================================================================")
    
    server = get_best_server()
    results = []
    
    for f in FILES_TO_UPLOAD:
        info = upload_file(server, f)
        if info:
            results.append(info)
            
    print("\n=================================================================")
    print("                 RESUMEN DE ENLACES EN LA NUBE                  ")
    print("=================================================================")
    for r in results:
        print(f"* {r['name']} ({r['size_mb']} MB): {r['download_url']}")
        
    # Guardar en un archivo de texto para referencia rápida
    out_file = BASE_DIR / "tesis_experimentos" / "01_data_metadata" / "enlaces_nube_rapida.txt"
    with open(out_file, "w", encoding="utf-8") as out:
        out.write("# Enlaces de Acceso Rapido en la Nube - Datasets Tesis II\n")
        out.write(f"Fecha: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for r in results:
            out.write(f"- {r['name']} ({r['size_mb']} MB): {r['download_url']}\n")
    print(f"\n[+] Enlaces guardados en: {out_file}")

if __name__ == "__main__":
    main()
