import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
http://127.0.0.1:8000

# Read the data separator : , and encoding : utf-8
data = pd.read_csv('sensorAccelerationDT.csv', sep=',', encoding='utf-8')

# Convert the dateTime column to a datetime object
data['dateTime'] = pd.to_datetime(data['dateTime'])

# Calculate the duration of the movement
total_time = (data['dateTime'].iloc[-1] - data['dateTime'].iloc[0]).total_seconds()
print(total_time)

# Crée une figure de 2 x 2
fig, axs = plt.subplots(2, 2)

# Print X, Y, Z columns with drift and gravity
axs[0, 0].plot(data['dateTime'], data['X'], label='x')
axs[0, 0].plot(data['dateTime'], data['Y'], label='y')
axs[0, 0].plot(data['dateTime'], data['Z'], label='z')
axs[0, 0].legend()

# Calculate the median of the X, Y, Z columns for the last 20 values
median_x = data['X'].iloc[-20:].median()
median_y = data['Y'].iloc[-20:].median()
median_z = data['Z'].iloc[-20:].median()

# Subtract the median from the X, Y, Z columns to remove the gravity and drift
data['X'] = data['X'] - median_x
data['Y'] = data['Y'] - median_y
data['Z'] = data['Z'] - median_z

# Print X, Y, Z columns
axs[0, 1].plot(data['dateTime'], data['X'], label='x')
axs[0, 1].plot(data['dateTime'], data['Y'], label='y')
axs[0, 1].plot(data['dateTime'], data['Z'], label='z')
axs[0, 1].legend()

# print the graph
plt.show()