# Rectangle Calculator Function
def rectangle_stats(length, width):
    perimeter = 2 * (length + width)
    area = length * width
    return perimeter, area
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
perimeter, area = rectangle_stats(length, width)
# Display the results
print(f"Perimeter: {perimeter:.2f}")
print(f"Area: {area:.2f}")