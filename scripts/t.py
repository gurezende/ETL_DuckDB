import duckdb


duckdb.read_parquet("data.parquet")
# duckdb.sql("""
#         select 
#             product,
#             avg(quantity) as avg_quantity, 
#             avg(price) as avg_price 
#         from data.parquet 
#         group by product
#            """).show()

# duckdb.sql("""
#         select 
#            quantity,
#            count(quantity)*100 / (select count(*) from data.parquet) as ct_quantity 
#         from data.parquet 
#         group by 1
#            """).show()

duckdb.sql("select * from data.parquet").show()