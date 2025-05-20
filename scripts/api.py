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
    Generate a dictionary of fake product data for a specified number of entries.

    Args:
        n (int): The number of fake data entries to generate. Defaults to 1.

    Returns:
        dict: A dictionary where each key is a unique ID and each value is a 
        dictionary containing 'date', 'product', 'price', and 'quantity' keys 
        with randomly generated values.
    """

    data = {}
    for n in range(n):
        id = datetime.now().microsecond
        data[id] = {
        'date': datetime.now() + timedelta(days=days, hours=hours),
        'store': random.choice(['store1', 'store2', 'store3', 'store4', 'store5']),
        'product': random.choice(['widget', 'gadget', 'tdget'], p=[0.53, 0.38, 0.09]), 
        'quantity': int(random.choice([1,2,3,4,5,6,7,8,9,10], p=[0.23, 0.26, 0.14, 0.16, 0.08, 0.03, 0.06, 0.02, 0.01, 0.01])),
        # 'quantity': random.randint(1,10),
        'price': random.choice([10.8, 10.4, 10.5, 11.2, 11.5, 12.], p=[0.15, 0.22, 0.21, 0.19, 0.18, 0.05])
            }
        time.sleep(0.001)

    print("API Data generated successfully...")
    
    return data