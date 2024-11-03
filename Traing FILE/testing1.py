# Function to calculate the area of a rectangle
def calculate_area(length, width):
    area = lenght * width  
    return area

# Get length and width from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate and display the area
print("The area of the rectangle is:", calculate_area(length, width))
