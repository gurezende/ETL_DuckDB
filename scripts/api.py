# Imports
from fastapi import FastAPI
from numpy import random
from datetime import datetime
import time

# Initialize app
app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Welcome to the Products API. Try /get_data to generate some fake data."}

@app.get("/get_data")
async def fake_data(n:int=1):
    data = {}
    for n in range(n):
        id = datetime.now().microsecond
        data[id] = { 
        'date': datetime.now(),
        'product': random.choice(['widget', 'gadget', 'tdget']), 
        'price': random.choice([10.8, 10.4, 10.5, 11.20, 11.5, 12.]), 
        'quantity': random.randint(1, 10)
            }
        time.sleep(0.001)
    return data