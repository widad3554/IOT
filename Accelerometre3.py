import pandas as pd
import matplotlib.pyplot as plt

# Read the data separator : , and encoding : utf-8
data = pd.read_csv('sensorAccelerationDT3.csv', sep=';', encoding='utf-8')

# Calculate the duration of the movement
data['time'] = [float(i.replace(',', '.')) for i in data['time']]
duration = data['time'].iloc[-1] - data['time'].iloc[0]
print('Duration of the movement : ', duration, 's')

# rename the columns
data.columns = ['time', 'X', 'Y', 'Z', 'Total']

# Convert the X, Y, Z, Total columns to float
data['X'] = [float(i.replace(',', '.')) for i in data['X']]
data['Y'] = [float(i.replace(',', '.')) for i in data['Y']]
data['Z'] = [float(i.replace(',', '.')) for i in data['Z']]
data['Total'] = [float(i.replace(',', '.')) for i in data['Total']]

print(data)

# Create a figure with 2 rows and 2 columns
fig, axs = plt.subplots(2, 2)

# Print X, Y, Z columns in the first graph
axs[0, 0].plot(data['time'], data['X'], 'r')
axs[0, 0].plot(data['time'], data['Y'], 'g')
axs[0, 0].plot(data['time'], data['Z'], 'b')
axs[0, 0].legend(['X', 'Y', 'Z'])

# prepare the data for the 3D graph
data['X'] = data['X'] - data['X'].mean()
data['Y'] = data['Y'] - data['Y'].mean()
data['Z'] = data['Z'] - data['Z'].mean()

# Print the X, Y, Z columns in the second graph
axs[0, 1].plot(data['time'], data['X'], 'r')
axs[0, 1].plot(data['time'], data['Y'], 'g')
axs[0, 1].plot(data['time'], data['Z'], 'b')
axs[0, 1].legend(['X', 'Y', 'Z'])

# Calculate the speed of the movement from acceleration data X_speed, Y_speed, Z_speed
data['X_speed'] = data['X'].cumsum() / duration
data['Y_speed'] = data['Y'].cumsum() / duration
data['Z_speed'] = data['Z'].cumsum() / duration

# Print the X_speed, Y_speed, Z_speed columns in the third graph
axs[1, 0].plot(data['time'], data['X_speed'], 'r')
axs[1, 0].plot(data['time'], data['Y_speed'], 'g')
axs[1, 0].plot(data['time'], data['Z_speed'], 'b')
axs[1, 0].legend(['X_speed', 'Y_speed', 'Z_speed'])

# Calculate the position of the movement from speed data X_position, Y_position, Z_position
data['X_position'] = data['X_speed'].cumsum() / duration
data['Y_position'] = data['Y_speed'].cumsum() / duration
data['Z_position'] = data['Z_speed'].cumsum() / duration

# Print the X_position, Y_position, Z_position columns in the fourth graph
axs[1, 1].plot(data['time'], data['X_position'], 'r')
axs[1, 1].plot(data['time'], data['Y_position'], 'g')
axs[1, 1].plot(data['time'], data['Z_position'], 'b')
axs[1, 1].legend(['X_position', 'Y_position', 'Z_position'])
plt.show()

# print the 3D graph of the movement
fig2 = plt.figure()
ax = fig2.add_subplot(111, projection='3d')
ax.plot(data['X_position'], data['Y_position'], data['Z_position'])
# add point for the start and the end of the movement
ax.scatter(data['X_position'].iloc[0], data['Y_position'].iloc[0], data['Z_position'].iloc[0], c='r', marker='o')
ax.scatter(data['X_position'].iloc[-1], data['Y_position'].iloc[-1], data['Z_position'].iloc[-1], c='g', marker='o')
plt.show()




