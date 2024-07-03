import pandas as pd
import numpy as np
import datetime
import random

# Function to generate random dates
def generate_random_dates(start_date, end_date, n):
    start_u = start_date.value//10**9
    end_u = end_date.value//10**9
    return pd.to_datetime(np.random.randint(start_u, end_u, n), unit='s')

# Parameters
num_samples = 1000  # Number of samples
start_date = pd.to_datetime('2023-01-01')
end_date = pd.to_datetime('2023-12-31')

# Generate random dates
dates = generate_random_dates(start_date, end_date, num_samples)

# Generate random data
data = {
    'timestamp': dates,
    'current_supply': np.random.uniform(low=1000, high=5000, size=num_samples),  # in MW
    'current_demand': np.random.uniform(low=800, high=4500, size=num_samples),  # in MW
    'historical_price': np.random.uniform(low=0.1, high=0.5, size=num_samples)  # in MYR/kWh
}

# Create DataFrame
df = pd.DataFrame(data)
df['price'] = df.apply(lambda row: row['historical_price'] * (1 + (row['current_demand'] - row['current_supply']) / 10000), axis=1)

# Save to CSV
df.to_csv('malaysia_energy_data.csv', index=False)

print("Dummy data created and saved to 'malaysia_energy_data.csv'")
