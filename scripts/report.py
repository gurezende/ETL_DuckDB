# imports
import duckdb
import pandas as pd
import seaborn as sns
import tabulate as tb
from datetime import datetime

# Date of the report
today = datetime.now().strftime("%Y-%m-%d")

# Create a connection to the database
con = duckdb.connect("data.db")

# Load the data to pandas dataframe
df = con.execute(f"SELECT * FROM DataByStore WHERE dt = '{today}'").fetchdf()
df_product = con.execute(f"SELECT * FROM DataByProduct WHERE dt = '{today}'").fetchdf()

### Calculate KPIs for the report ###

# BY STORE

# Total Quantity Sold & Revenue by store
total_quantity_sold = (df
                       .groupby(['store'])
                        .agg({'total_qty':'sum', 'total_revenue':'sum'})
                       .reset_index()
                       .sort_values(by='total_revenue', ascending=False)
                       .assign(pct_qty = lambda x: x['total_qty'] / x['total_qty'].sum(),
                               pct_revenue = lambda x: x['total_revenue']/ x['total_revenue'].sum())
                       )

print("|> KPIs by STORE")
print("\n--------- Total Quantity Sold & Revenue By Store ---------\n")
print(tb.tabulate(total_quantity_sold,headers='keys', tablefmt='psql'))
print("\n")

# Distribution of sales by product by store
products_by_store = (df
                     .groupby(['store', 'product'])
                     ['total_qty']
                     .sum()
                     .reset_index()
                     .assign(pct = lambda x: x['total_qty']/ x['total_qty'].sum())
                     .sort_values(by= ['store','pct'], ascending=[True, False])
                     )

print("\n--------- Total Quantity By Product By Store ---------\n")
print(tb.tabulate(products_by_store, headers='keys', tablefmt='psql'))
print("\n")


# BY PRODUCT

print("|> KPIs by PRODUCT")

# Total qty and revenue by product
total_qty_product = (df_product
                     .groupby('product')
                     .agg({'total_qty':'sum', 'total_revenue': 'sum'})
                     .reset_index()
                     .assign(pct_qty = lambda x: x['total_qty'] / x['total_qty'].sum(),
                               pct_revenue = lambda x: x['total_revenue']/ x['total_revenue'].sum())
                     .sort_values(by='total_revenue', ascending=False)
                     )

print("\n--------- Total Quantity Sold & Revenue By Product ---------\n")
print(tb.tabulate(total_qty_product, headers='keys', tablefmt='psql'))
print('\n')


# COMPARISON Week-Over-Week

