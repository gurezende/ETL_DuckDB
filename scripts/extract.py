# Imports
import numpy as np
import pandas as pd
import requests
import time
from datetime import datetime, timedelta

# API URL
API_URL = 'http://localhost:8000/'

# Create empty pandas dataframe as placeholder
dtf = pd.DataFrame()

# Function to loop API requests
def extract_data(dtf=dtf, days=0, hours=0):
    # Get data from API
    data = requests.get(f"{API_URL}/get_data", params={'n': 1000, 'days': days, 'hours': hours})	

    # Convert to pandas dataframe
    df = pd.DataFrame.from_dict(data.json(), 
                                orient='index', 
                                columns=['date', 'store', 'product', 'quantity','price'])

    # Append to db
    dtf = pd.concat([dtf, df])

    return dtf

if __name__ == '__main__':

    # Loop API requests
    # For each day in this list
    for d in [3]:
        # And for each hour in this list
        for h in [0,1]:
            # Extract data from API
            dtf = extract_data(dtf, days=d, hours=h)
            print(dtf['product'].count())
            time.sleep(3)
    
        # Get date
        date_today = ((datetime.now() + timedelta(days=d))).strftime('%Y_%m_%d')

        # Save to csv
        dtf.to_parquet(f'apidata{date_today}.parquet', engine='pyarrow', index=False)
        print(f"Data saved to apidata{date_today}.parquet")

        # Clear dataframe for next day loop
        dtf = pd.DataFrame()



"""This script is used to extract data from the API and save it to a parquet file."""