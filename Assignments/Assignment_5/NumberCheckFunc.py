def check_number(num):
    # Check if the number is even or odd
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
# Ask the user for a whole number
number = int(input("Enter a whole number: "))
# Call the function and display the result
result = check_number(number)
# Display the result
print(f"{number} is an {result} number.")