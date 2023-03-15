import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the data-lidar.csv file, separator = ",", encoding = utf-8
df = pd.read_csv('data-lidar.csv', sep=',', encoding='utf-8')

# Convert the Time column to a datetime object
df['Time'] = pd.to_datetime(df['Time'])

total_time = (df['Time'].iloc[-1] - df['Time'].iloc[0]).total_seconds()
nb_lines = len(df.index)

frequency = total_time / nb_lines
range_ = list(np.arange(0, total_time, frequency))
df['Time'] = range_

frequency_angle = 360 / nb_lines
angle = list(np.arange(0, 360, frequency_angle))
df['Angle'] = angle

print(df)

# Plot the data
# plt.plot(df['Time'], df['Distance'])
# plt.xlabel('Time (s)')
# plt.ylabel('Distance (m)')
# plt.show()

