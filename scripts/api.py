# Imports
from fastapi import FastAPI
from numpy import random
from datetime import datetime, timedelta
import time

# Initialize app
app = FastAPI()


# Endpoints

# Root
@app.get("/")
async def root():
    return {"message": "Welcome to the Products API. Try /get_data to generate some fake data."}

# Fake data
@app.get("/get_data")
async def fake_data(n:int=1, days:int=0, hours: int=0):
    """
    Generate fake data for the ETL pipeline.

    Parameters:
    n (int): The number of rows to generate. Defaults to 1.
    days (int): The number of days to offset the date by. Defaults to 0.
    hours (int): The number of hours to offset the date by. Defaults to 0.

    Returns:
    dict: A dictionary with the generated data. The keys are the microsecond timestamps and the values are dictionaries with the keys 'dt', 'store', 'product', 'quantity', and 'price'.
    """
    
    data = {}
    for n in range(n):
        id = datetime.now().microsecond
        data[id] = {
        'dt': datetime.now() + timedelta(days=days, hours=hours),
        'store': random.choice(['store1', 'store2', 'store3', 'store4', 'store5']),
        'product': random.choice(['widget', 'gadget', 'tdget'], p=[0.53, 0.38, 0.09]), 
        'quantity': int(abs(random.randn()))+2,
        # 'quantity': int(random.choice([1,2,3,4,5,6,7,8,9,10], p=[0.18, 0.20, 0.14, 0.16, 0.08, 0.03, 0.1, 0.04, 0.05, 0.02])),
        # 'price': random.choice([10.8, 10.4, 10.5, 11.2, 11.5, 12.], p=[0.15, 0.22, 0.21, 0.19, 0.18, 0.05])
        'price': random.choice([10., 9.4, 9.5, 7., 6.5, 7.3, 7.1, 7.2, 9.8, 7.5], p=[0.05, 0.06, 0.06, 0.19, 0.15, 0.16, 0.18, 0.05, 0.05, 0.05])
            }
        time.sleep(0.001)

    print("API Data generated successfully...")
    
    return data


"""This script is used to create an API endpoint that generate fake data."""