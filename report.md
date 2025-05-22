# KPIs REPORT
Attached is the report for the day: **2025-05-22**.

## **|> KPIs by STORE**

### Total Quantity Sold & Revenue By Store
|    | store   |   total_qty |   total_revenue |   pct_qty |   pct_revenue |
|---:|:--------|------------:|----------------:|----------:|--------------:|
|  2 | store3  |        1235 |         13550.6 |  0.202791 |      0.204024 |
|  3 | store4  |        1229 |         13372.5 |  0.201806 |      0.201342 |
|  4 | store5  |        1219 |         13279   |  0.200164 |      0.199935 |
|  0 | store1  |        1209 |         13226.4 |  0.198522 |      0.199143 |
|  1 | store2  |        1198 |         12988.2 |  0.196716 |      0.195556 |

### Total Quantity By Product By Store
|    | store   | product   |   total_qty |       pct |
|---:|:--------|:----------|------------:|----------:|
|  2 | store1  | widget    |         643 | 0.105583  |
|  0 | store1  | gadget    |         489 | 0.0802956 |
|  1 | store1  | tdget     |          77 | 0.0126437 |
|  5 | store2  | widget    |         592 | 0.0972085 |
|  3 | store2  | gadget    |         483 | 0.0793103 |
|  4 | store2  | tdget     |         123 | 0.020197  |
|  8 | store3  | widget    |         632 | 0.103777  |
|  6 | store3  | gadget    |         453 | 0.0743842 |
|  7 | store3  | tdget     |         150 | 0.0246305 |
| 11 | store4  | widget    |         650 | 0.106732  |
|  9 | store4  | gadget    |         458 | 0.0752053 |
| 10 | store4  | tdget     |         121 | 0.0198686 |
| 14 | store5  | widget    |         649 | 0.106568  |
| 12 | store5  | gadget    |         484 | 0.0794745 |
| 13 | store5  | tdget     |          86 | 0.0141215 |


## **|> KPIs by PRODUCT**

### Total Quantity Sold & Revenue By Product
|    | product   |   total_qty |   total_revenue |   pct_qty |   pct_revenue |
|---:|:----------|------------:|----------------:|----------:|--------------:|
|  2 | widget    |        3166 |         34523.9 | 0.519869  |     0.519808  |
|  0 | gadget    |        2367 |         25811.2 | 0.38867   |     0.388625  |
|  1 | tdget     |         557 |          6081.6 | 0.0914614 |     0.0915673 |

### Week-Over-Week (WoW) Total Quantity Sold & Revenue By Store
|    | store   |   total_qty |   total_revenue |   last_week_qty |   last_week_revenue |   WoW_qty |   WoW_revenue |
|---:|:--------|------------:|----------------:|----------------:|--------------------:|----------:|--------------:|
|  0 | store1  |        1209 |         13226.4 |             nan |                 nan |       nan |           nan |
|  1 | store2  |        1198 |         12988.2 |             nan |                 nan |       nan |           nan |
|  2 | store3  |        1235 |         13550.6 |             nan |                 nan |       nan |           nan |
|  3 | store4  |        1229 |         13372.5 |             nan |                 nan |       nan |           nan |
|  4 | store5  |        1219 |         13279   |             nan |                 nan |       nan |           nan |

### Month-Over-Month (MoM) Total Quantity Sold & Revenue By Store
|    | store   |   total_qty |   total_revenue |   last_month_qty |   last_month_revenue |   MoM_qty |   MoM_revenue |
|---:|:--------|------------:|----------------:|-----------------:|---------------------:|----------:|--------------:|
|  0 | store1  |        1209 |         13226.4 |              nan |                  nan |       nan |           nan |
|  1 | store2  |        1198 |         12988.2 |              nan |                  nan |       nan |           nan |
|  2 | store3  |        1235 |         13550.6 |              nan |                  nan |       nan |           nan |
|  3 | store4  |        1229 |         13372.5 |              nan |                  nan |       nan |           nan |
|  4 | store5  |        1219 |         13279   |              nan |                  nan |       nan |           nan |

## Price Optimization
These are the optimized prices for each product by store:
|    |   store |   price | product   |   quantity |   pred_0.025 |   pred_0.5 |   pred_0.975 |   revenue_pred_0.025 |   revenue_pred_0.5 |   revenue_pred_0.975 |   revenue_actual |
|---:|--------:|--------:|:----------|-----------:|-------------:|-----------:|-------------:|---------------------:|-------------------:|---------------------:|-----------------:|
|  0 |       1 |     9.4 | gadget    |         84 |     41.3438  |    59.9815 |      78.4231 |             388.632  |            563.826 |              737.177 |            789.6 |
|  1 |       1 |     9.4 | tdget     |          4 |      3.30205 |    13.2875 |      23.5219 |              31.0393 |            124.902 |              221.106 |             37.6 |
|  2 |       1 |     9.4 | widget    |        108 |     69.6453  |    95.9143 |     106.786  |             654.666  |            901.594 |             1003.79  |           1015.2 |
|  3 |       2 |     9.4 | gadget    |         71 |     48.6888  |    69.5163 |      84.8773 |             457.675  |            653.453 |              797.847 |            667.4 |
|  4 |       2 |     7   | tdget     |         20 |      7.53661 |    18.0206 |      19.6864 |              52.7563 |            126.145 |              137.805 |            140   |
|  5 |       2 |     9.4 | widget    |        114 |     61.8105  |    98.4517 |     137.344  |             581.019  |            925.446 |             1291.04  |           1071.6 |
|  6 |       3 |     9.4 | gadget    |         60 |     39.1881  |    61.1038 |      81.0911 |             368.368  |            574.376 |              762.256 |            564   |
|  7 |       3 |    10   | tdget     |          8 |      8.51375 |    14.5586 |      23.3595 |              85.1375 |            145.586 |              233.595 |             80   |
|  8 |       3 |     9.4 | widget    |        118 |     57.1451  |    89.0863 |     126.596  |             537.164  |            837.411 |             1190.01  |           1109.2 |
|  9 |       4 |     9.4 | gadget    |         98 |     41.3766  |    70.7523 |      95.4298 |             388.94   |            665.072 |              897.04  |            921.2 |
| 10 |       4 |     9.4 | tdget     |         21 |      5.86342 |    17.2178 |      32.3601 |              55.1161 |            161.848 |              304.185 |            197.4 |
| 11 |       4 |     9.4 | widget    |         62 |     62.2681  |    86.7663 |     108.433  |             585.32   |            815.604 |             1019.27  |            582.8 |
| 12 |       5 |     9.4 | gadget    |         45 |     40.3885  |    61.1346 |      79.9481 |             379.652  |            574.666 |              751.512 |            423   |
| 13 |       5 |     9.4 | tdget     |         24 |      4.35141 |    15.184  |      30.4589 |              40.9033 |            142.729 |              286.314 |            225.6 |
| 14 |       5 |     9.4 | widget    |         91 |     46.9648  |    82.5106 |     123.705  |             441.469  |            775.6   |             1162.83  |            855.4 |

## Dashboard
![Mosaic Plot](mosaic.png)
