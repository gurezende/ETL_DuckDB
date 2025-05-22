# imports
import duckdb
import pandas as pd
import matplotlib.pyplot as plt
import tabulate as tb
from datetime import datetime, timedelta
from textwrap import dedent


def generate_report():
    
    """
    Generate a KPI report for sales data by store and product.

    This function connects to a DuckDB database, retrieves sales data for the current day,
    and calculates key performance indicators (KPIs) for both stores and products. It also
    compares sales data week-over-week and month-over-month. The function generates a report
    that includes total quantity sold and revenue by store and product, distribution of sales
    by product by store, and performance comparisons. It also creates visualizations in the
    form of a mosaic plot and saves the report to a Markdown file.

    Returns:
        str: The content of the generated report.
    """

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

    
    # Distribution of sales by product by store
    products_by_store = (df
                        .groupby(['store', 'product'])
                        ['total_qty']
                        .sum()
                        .reset_index()
                        .assign(pct = lambda x: x['total_qty']/ x['total_qty'].sum())
                        .sort_values(by= ['store','pct'], ascending=[True, False])
                        )


    # BY PRODUCT

    # Total qty and revenue by product
    total_qty_product = (df_product
                        .groupby('product')
                        .agg({'total_qty':'sum', 'total_revenue': 'sum'})
                        .reset_index()
                        .assign(pct_qty = lambda x: x['total_qty'] / x['total_qty'].sum(),
                                pct_revenue = lambda x: x['total_revenue']/ x['total_revenue'].sum())
                        .sort_values(by='total_revenue', ascending=False)
                        )

 
    # COMPARISON Week-Over-Week (WoW)

    # Last week
    last_week = (datetime.now() + timedelta(days=-7)).strftime("%Y-%m-%d")

    # Load the data to pandas dataframe
    df_last_wk = con.execute(f"SELECT * FROM DataByStore WHERE dt = '{last_week}'").fetchdf()
    df_product_last_wk = con.execute(f"SELECT * FROM DataByProduct WHERE dt = '{last_week}'").fetchdf()


    # Total Quantity Sold & Revenue by store
    wow_qty_sold = (df
                    .groupby(['store'])
                    .agg({'total_qty':'sum', 'total_revenue':'sum'})
                    .reset_index()
                    .merge(
                        df_last_wk
                        .groupby(['store'])
                        .agg({'total_qty':'sum', 'total_revenue':'sum'})
                        .reset_index()
                        .rename(columns={'total_qty':'last_week_qty', 'total_revenue':'last_week_revenue'}),
                        on='store',
                        how='left'   )
                    .assign(WoW_qty = lambda x: (x['total_qty'] - x['last_week_qty']) / x['last_week_qty'],
                            WoW_revenue = lambda x: (x['total_revenue'] - x['last_week_revenue']) / x['last_week_revenue'])
                    .sort_values(by='WoW_revenue', ascending=False)
                    )


    # COMPARISON Week-Over-Week (WoW)

    # Last week
    last_week = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    # Load the data to pandas dataframe
    df_last_wk = con.execute(f"SELECT * FROM DataByStore WHERE dt = '{last_week}'").fetchdf()
    df_product_last_wk = con.execute(f"SELECT * FROM DataByProduct WHERE dt = '{last_week}'").fetchdf()


    # Total Quantity Sold & Revenue by store
    wow_qty_sold = (df
                    .groupby(['store'])
                    .agg({'total_qty':'sum', 'total_revenue':'sum'})
                    .reset_index()
                    .merge(
                        df_last_wk
                        .groupby(['store'])
                        .agg({'total_qty':'sum', 'total_revenue':'sum'})
                        .reset_index()
                        .rename(columns={'total_qty':'last_week_qty', 'total_revenue':'last_week_revenue'}),
                        on='store',
                        how='left'   )
                    .assign(WoW_qty = lambda x: (x['total_qty'] - x['last_week_qty']) / x['last_week_qty'],
                            WoW_revenue = lambda x: (x['total_revenue'] - x['last_week_revenue']) / x['last_week_revenue'])
                    .sort_values(by='WoW_revenue', ascending=False)
                    )

    
    # COMPARISON Month-Over-Month (MoM)

    # Last week
    last_month = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

    # Load the data to pandas dataframe
    df_last_mth = con.execute(f"SELECT * FROM DataByStore WHERE dt = '{last_month}'").fetchdf()
    df_product_last_mth = con.execute(f"SELECT * FROM DataByProduct WHERE dt = '{last_month}'").fetchdf()


    # Total Quantity Sold & Revenue by store
    mom_qty_sold = (df
                    .groupby(['store'])
                    .agg({'total_qty':'sum', 'total_revenue':'sum'})
                    .reset_index()
                    .merge(
                        df_last_wk
                        .groupby(['store'])
                        .agg({'total_qty':'sum', 'total_revenue':'sum'})
                        .reset_index()
                        .rename(columns={'total_qty':'last_month_qty', 'total_revenue':'last_month_revenue'}),
                        on='store',
                        how='left'   )
                    .assign(MoM_qty = lambda x: (x['total_qty'] - x['last_month_qty']) / x['last_month_qty'],
                            MoM_revenue = lambda x: (x['total_revenue'] - x['last_month_revenue']) / x['last_month_revenue'])
                    .sort_values(by='MoM_revenue', ascending=False)
                    )

    
    # Graphics
    # Mosaic Plot
    fig = plt.figure(layout= 'constrained', figsize=(21, 14))
    mosaic = fig.subplot_mosaic('''
                                aaab
                                cdef
                                ''')


    # Plot A
    mosaic['a'].bar(total_quantity_sold.store, total_quantity_sold.total_revenue, color='coral')

    # Plot B through F
    mosaic['b'].barh(products_by_store.query('store == "store1"')['product'], 
                    products_by_store.query('store == "store1"')['pct'], 
                    color='forestgreen')
    mosaic['c'].barh(products_by_store.query('store == "store2"')['product'], 
                    products_by_store.query('store == "store2"')['pct'],
                    color='orange')
    mosaic['d'].barh(products_by_store.query('store == "store3"')['product'], 
                    products_by_store.query('store == "store3"')['pct'],               
                    color='royalblue')
    mosaic['e'].barh(products_by_store.query('store == "store4"')['product'], 
                    products_by_store.query('store == "store4"')['pct'],
                    color='purple')
    mosaic['f'].barh(products_by_store.query('store == "store5"')['product'], 
                    products_by_store.query('store == "store5"')['pct'],
                    color='gold')

    # Define Titles
    titles = ['Total Revenue (USD) by Store', '[STORE1] Total Quantity % Sold by Product', '[STORE2] Total Quantity % Sold by Product',
            '[STORE3] Total Quantity % Sold by Product', '[STORE4] Total Quantity % Sold by Product', '[STORE5] Total Quantity % Sold by Product']

    for ax, g_title in zip(mosaic.items(), titles):
        ax[1].set_title(g_title, fontstyle='italic')

    # Save the figure
    fig.savefig('mosaic.png')

    # Close the connection
    con.close()

    # Report
    report_content  = dedent(f"""\
# KPIs REPORT
Attached is the report for the day: **{datetime.now().strftime('%Y-%m-%d')}**.

## **|> KPIs by STORE**

### Total Quantity Sold & Revenue By Store
{tb.tabulate(total_quantity_sold,headers='keys', tablefmt='pipe')}

### Total Quantity By Product By Store
{tb.tabulate(products_by_store, headers='keys', tablefmt='pipe')}


## **|> KPIs by PRODUCT**

### Total Quantity Sold & Revenue By Product
{tb.tabulate(total_qty_product, headers='keys', tablefmt='pipe')}

### Week-Over-Week (WoW) Total Quantity Sold & Revenue By Store
{tb.tabulate(wow_qty_sold, headers='keys', tablefmt='pipe')}

### Month-Over-Month (MoM) Total Quantity Sold & Revenue By Store
{tb.tabulate(mom_qty_sold, headers='keys', tablefmt='pipe')}
\
""")

    with open("report.md", "w") as file:
        file.write(report_content)

    print("Report saved to report.md")

    # Return
    return report_content

# Test
if __name__ == "__main__":
    generate_report()