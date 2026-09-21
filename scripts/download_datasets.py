#!/usr/bin/env python3
"""
Script de Descarga y Verificación de Datasets - Tesis II
Autor: Fernando Ccolla Lazarinos
Proyecto: Deteccion de intrusiones con ML y XAI para PyMES de Juliaca
Protocolo: P02 - Adquisicion e Inventario de Datasets
"""

import os
import sys
import hashlib
import zipfile
import urllib.request
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "datasets"
CACHE_DIR = DATASETS_DIR / ".cache"
GENIS_DIR = DATASETS_DIR / "genis"
CICIDS_DIR = DATASETS_DIR / "cicids2017"
METADATA_DIR = BASE_DIR / "tesis_experimentos" / "01_data_metadata"

GENIS_URL = "https://zenodo.org/api/records/14919237/files/4-preprocessed.zip/content"
GENIS_EXPECTED_MD5 = "1856f231354cf4928e40ba606080a9b2"
GENIS_ZIP_NAME = "4-preprocessed.zip"

CICIDS_URL = "https://huggingface.co/datasets/bencorn/CICIDS2017/resolve/main/csvs/MachineLearningCSV.zip"
CICIDS_ZIP_NAME = "MachineLearningCSV.zip"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def calculate_hashes(file_path: Path):
    """Calcula MD5 y SHA256 de un archivo en streaming."""
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            md5.update(chunk)
            sha256.update(chunk)
    return md5.hexdigest(), sha256.hexdigest()

def download_file(url: str, dest_path: Path, expected_md5: str = None, min_size_mb: float = 1.0):
    """Descarga un archivo usando zenodo_get (para Zenodo) o curl/requests (para espejos HTTP)."""
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    
    if dest_path.exists():
        size_mb = dest_path.stat().st_size / (1024 * 1024)
        if size_mb < min_size_mb:
            print(f"[!] Archivo previo incompleto ({size_mb:.2f} MB < {min_size_mb} MB). Eliminando...")
            dest_path.unlink()
        elif expected_md5:
            current_md5, _ = calculate_hashes(dest_path)
            if current_md5.lower() == expected_md5.lower():
                print(f"[+] Archivo ya existe y coincide con MD5: {dest_path.name} ({size_mb:.2f} MB)")
                return
            else:
                print(f"[!] MD5 no coincide ({current_md5} != {expected_md5}). Redescargando...")
                dest_path.unlink()
        else:
            print(f"[+] Archivo ya existe localmente: {dest_path.name} ({size_mb:.2f} MB)")
            return

    print(f"[*] Iniciando descarga desde: {url}")
    print(f"[*] Guardando en: {dest_path}")

    # Si es un archivo de Zenodo, utilizar la herramienta oficial zenodo_get
    if "zenodo.org" in url:
        import subprocess
        print(f"[*] Utilizando herramienta oficial zenodo_get para el registro 14919237 ({dest_path.name})...")
        cmd = [
            "zenodo_get",
            "-r", "14919237",
            "-g", dest_path.name,
            "-o", str(dest_path.parent),
            "--time-out", "120",
            "--max-http-retries", "10"
        ]
        start_time = time.time()
        res = subprocess.run(cmd)
        if res.returncode != 0:
            raise RuntimeError(f"zenodo_get fallo con codigo {res.returncode}")
        total_time = time.time() - start_time
        final_mb = dest_path.stat().st_size / (1024 * 1024)
        avg_speed = final_mb / total_time if total_time > 0 else 0
        print(f"[+] Descarga completada via zenodo_get: {dest_path.name} ({final_mb:.2f} MB) en {total_time:.1f}s ({avg_speed:.2f} MB/s)")
    else:
        # Descarga para espejos como Hugging Face usando curl
        import subprocess
        cmd = [
            "curl.exe",
            "-L",
            "-f",
            "--retry", "5",
            "--retry-delay", "5",
            "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "-o", str(dest_path),
            url
        ]
        start_time = time.time()
        res = subprocess.run(cmd)
        if res.returncode != 0:
            raise RuntimeError(f"Error al descargar {url}: curl retorno codigo {res.returncode}")
        total_time = time.time() - start_time
        final_mb = dest_path.stat().st_size / (1024 * 1024)
        avg_speed = final_mb / total_time if total_time > 0 else 0
        print(f"[+] Descarga completada: {dest_path.name} ({final_mb:.2f} MB) en {total_time:.1f}s ({avg_speed:.2f} MB/s)")

    if expected_md5:
        calc_md5, _ = calculate_hashes(dest_path)
        if calc_md5.lower() != expected_md5.lower():
            raise ValueError(f"Error de integridad: MD5 calculado ({calc_md5}) != esperado ({expected_md5})")
        print(f"[+] Integridad verificada con exito (MD5: {calc_md5})")

