# KPIs REPORT
Attached is the report for the day: **2025-05-28**.

## **|> KPIs by STORE**

### Total Quantity Sold & Revenue By Store
|    | store   |   total_qty |   total_revenue |   pct_qty |   pct_revenue |
|---:|:--------|------------:|----------------:|----------:|--------------:|
|  1 | store2  |         564 |          4252.6 |  0.237374 |      0.235882 |
|  4 | store5  |         480 |          3655.9 |  0.20202  |      0.202784 |
|  2 | store3  |         478 |          3634.1 |  0.201178 |      0.201575 |
|  3 | store4  |         440 |          3356.7 |  0.185185 |      0.186189 |
|  0 | store1  |         414 |          3129.2 |  0.174242 |      0.17357  |

### Total Quantity By Product By Store
|    | store   | product   |   total_qty |        pct |
|---:|:--------|:----------|------------:|-----------:|
|  2 | store1  | widget    |         219 | 0.0921717  |
|  0 | store1  | gadget    |         178 | 0.0749158  |
|  1 | store1  | tdget     |          17 | 0.00715488 |
|  5 | store2  | widget    |         283 | 0.119108   |
|  3 | store2  | gadget    |         241 | 0.101431   |
|  4 | store2  | tdget     |          40 | 0.016835   |
|  8 | store3  | widget    |         271 | 0.114057   |
|  6 | store3  | gadget    |         168 | 0.0707071  |
|  7 | store3  | tdget     |          39 | 0.0164141  |
| 11 | store4  | widget    |         228 | 0.0959596  |
|  9 | store4  | gadget    |         160 | 0.0673401  |
| 10 | store4  | tdget     |          52 | 0.0218855  |
| 14 | store5  | widget    |         277 | 0.116582   |
| 12 | store5  | gadget    |         158 | 0.0664983  |
| 13 | store5  | tdget     |          45 | 0.0189394  |


## **|> KPIs by PRODUCT**

### Total Quantity Sold & Revenue By Product
|    | product   |   total_qty |   total_revenue |   pct_qty |   pct_revenue |
|---:|:----------|------------:|----------------:|----------:|--------------:|
|  2 | widget    |        1278 |          9674.6 |  0.537879 |     0.536628  |
|  0 | gadget    |         905 |          6897.2 |  0.380892 |     0.382572  |
|  1 | tdget     |         193 |          1456.7 |  0.081229 |     0.0807998 |

### Week-Over-Week (WoW) Total Quantity Sold & Revenue By Store
|    | store   |   total_qty |   total_revenue |   last_week_qty |   last_week_revenue |    WoW_qty |   WoW_revenue |
|---:|:--------|------------:|----------------:|----------------:|--------------------:|-----------:|--------------:|
|  1 | store2  |         564 |          4252.6 |             494 |              3750.5 |  0.1417    |    0.133875   |
|  2 | store3  |         478 |          3634.1 |             437 |              3361   |  0.0938215 |    0.0812556  |
|  0 | store1  |         414 |          3129.2 |             410 |              3101.3 |  0.0097561 |    0.00899623 |
|  4 | store5  |         480 |          3655.9 |             522 |              3980   | -0.0804598 |   -0.0814322  |
|  3 | store4  |         440 |          3356.7 |             499 |              3798.8 | -0.118236  |   -0.116379   |

### Month-Over-Month (MoM) Total Quantity Sold & Revenue By Store
|    | store   |   total_qty |   total_revenue |   last_month_qty |   last_month_revenue |     MoM_qty |   MoM_revenue |
|---:|:--------|------------:|----------------:|-----------------:|---------------------:|------------:|--------------:|
|  1 | store2  |         564 |          4252.6 |              454 |               3423.3 |  0.242291   |    0.242252   |
|  3 | store4  |         440 |          3356.7 |              424 |               3282.1 |  0.0377358  |    0.0227294  |
|  4 | store5  |         480 |          3655.9 |              482 |               3688.3 | -0.00414938 |   -0.00878453 |
|  2 | store3  |         478 |          3634.1 |              486 |               3681.8 | -0.0164609  |   -0.0129556  |
|  0 | store1  |         414 |          3129.2 |              506 |               3873.7 | -0.181818   |   -0.192194   |

## Price Optimization
These are the optimized prices for each product by store:
|    |   price | product   |   quantity |   pred_0.025 |   pred_0.5 |   pred_0.975 |   revenue_pred_0.025 |   revenue_pred_0.5 |   revenue_pred_0.975 |   revenue_actual |
|---:|--------:|:----------|-----------:|-------------:|-----------:|-------------:|---------------------:|-------------------:|---------------------:|-----------------:|
|  0 |       7 | gadget    |         46 |     16.1752  |    31.4279 |      45.7003 |             113.226  |           219.995  |             319.902  |              322 |
|  1 |       7 | tdget     |          6 |      3.28663 |     7.8613 |      12.7895 |              23.0064 |            55.0291 |              89.5264 |               42 |
|  2 |       7 | widget    |         34 |     20.3654  |    44.0708 |      61.1326 |             142.558  |           308.496  |             427.928  |              238 |

## Dashboard
![Attached Plot](mosaic.png)
![Attached Plot Price](price_optimization.png)
