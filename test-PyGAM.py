#Import necessary libraries

import pandas as pd
import numpy as np
from numpy import random
from pygam import GAM, s, f
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


n_obs = 100
# Load the sample dataset (simulated hotel booking data)
data = {
    'day_of_week': random.choice(['Weekday', 'Weekend'], p=[0.7, 0.3], size=n_obs),
    'season': random.choice(['Summer', 'Fall', 'Winter', 'Spring'],p=[0.25, 0.25, 0.25, 0.25], size=n_obs),
    'room_type': random.choice(['Standard', 'Deluxe'], p=[0.7, 0.3], size=n_obs),
    'distance_to_attractions': random.choice([2.5, 1.0, 1.5, 2., 3.0, 0.5], size=n_obs)
}
df = pd.DataFrame(data)

df['price'] = (100 +
               100 * df['season'].apply(lambda x: 0.5 if x == 'Summer' else 0.45 if x == 'Fall' else -1 if x == 'Winter' else -2) + 
               100 * df['room_type'].apply(lambda x: 0 if x == 'Standard' else 0.15) + 
               100 * df['day_of_week'].apply(lambda x: 0 if x == 'Weekday' else 0.25)
               )
df['customer_rating'] = (2 +
                         10 * df['room_type'].apply(lambda x: 0 if x == 'Standard' else 0.25) -
                         (2 - df['distance_to_attractions'])).clip(0, 5)
df['demand'] = (120 + 
                25 * df['season'].apply(lambda x: 0.5 if x == 'Summer' else -0.05)+# if x == 'Winter' else 0) + 
                -100 * df['room_type'].apply(lambda x: 0.15 if x == 'Standard' else 0) + 
                100 * df['day_of_week'].apply(lambda x: 0 if x == 'Weekday' else 0.15) +
                -20 * df['distance_to_attractions']/100 + 
                10 * df['customer_rating']/100 +
                -50 * df['price']/100).astype(int)



# Preprocess the data
categorical_features = ['day_of_week', 'season', 'room_type']
for feature in categorical_features:
    encoder = LabelEncoder()
    df[feature] = encoder.fit_transform(df[feature])

# Summer = 2, Fall = 0, Winter = 3, Spring = 1
# Standard = 1, Deluxe = 0
# Weekday = 0, Weekend = 1

X = df[['day_of_week', 'season', 'room_type', 'distance_to_attractions', 'customer_rating', 'price']]
y = df['demand']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

numerical_features = ['distance_to_attractions', 'customer_rating', 'price']
X_train = X.copy()
scaler = StandardScaler()
X_train[numerical_features] = scaler.fit_transform(X_train[numerical_features])


# Create a GAM model
gam = GAM(f(0) + f(1) + f(2) + s(3) + s(4) + s(5))

# Fit the model to the training data
gam.fit(X_train, y)


# Define a range of possible prices
prices = np.linspace(50, 350, 50)

# Define the conditions for which to predict demand
conditions = {
    'day_of_week': 1,  # Weekday = 0, Weekend = 1
    'season': 2,  # Summer = 2, Fall = 0, Winter = 3, Spring = 1
    'room_type': 1,  # Standard = 1, Deluxe = 0
    'distance_to_attractions': 2.0,
    'customer_rating': 4.0
}

X_pred = pd.DataFrame([conditions] * len(prices))
X_pred['price'] = prices
X_pred = X_pred[['day_of_week', 'season', 'room_type', 'distance_to_attractions', 'customer_rating', 'price']]

X_pred[numerical_features] = scaler.transform(X_pred[numerical_features])

# Predict demand for each price point
predicted_demand = gam.predict(X_pred)

# Calculate the revenue for each price point
revenue = prices * predicted_demand

# Identify the price that maximizes revenue
optimal_price = prices[np.argmax(revenue)]
max_revenue = np.max(revenue)

# Output the results
print(f"Optimal Price: {optimal_price:.2f}")
print(f"Maximum Revenue: {max_revenue:.2f}")



# Visualize the predicted demand curve
fig1 = px.line(x=prices, y=predicted_demand,
              title='Predicted Demand Curve',
              labels={'x': 'Price', 'y': 'Predicted Demand'},
              width=1000, height=600)
fig1.update_traces(line=dict(width=3))
fig1.show()

# Visualize the revenue curve
fig2 = px.line(x=prices, y=revenue, 
              title='Revenue Curve',
              labels={'x': 'Price', 'y': 'Revenue'},
              width=1000, height=600)
px.scatter(x=prices, y=revenue, title='Revenue Curve', labels={'x': 'Price', 'y': 'Revenue'})
fig2.add_trace(go.Scatter(x=[optimal_price], y=[max_revenue], mode='markers', 
                         name='Maximum Revenue', marker=dict(color='red'), line=dict(color='blue')))
fig2.update_traces(line=dict(width=3))

fig2.show()


# Test prices for different seasons
X_pred = pd.DataFrame(columns=X.columns)
optimal_prices = []
max_revenues = []

for season in [0, 1, 2, 3]:
    conditions = {
        'day_of_week': 1,  # Weekday = 0, Weekend = 1
        'season': season,  # Summer = 2, Fall = 0, Winter = 3, Spring = 1
        'room_type': 1,  # Standard = 1, Deluxe = 0
        'distance_to_attractions': 1,
        'customer_rating': 4.0
    }
    X_add = pd.DataFrame([conditions] * len(prices))
    # Define a range of possible prices
    prices = np.linspace(80, 350, 50)
    X_add['price'] = prices
    X_add[numerical_features] = scaler.transform(X_add[numerical_features])
    predicted_demand = gam.predict(X_add)
    X_add['demand'] = predicted_demand
    X_add['price'] = prices
    X_add['revenue'] = prices * predicted_demand
    X_pred = pd.concat([X_pred, X_add])
    
# Revenue predictions
X_pred = X_pred[['day_of_week', 'season', 'room_type', 'distance_to_attractions', 'customer_rating', 'price', 'demand', 'revenue']]


# Visualize the revenue curve
fig3 = px.line(data_frame=X_pred, 
               x='price', y='revenue',
               color='season',
               title='Revenue Curve | Fall = 0, Spring = 1, Summer = 2, Winter = 3',
               labels={'x': 'Price', 'y': 'Revenue'},
               width=1000, height=600)
px.scatter(data_frame=X_pred, x='price', y='revenue', title='Revenue Curve', labels={'x': 'Price', 'y': 'Revenue'})

for season in [0,1,2,3]:
    max_revenue = X_pred.query('season == @season')['revenue'].max()
    optimal_price = X_pred.query('season == @season & revenue == @max_revenue')['price'].values[0]
    fig3.add_trace(go.Scatter(x=[optimal_price], y=[max_revenue], mode='markers', 
                              name=f'Max {season}', marker=dict(color='red')))
fig3.update_traces(line=dict(width=3))
fig3.show()

# Matplotlib
# Visualize the predicted demand curve
plt.figure(figsize=(10, 5))
plt.plot(prices, predicted_demand)
plt.xlabel("Price")
plt.ylabel("Predicted Demand")
plt.title("Predicted Demand Curve")
plt.grid(True)
plt.show()

# Visualize the revenue curve
plt.figure(figsize=(10, 5))
plt.plot(prices, revenue)
plt.xlabel("Price")
plt.ylabel("Revenue")
plt.title("Revenue Curve")
plt.grid(True)
plt.show()