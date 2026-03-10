import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
base_dir = Path(__file__).resolve().parent.parent
file_path = base_dir / "data" / "sales.csv"

df = pd.read_csv(file_path, encoding = "cp1258")

df["revenue"] = df["PRICEEACH"] * df["QUANTITYORDERED"]

engine = create_engine("postgresql://postgres:04092005@localhost:5432/sales_db")

df.to_sql("sales", engine, if_exists ="replace", index = False)
print("Data loaded successfully")