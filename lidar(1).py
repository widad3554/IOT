import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

# Read the data-lidar.csv file, separator = ",", encoding = utf-8
df = pd.read_csv('data-lidar.csv', sep=',', encoding='utf-8')

# delete the 110 first lines because the data is overlapping
df = df[110:]

# Convert the Time column to a datetime object
df['Time'] = pd.to_datetime(df['Time'])

# Calculate the time considering a continuous movement
total_time = (df['Time'].iloc[-1] - df['Time'].iloc[0]).total_seconds()
nb_lines = len(df.index)
frequency = total_time / nb_lines
range_ = list(np.arange(0, total_time, frequency))
df['Time'] = range_

# Calculate the angle considering a continuous movement
frequency_angle = 360 / nb_lines
angle = list(np.arange(0, 360, frequency_angle))
df['Angle'] = angle

# Plot the data (Time, Distance)
plt.plot(df['Time'], df['Distance'])
plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.show()

# convert angle, distance to x, y
df['X'] = df['Distance'] * np.cos(df['Angle'] * np.pi / 180)
df['Y'] = df['Distance'] * np.sin(df['Angle'] * np.pi / 180)

# Plot the data
plt.plot(df['X'], df['Y'])
plt.xlabel('X (cm)')
plt.ylabel('Y (cm)')
plt.show()

# calculate the surface
tab_y = df['Y'].tolist()
tab_x = df['X'].tolist()
poly = Polygon(zip(tab_x, tab_y))

# print the surface in cm2
print(str(poly.area) + " cm2")
# conversion cm2 to m2
print(str(poly.area / 10000) + " m2")
