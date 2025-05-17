# Imports
import duckdb
import numpy as np
import pandas as pd
import requests
import time

# API URL
API_URL = 'http://localhost:8000/'

# Initialize duckdb
# con = duckdb.connect(database=':memory:', read_only=False)

# Create empty pandas dataframe as placeholder
dtf = pd.DataFrame()

# Function to loop API requests
def extract_data(dtf=dtf):
    # Get data from API
    data = requests.get(f"{API_URL}/get_data", params={'n': 1})

    # Convert to pandas dataframe
    df = pd.DataFrame.from_dict(data.json(), 
                                orient='index', 
                                columns=['date', 'product', 'quantity','price'])

    # Append to dataframe
    dtf = pd.concat([dtf, df])

    return dtf

if __name__ == '__main__':
    # Loop API requests
    while True:
        dtf = extract_data(dtf)
        print(dtf)
        time.sleep(1)