import duckdb
import os

# Read the current directory for parquet files
print([f for f in os.listdir("./") if f.endswith(".parquet")])

