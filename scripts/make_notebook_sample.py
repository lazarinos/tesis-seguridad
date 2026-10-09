"""Genera la muestra estratificada de GeNIS (semilla 42) usada por el notebook de demostración."""
import os
import pandas as pd
from sklearn.model_selection import train_test_split

OUT = os.path.join("notebook", "data")
os.makedirs(OUT, exist_ok=True)

for split, n in (("train", 20000), ("test", 5000)):
    df = pd.read_csv(os.path.join("datasets", "genis", f"genis-30-sec-{split}.csv"))
    sample, _ = train_test_split(df, train_size=n, stratify=df["CategoryLabel"], random_state=42)
    sample = sample.sort_index()
    path = os.path.join(OUT, f"genis_muestra_{split}.csv.gz")
    sample.to_csv(path, index=False, compression="gzip")
    print(split, len(df), "->", len(sample), sample["CategoryLabel"].value_counts().to_dict(), os.path.getsize(path) // 1024, "KB")