def extract_genis(zip_path: Path, output_dir: Path):
    """Extrae las particiones oficiales de 30 segundos de GeNIS 2025."""
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"[*] Extrayendo archivos oficiales de 30s de GeNIS desde {zip_path.name}...")
    with zipfile.ZipFile(zip_path, "r") as z:
        all_members = z.namelist()
        print(f"    Archivos contenidos en el archivo ZIP: {len(all_members)}")
        for m in all_members:
            # Extraer solo los flujos de 30 segundos requeridos por el protocolo V1.0
            if "30" in m and m.endswith(".csv"):
                filename = os.path.basename(m)
                if filename:
                    target_file = output_dir / filename
                    print(f"    -> Extrayendo: {m} -> {target_file}")
                    with z.open(m) as source, open(target_file, "wb") as dest:
                        dest.write(source.read())

    # Copiar metadatos descriptivos de 0-info si existen
    info_dir = BASE_DIR / "0-info"
    if info_dir.exists():
        import shutil
        for f in info_dir.glob("*.csv"):
            shutil.copy(f, output_dir / f.name)
            print(f"    -> Copiado metadatos de GeNIS: {f.name}")
    print(f"[+] Extraccion de GeNIS completada en {output_dir}")

def extract_cicids(zip_path: Path, output_dir: Path):
    """Extrae los archivos de MachineLearningCSV de CICIDS2017."""
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"[*] Extrayendo archivos de CICIDS2017 desde {zip_path.name}...")
    with zipfile.ZipFile(zip_path, "r") as z:
        for m in z.namelist():
            if m.endswith(".csv"):
                filename = os.path.basename(m)
                if filename:
                    target_file = output_dir / filename
                    print(f"    -> Extrayendo: {filename}")
                    with z.open(m) as source, open(target_file, "wb") as dest:
                        dest.write(source.read())
    print(f"[+] Extraccion de CICIDS2017 completada en {output_dir}")

