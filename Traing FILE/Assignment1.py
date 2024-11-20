# Example 11: Chained Comparison Mistake
# Incorrect: Using separate comparisons instead of chaining.
x = 5
if 3 < x < 10:  # Chained comparison
    print("x is between 3 and 10")

# Example 12: Exponentiation Operator Misuse
# Incorrect: Using * instead of ** for exponentiation.
base = 3
exponent = 4
result = base ** exponent  # Use ** for exponentiation
print("3 to the power of 4 is:", result)

# Example 13: List Concatenation Mistake
# Incorrect: Using + to combine lists and integers.
numbers = [1, 2, 3]
new_numbers = numbers + [4]  # Concatenate a list with a list
print(new_numbers)



# Example 14: Division by Zero Mistake
# Incorrect: Forgetting to handle zero in the denominator.
a = 10
b = 0

try:
    result = a / b
    print("Result is:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


# Example 15: Assignment in an If Condition Mistake
# Incorrect: Using assignment (=) instead of comparison (==).
x = 10
if x == 5:  # Comparison, not assignment
    print("x is 5")


# Example 16: Augmented Assignment Operator Mistake
# Incorrect: Forgetting the correct symbol for minus equals (-=).
total = 100
discount = 10
total -= discount  # Correct use of the augmented assignment operator
print("Total after discount:", total)

# Example 17: Membership Operator Mistake
# Incorrect: Using "in" for direct comparison instead of membership.
my_list = [1, 2, 3]
if 2 in my_list:  # This checks if 2 is in the list directly
    print("2 is in the list")

# Example 18: Logical Operator Precedence Mistake
# Incorrect: Not using parentheses to clarify order of operations.
x = 5
y = 0
if x > 0 or (y != 0 and x < 10):  # Add parentheses to clarify precedence
    print("Condition met")


# Example 19: Concatenation of Non-String Types
# Incorrect: Trying to concatenate a non-string without conversion.
greeting = "Hello, "
name = 1234
print(greeting + str(name))  # Convert the integer to a string

# Example 20: Using Logical Operators with Non-Boolean Values
# Incorrect: Assuming "and" returns a boolean.
value = 10
result = bool(value and 20)  # Converts the result of the and operation to a boolean
print("Result is:", result)
