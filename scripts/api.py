# Imports
from fastapi import FastAPI
from numpy import random
from datetime import datetime
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
async def fake_data(n:int=1):
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
        'date': datetime.now(),
        'product': random.choice(['widget', 'gadget', 'tdget']), 
        'quantity': random.randint(1, 10),
        'price': random.choice([10.8, 10.4, 10.5, 11.20, 11.5, 12.])
            }
        time.sleep(0.001)
    return data