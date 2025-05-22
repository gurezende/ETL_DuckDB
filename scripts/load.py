# Imports
import duckdb
import os
import transform
from datetime import datetime, date


def transform_and_load(files):
    # Create a DuckDB database (If Not Exists) and load the parquet files
    (duckdb
    .connect("data.db")
    .execute("CREATE TABLE IF NOT EXISTS DataByStore (store VARCHAR, product VARCHAR, total_qty INTEGER, total_revenue DECIMAL(10, 2), dt DATE)")
    .execute("CREATE TABLE IF NOT EXISTS DataByProduct (product VARCHAR, total_qty INTEGER, avg_price DECIMAL(10, 2), avg_qty DECIMAL(10, 2), total_revenue DECIMAL(10, 2), dt DATE)")
    )

    # Create a connection to the database
    con = duckdb.connect("data.db")

    # Check if the tables exist
    con.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES")
    print(con.fetchall())

    # Run the transformation script
    by_store, by_product = transform.transform(files)

    # Insert the data into the table
    inserts = (duckdb.execute('SELECT * FROM by_store').fetchall())
    con.executemany("INSERT INTO DataByStore VALUES (?, ?, ?, ?, ?)", inserts)
    inserts = (duckdb.execute('SELECT * FROM by_product').fetchall())
    con.executemany("INSERT INTO DataByProduct VALUES (?, ?, ?, ?, ?, ?)", inserts)

    # Print the number of rows in the table
    con.execute("SELECT COUNT(*) FROM DataByStore")
    print(con.fetchall())

    con.execute("SELECT COUNT(*) FROM DataByProduct")
    print(con.fetchall())

    # Close the connection
    con.close()


# Test
if __name__ == '__main__':

    # Read the current directory for parquet files
    files = [f for f in os.listdir("./") if f.endswith(".parquet")]

    # Run the transformation script
    transform_and_load(files)
    

"""This script is used to load the data into a DuckDB database."""