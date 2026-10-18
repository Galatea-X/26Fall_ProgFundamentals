# Module 4 Assignment - Temperature & Humidity Menu

# Function that reads and displays the temperature
def read_temperature():
    # Sensor data is read ONLY when this function is called
    temperature = 22.5          # Placeholder for actual sensor reading
    print("Temperature:", temperature, "°C")

# Function that reads and displays the humidity
def read_humidity():
    # Sensor data is read ONLY when this function is called
    humidity = 55.0             # Placeholder for actual sensor reading
    print("Humidity:", humidity, "%")
# Main program

# Display the menu once when the program starts
print("Please choose from the following options:")
print("T - Temperature")
print("H - Humidity")
print("0 - Both")

# Continuously wait for a valid choice from the user
while True:
    # Get the user's input (strip spaces and convert to uppercase)
    choice = input("Enter your choice: ").strip().upper()

    # Check the user's choice and call the correct function(s)
    if choice == "T":
        # Call the temperature function only when the user chooses T
        read_temperature()
        break                   # Exit the loop after a valid choice

    elif choice == "H":
        # Call the humidity function only when the user chooses H
        read_humidity()
        break                   # Exit the loop after a valid choice

    elif choice == "0":
        # Call both functions when the user chooses 0
        read_temperature()
        read_humidity()
        break                   # Exit the loop after a valid choice

    else:
        # Invalid input – keep asking until a valid choice is entered
        print("Invalid choice. Please enter T, H, or 0.")
