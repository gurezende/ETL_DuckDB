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
def extract_data(dtf=dtf, days:list=[0], hours:list=[0], n=1000):

    # For each day in this list
    for d in days:
        # And for each hour in this list
        for h in hours:
            # Get data from API
            data = requests.get(f"{API_URL}/get_data", params={'n': n, 'days': d, 'hours': h})	

            # Convert to pandas dataframe
            df = pd.DataFrame.from_dict(data.json(), 
                                        orient='index', 
                                        columns=['store', 'product', 'quantity','price', 'dt'])

            # Append to db
            dtf = pd.concat([dtf, df])

            print(f"{dtf['product'].count()} new rows generated...")
            time.sleep(3)
    
        # Get date
        date_today = ((datetime.now() + timedelta(days=d))).strftime('%Y_%m_%d')

        # Save to csv
        dtf.to_parquet(f'apidata{date_today}.parquet', engine='pyarrow', index=False)
        print(f"Data saved to apidata{date_today}.parquet")

        # Clear dataframe for next day loop
        dtf = pd.DataFrame()


# Test
if __name__ == '__main__':

    extract_data(days=[0,-7,-30],n=5)



"""This script is used to extract data from the API and save it to a parquet file."""