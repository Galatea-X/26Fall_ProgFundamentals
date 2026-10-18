# Assignment 2: Moving Average and Temperature Status
temp1 = 21.5
temp2 = 22.0
temp3 = 23.1
temp4 = 24.8
temp5 = 25.2

hum1 = 48.0
hum2 = 50.5
hum3 = 52.0
hum4 = 49.5
hum5 = 51.0

# Calculate the moving average for temperature
# (simple average of the five readings)
temp_sum = temp1 + temp2 + temp3 + temp4 + temp5
temp_average = temp_sum / 5

# Calculate the moving average for humidity
hum_sum = hum1 + hum2 + hum3 + hum4 + hum5
hum_average = hum_sum / 5

# Display the moving averages
print("Moving Average Temperature:", temp_average, "°C")
print("Moving Average Humidity:", hum_average, "%")
print()   # blank line for readability

# Define the normal temperature range (common room values)
# Normal range used here: 20.0 °C to 25.0 °C
normal_low = 20.0
normal_high = 25.0

# Boolean checks for the temperature range
is_normal = (temp_average >= normal_low) and (temp_average <= normal_high)
is_high = temp_average > normal_high
is_low = temp_average < normal_low

# Print the correct temperature status message
if is_normal:
    print("The temperature is normal")
elif is_high:
    print("The temperature is high")
elif is_low:
    print("The temperature is low")
