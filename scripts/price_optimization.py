# Data Wrangling
import pandas as pd
import numpy as np
import duckdb
import os
from plotnine import *

# Price Modeling
from pygam import GAM, ExpectileGAM, s, f

import warnings
warnings.simplefilter('ignore')

def price_optimization():
    
    # Load Data
    df = pd.read_parquet([f for f in os.listdir("./") if f.endswith(".parquet")])
    print(df.columns)

    # Clean and format data

    df['dt'] = df['dt'].apply(lambda x: x[:10])
    df['store'] = df['store'].apply(lambda x: int(x[-1]))
    
    # Aggregate
    df = (df
          .groupby(['store', 'product', 'price', 'dt'])
          .agg({'quantity': 'sum' })
          .reset_index()
    )

# """
    # Get Unique products for price optimization
    unique_prod = df['product'].unique()
    
    # Create an empty dataframe to store results
    all_gam_results = pd.DataFrame()
    
    
    # Loop through stores and products
    for product in unique_prod:
        # Filter for current product
        product_data = df.query('product == @product')

         # Predictors & target split
        X = product_data[['price']]
        y = product_data['quantity']

         # List of quantiles for modeling
        quantiles = [0.025, 0.5, 0.975]
        gam_results = {}

         # Fit the GAM model
        for q in quantiles:
            gam = ExpectileGAM(s(0), expectile=q) # instance the model and smooth tern on price (feature 0)
            gam.fit(X,y) #fit
            gam_results[f'pred_{q}'] = gam.predict(X) #predict for that quantile

         # Store the results in a DF
        predictions_gam = pd.DataFrame(gam_results).set_index(X.index)

         # Concatenate results column-wise with the original data
        predictions_gam_df = pd.concat([product_data[['price', 'product','quantity']], predictions_gam], axis=1)
        
        # Concatenate results row-wise
        all_gam_results = pd.concat([all_gam_results, predictions_gam_df], axis=0)
        

         # Calculate Revenue for each predicted price band
        for col in all_gam_results.columns:
            if col.startswith('pred'):
                all_gam_results['revenue_' + col] = all_gam_results['price'] * all_gam_results[col]

        # Actual revenue
        all_gam_results['revenue_actual'] = all_gam_results['price'] * all_gam_results['quantity']     

    # Calculating where the predicted median revenue is the max
    best_50 = (
        all_gam_results
        .groupby(['product'])
        .apply(lambda x: x[x['revenue_pred_0.5'] == x['revenue_pred_0.5'].max()].head(1))
        .reset_index(drop=True)
        )
    
    # Calculating where the predicted 97.5% percentile revenue is the max
    best_975 = (
        all_gam_results
        .groupby('product')
        .apply(lambda x: x[x['revenue_pred_0.975'] == x['revenue_pred_0.975'].max()].head(1))
        .reset_index(drop=True)
)

    # Calculating where the predicted 2.5% percentile revenue is the max
    best_025 = (
        all_gam_results
        .groupby('product')
        .apply(lambda x: x[x['revenue_pred_0.025'] == x['revenue_pred_0.025'].max()].head(1))
        .reset_index(drop=True)
    )
    
    # Visualize the GAM Optimization Result
    fig = (ggplot(
        # Data
        data = all_gam_results,
        # Axes
        mapping = aes(x='price', y='revenue_pred_0.5', color='product', group='product') ) + 
        # Adding the Band
        geom_ribbon(aes(ymax= 'revenue_pred_0.975', ymin= 'revenue_pred_0.025'), 
                        fill='#d3d3d3', color= '#FF000000', alpha=0.7, show_legend=False) +
        # Adding the points
        geom_point(aes(y='revenue_actual'), alpha=0.15, color="#2C3E50") +
        # Adding 50th percentile line
        geom_line(aes(y='revenue_pred_0.5'), alpha=0.5, color='darkred') +
        # Addimg the 50th pct points
        geom_point(data=best_50, color='red') + 
        # Addimg the 97th pct points
        geom_point(data=best_975, mapping= aes(y='revenue_pred_0.975'), color='blue') + 
        # Addimg the 2.5th pct points
        geom_point(data=best_025, mapping= aes(y='revenue_pred_0.025'), color='blue') + 
        # Wraps by product
        facet_wrap('product', scales='free') + 
        # Labels
        labs(
            title='Price Optimization',
            subtitle='Maximum median revenue (red point) vs 95% Maximum Confidence Interval',
            x= 'Price',
            y= 'Predicted Revenue'
            ) +
        theme(figure_size=(12,7))
    )

    # Save the plot
    fig.save("price_optimization.png")

    # Optimizred price for each product
    return best_50

    # """

# Test
if __name__ == "__main__":
    # Read the current directory for parquet files
    files = [f for f in os.listdir("./") if f.endswith(".parquet")]
    print("\n")
    print(price_optimization())