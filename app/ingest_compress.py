# app/ingest_compress.py
import pandas as pd
import zlib

def load_and_compress_csv(file_path):
    df = pd.read_csv(file_path)
    compressed = zlib.compress(df.to_csv(index=False).encode())
    print(f"Original: {df.memory_usage(deep=True).sum()} bytes")
    print(f"Compressed: {len(compressed)} bytes")
    return df, compressed
