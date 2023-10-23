# Simple Python Project: Calculate the Area of a Rectangle

# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Input: Length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangl: "))

# Calculate the area
area = calculate_rectangle_area(length, width)

# Output: Display the calculated area
print(f"The area of the rectangle with length {length} and width {width} is {area}.")
