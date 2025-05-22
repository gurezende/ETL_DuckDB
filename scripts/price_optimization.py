# Data Wrangling
import pandas as pd
import numpy as np
import duckdb
import os

# Price Modeling
from pygam import GAM, ExpectileGAM, s

import warnings
warnings.simplefilter('ignore')

def price_optimization(files=[f for f in os.listdir("./") if f.endswith(".parquet")]):
    
    # Load Data
    df = pd.read_parquet(files)

    # Clean and format data
    df['date'] = pd.to_datetime(df['date']).dt.date
    df['store'] = df['store'].apply(lambda x: int(x[-1]))

    # Aggregate
    df = (df
          .groupby(['store', 'product', 'price', 'date'])
          .agg({'quantity': 'sum' })
          .reset_index()
    )
    
# """
    # Get Unique products for price optimization
    unique_prod = df['product'].unique()
    unique_stores = df['store'].unique()
    
    # Create an empty dataframe to store results
    all_gam_results = pd.DataFrame()
    
    
    # Loop through stores and products
    for store in unique_stores:
        for product in unique_prod:
            # Filter for current product
            product_data = df.query('store == @store & product == @product')

            # Predictors & target split
            X = product_data[['price']]
            y = product_data['quantity']

            # List of quantiles for modeling
            quantiles = [0.025, 0.5, 0.975]
            gam_results = {}

            # Fit the GAM model
            for q in quantiles:
                gam = ExpectileGAM(s(0), expectile=q) # instance the model
                gam.fit(X,y) #fit
                gam_results[f'pred_{q}'] = gam.predict(X) #predict for that quantile

            # Store the results in a DF
            predictions_gam = pd.DataFrame(gam_results).set_index(X.index)

            # Concatenate results column-wise with the original data
            predictions_gam_df = pd.concat([product_data[['store','price', 'product','quantity']], predictions_gam], axis=1)
            
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
        .groupby(['store','product'])
        .apply(lambda x: x[x['revenue_pred_0.5'] == x['revenue_pred_0.5'].max()].head(1))
        .reset_index(drop=True)
        )
    
    # Optimizred price for each product
    return best_50

    # """

# Test
if __name__ == "__main__":
    # Read the current directory for parquet files
    files = [f for f in os.listdir("./") if f.endswith(".parquet")]
    print("\n")
    print(price_optimization(files))