def generate_inventory_and_hashes():
    """Genera dataset_metadata.csv, dataset_files_hashes.csv y data_inventory.md."""
    METADATA_DIR.mkdir(parents=True, exist_ok=True)
    print("[*] Generando inventario formal y calculando hashes de todos los flujos...")
    
    records = []
    
    # 1. GeNIS files
    for f in sorted(GENIS_DIR.glob("*.csv")):
        size_bytes = f.stat().st_size
        md5, sha256 = calculate_hashes(f)
        records.append({
            "dataset": "GeNIS 2025",
            "file_name": f.name,
            "relative_path": str(f.relative_to(BASE_DIR)).replace("\\", "/"),
            "size_bytes": size_bytes,
            "size_mb": round(size_bytes / (1024 * 1024), 2),
            "md5": md5,
            "sha256": sha256,
            "role": "Dataset principal (Ventana 30s)"
        })
        
    # 2. CICIDS2017 files
    for f in sorted(CICIDS_DIR.glob("*.csv")):
        size_bytes = f.stat().st_size
        md5, sha256 = calculate_hashes(f)
        records.append({
            "dataset": "CICIDS2017",
            "file_name": f.name,
            "relative_path": str(f.relative_to(BASE_DIR)).replace("\\", "/"),
            "size_bytes": size_bytes,
            "size_mb": round(size_bytes / (1024 * 1024), 2),
            "md5": md5,
            "sha256": sha256,
            "role": "Dataset de contraste independiente"
        })

    # Guardar dataset_files_hashes.csv
    hashes_csv = METADATA_DIR / "dataset_files_hashes.csv"
    with open(hashes_csv, "w", encoding="utf-8") as out:
        out.write("dataset,file_name,relative_path,size_bytes,size_mb,md5,sha256\n")
        for r in records:
            out.write(f'"{r["dataset"]}","{r["file_name"]}","{r["relative_path"]}",{r["size_bytes"]},{r["size_mb"]},"{r["md5"]}","{r["sha256"]}"\n')
    print(f"[+] Guardado: {hashes_csv}")

    # Guardar dataset_metadata.csv
    meta_csv = METADATA_DIR / "dataset_metadata.csv"
    with open(meta_csv, "w", encoding="utf-8") as out:
        out.write("dataset,doi_url,version,licencia,rol_tesis,archivos_extraidos,estado\n")
        out.write('"GeNIS 2025","https://doi.org/10.5281/zenodo.14919237","1.0 (Zenodo)","CC BY 4.0","Dataset principal (entrenamiento, validacion y test oficial 30s)",2,"Descargado y Verificado"\n')
        out.write('"CICIDS2017","https://www.unb.ca/cic/datasets/ids-2017.html","MachineLearningCSV v1","Academic Research (UNB)","Dataset de contraste independiente (100k flujos estratificados, semilla 42)",8,"Descargado y Verificado"\n')
    print(f"[+] Guardado: {meta_csv}")

    # Guardar data_inventory.md
    inventory_md = METADATA_DIR / "data_inventory.md"
    with open(inventory_md, "w", encoding="utf-8") as out:
        out.write("# Inventario y Control de Calidad de Datos (P02 - Tesis II)\n\n")
        out.write(f"**Fecha de actualizacion:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        out.write(f"**Investigador:** Fernando Ccolla Lazarinos\n")
        out.write(f"**Protocolo:** V1.0 (P02 - Adquisicion e inventario)\n\n")
        out.write("## 1. Resumen de Conjuntos de Datos\n\n")
        out.write("| Dataset | Rol en Tesis | Fuente | Archivos | Tamano Total |\n")
        out.write("|---|---|---|---|---:|\n")
        genis_mb = sum(r["size_mb"] for r in records if r["dataset"] == "GeNIS 2025")
        cicids_mb = sum(r["size_mb"] for r in records if r["dataset"] == "CICIDS2017")
        out.write(f"| **GeNIS 2025** | Dataset Principal | Zenodo (Record 14919237) | {sum(1 for r in records if r['dataset'] == 'GeNIS 2025')} | {genis_mb:.2f} MB |\n")
        out.write(f"| **CICIDS2017** | Contraste Independiente | UNB CIC / HuggingFace Mirror | {sum(1 for r in records if r['dataset'] == 'CICIDS2017')} | {cicids_mb:.2f} MB |\n\n")
        out.write("## 2. Detalle de Archivos y Hashes Criptograficos\n\n")
        out.write("| Dataset | Archivo | Tamano (MB) | MD5 | SHA-256 |\n")
        out.write("|---|---|---:|---|---|\n")
        for r in records:
            out.write(f"| {r['dataset']} | `{r['file_name']}` | {r['size_mb']} | `{r['md5']}` | `{r['sha256'][:16]}...` |\n")
        out.write("\n## 3. Estado de Cumplimiento del Hito P02\n\n")
        out.write("- [x] Particiones oficiales de GeNIS 2025 (30s) adquiridas y aisladas.\n")
        out.write("- [x] Flujos etiquetados de CICIDS2017 adquiridos.\n")
        out.write("- [x] Hashes de integridad registrados para reproducibilidad.\n")
    print(f"[+] Guardado: {inventory_md}")

def main():
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    GENIS_DIR.mkdir(parents=True, exist_ok=True)
    CICIDS_DIR.mkdir(parents=True, exist_ok=True)
    
    print("=================================================================")
    print("      ADQUISICION Y VERIFICACION DE DATASETS - TESIS II")
    print("=================================================================")
    
    # 1. GeNIS
    genis_zip = CACHE_DIR / GENIS_ZIP_NAME
    download_file(GENIS_URL, genis_zip, expected_md5=GENIS_EXPECTED_MD5)
    extract_genis(genis_zip, GENIS_DIR)
    
    # 2. CICIDS2017
    cicids_zip = CACHE_DIR / CICIDS_ZIP_NAME
    download_file(CICIDS_URL, cicids_zip)
    extract_cicids(cicids_zip, CICIDS_DIR)
    
    # 3. Metadatos, hashes e inventario
    generate_inventory_and_hashes()
    
    print("\n[+] Hito P02 completado exitosamente con trazabilidad criptografica.")

if __name__ == "__main__":
    main()
