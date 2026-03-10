import pandas as pd
from pathlib import Path
base_dir = Path(__file__).resolve().parent.parent
file_path = base_dir / "data" / "sales.csv"

df = pd.read_csv(file_path, encoding = "cp1258")

print(df.head())
print(df.info())