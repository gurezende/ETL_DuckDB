# KPIs REPORT
Attached is the report for the day: **2025-05-23**.

## **|> KPIs by STORE**

### Total Quantity Sold & Revenue By Store
|    | store   |   total_qty |   total_revenue |   pct_qty |   pct_revenue |
|---:|:--------|------------:|----------------:|----------:|--------------:|
|  0 | store1  |         485 |          3704.3 |  0.20344  |      0.204751 |
|  3 | store4  |         489 |          3665.3 |  0.205117 |      0.202596 |
|  2 | store3  |         477 |          3654.8 |  0.200084 |      0.202015 |
|  4 | store5  |         483 |          3646   |  0.202601 |      0.201529 |
|  1 | store2  |         450 |          3421.3 |  0.188758 |      0.189109 |

### Total Quantity By Product By Store
|    | store   | product   |   total_qty |       pct |
|---:|:--------|:----------|------------:|----------:|
|  2 | store1  | widget    |         275 | 0.115352  |
|  0 | store1  | gadget    |         172 | 0.0721477 |
|  1 | store1  | tdget     |          38 | 0.0159396 |
|  5 | store2  | widget    |         239 | 0.100252  |
|  3 | store2  | gadget    |         161 | 0.0675336 |
|  4 | store2  | tdget     |          50 | 0.0209732 |
|  8 | store3  | widget    |         302 | 0.126678  |
|  6 | store3  | gadget    |         138 | 0.0578859 |
|  7 | store3  | tdget     |          37 | 0.0155201 |
| 11 | store4  | widget    |         255 | 0.106963  |
|  9 | store4  | gadget    |         181 | 0.0759228 |
| 10 | store4  | tdget     |          53 | 0.0222315 |
| 14 | store5  | widget    |         297 | 0.124581  |
| 12 | store5  | gadget    |         156 | 0.0654362 |
| 13 | store5  | tdget     |          30 | 0.0125839 |


## **|> KPIs by PRODUCT**

### Total Quantity Sold & Revenue By Product
|    | product   |   total_qty |   total_revenue |   pct_qty |   pct_revenue |
|---:|:----------|------------:|----------------:|----------:|--------------:|
|  2 | widget    |        1368 |         10369.7 | 0.573826  |      0.573174 |
|  0 | gadget    |         808 |          6154.3 | 0.338926  |      0.340173 |
|  1 | tdget     |         208 |          1567.7 | 0.0872483 |      0.086653 |

### Week-Over-Week (WoW) Total Quantity Sold & Revenue By Store
|    | store   |   total_qty |   total_revenue |   last_week_qty |   last_week_revenue |    WoW_qty |   WoW_revenue |
|---:|:--------|------------:|----------------:|----------------:|--------------------:|-----------:|--------------:|
|  4 | store5  |         483 |          3646   |             444 |              3319.8 |  0.0878378 |    0.0982589  |
|  3 | store4  |         489 |          3665.3 |             469 |              3513.1 |  0.0426439 |    0.0433236  |
|  1 | store2  |         450 |          3421.3 |             427 |              3303.6 |  0.0538642 |    0.0356278  |
|  2 | store3  |         477 |          3654.8 |             482 |              3638.9 | -0.0103734 |    0.00436945 |
|  0 | store1  |         485 |          3704.3 |             531 |              3995   | -0.086629  |   -0.072766   |

### Month-Over-Month (MoM) Total Quantity Sold & Revenue By Store
|    | store   |   total_qty |   total_revenue |   last_month_qty |   last_month_revenue |    MoM_qty |   MoM_revenue |
|---:|:--------|------------:|----------------:|-----------------:|---------------------:|-----------:|--------------:|
|  4 | store5  |         483 |          3646   |              434 |               3266   |  0.112903  |    0.11635    |
|  1 | store2  |         450 |          3421.3 |              426 |               3287.5 |  0.056338  |    0.0406996  |
|  0 | store1  |         485 |          3704.3 |              485 |               3673.7 |  0         |    0.00832948 |
|  2 | store3  |         477 |          3654.8 |              499 |               3726.1 | -0.0440882 |   -0.0191353  |
|  3 | store4  |         489 |          3665.3 |              512 |               3897.1 | -0.0449219 |   -0.0594801  |

## Price Optimization
These are the optimized prices for each product by store:
|    |   price | product   |   quantity |   pred_0.025 |   pred_0.5 |   pred_0.975 |   revenue_pred_0.025 |   revenue_pred_0.5 |   revenue_pred_0.975 |   revenue_actual |
|---:|--------:|:----------|-----------:|-------------:|-----------:|-------------:|---------------------:|-------------------:|---------------------:|-----------------:|
|  0 |       7 | gadget    |         27 |     11.7244  |   30.8156  |      42.8507 |              82.0707 |           215.709  |             299.955  |              189 |
|  1 |       7 | tdget     |          5 |      3.46534 |    7.74734 |      13.2021 |              24.2574 |            54.2314 |              92.4146 |               35 |
|  2 |       7 | widget    |         59 |     20.6369  |   48.8549  |      63.4843 |             144.458  |           341.984  |             444.39   |              413 |

## Dashboard
![Attached Plot](mosaic.png)
![Attached Plot Price](price_optimization.png)
