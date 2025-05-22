# KPIs REPORT
Attached is the report for the day: **2025-05-22**.

## **|> KPIs by STORE**

### Total Quantity Sold & Revenue By Store
|    | store   |   total_qty |   total_revenue |   pct_qty |   pct_revenue |
|---:|:--------|------------:|----------------:|----------:|--------------:|
|  2 | store3  |         449 |          3372.9 |  0.232402 |      0.229114 |
|  4 | store5  |         402 |          3074.8 |  0.208075 |      0.208865 |
|  0 | store1  |         363 |          2836.3 |  0.187888 |      0.192664 |
|  3 | store4  |         362 |          2729.4 |  0.187371 |      0.185402 |
|  1 | store2  |         356 |          2708.1 |  0.184265 |      0.183955 |

### Total Quantity By Product By Store
|    | store   | product   |   total_qty |        pct |
|---:|:--------|:----------|------------:|-----------:|
|  2 | store1  | widget    |         208 | 0.10766    |
|  0 | store1  | gadget    |         126 | 0.0652174  |
|  1 | store1  | tdget     |          29 | 0.0150104  |
|  5 | store2  | widget    |         225 | 0.11646    |
|  3 | store2  | gadget    |          82 | 0.0424431  |
|  4 | store2  | tdget     |          49 | 0.0253623  |
|  8 | store3  | widget    |         252 | 0.130435   |
|  6 | store3  | gadget    |         151 | 0.0781573  |
|  7 | store3  | tdget     |          46 | 0.0238095  |
| 11 | store4  | widget    |         179 | 0.0926501  |
|  9 | store4  | gadget    |         139 | 0.0719462  |
| 10 | store4  | tdget     |          44 | 0.0227743  |
| 14 | store5  | widget    |         225 | 0.11646    |
| 12 | store5  | gadget    |         161 | 0.0833333  |
| 13 | store5  | tdget     |          16 | 0.00828157 |


## **|> KPIs by PRODUCT**

### Total Quantity Sold & Revenue By Product
|    | product   |   total_qty |   total_revenue |   pct_qty |   pct_revenue |
|---:|:----------|------------:|----------------:|----------:|--------------:|
|  2 | widget    |        1089 |          8313.2 | 0.563665  |      0.564698 |
|  0 | gadget    |         659 |          5000.1 | 0.341097  |      0.339646 |
|  1 | tdget     |         184 |          1408.2 | 0.0952381 |      0.095656 |

### Week-Over-Week (WoW) Total Quantity Sold & Revenue By Store
|    | store   |   total_qty |   total_revenue |   last_week_qty |   last_week_revenue |    WoW_qty |   WoW_revenue |
|---:|:--------|------------:|----------------:|----------------:|--------------------:|-----------:|--------------:|
|  2 | store3  |         449 |          3372.9 |             390 |              2951.3 |  0.151282  |     0.142852  |
|  0 | store1  |         363 |          2836.3 |             334 |              2514.8 |  0.0868263 |     0.127843  |
|  4 | store5  |         402 |          3074.8 |             374 |              2802   |  0.0748663 |     0.097359  |
|  3 | store4  |         362 |          2729.4 |             344 |              2682.3 |  0.0523256 |     0.0175596 |
|  1 | store2  |         356 |          2708.1 |             426 |              3241.7 | -0.164319  |    -0.164605  |

### Month-Over-Month (MoM) Total Quantity Sold & Revenue By Store
|    | store   |   total_qty |   total_revenue |   last_month_qty |   last_month_revenue |    MoM_qty |   MoM_revenue |
|---:|:--------|------------:|----------------:|-----------------:|---------------------:|-----------:|--------------:|
|  2 | store3  |         449 |          3372.9 |              357 |               2737.4 |  0.257703  |     0.232155  |
|  4 | store5  |         402 |          3074.8 |              366 |               2776.8 |  0.0983607 |     0.107318  |
|  0 | store1  |         363 |          2836.3 |              356 |               2707.5 |  0.0196629 |     0.0475716 |
|  1 | store2  |         356 |          2708.1 |              388 |               2963.6 | -0.0824742 |    -0.0862127 |
|  3 | store4  |         362 |          2729.4 |              423 |               3181.3 | -0.144208  |    -0.142049  |

## Price Optimization
These are the optimized prices for each product by store:
|    |   price | product   |   quantity |   pred_0.025 |   pred_0.5 |   pred_0.975 |   revenue_pred_0.025 |   revenue_pred_0.5 |   revenue_pred_0.975 |   revenue_actual |
|---:|--------:|:----------|-----------:|-------------:|-----------:|-------------:|---------------------:|-------------------:|---------------------:|-----------------:|
|  0 |     7   | gadget    |          8 |      3.34535 |    8.84661 |      14.6118 |              23.4174 |            61.9262 |             102.282  |             56   |
|  1 |     7.5 | tdget     |          7 |      2.4899  |    6.15548 |      10.2572 |              18.6742 |            46.1661 |              76.9289 |             52.5 |
|  2 |     7   | widget    |          6 |      5.59017 |   13.5041  |      23.2233 |              39.1312 |            94.5289 |             162.563  |             42   |

## Dashboard
![Attached Plot](mosaic.png)
