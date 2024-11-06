# Example 1: Division Operator Mistake
result = 5 / 2
print("Result of 5 / 2 is:", result)




# Example 2: Concatenation Operator Mistake
age = 25
message = "Your age is " + str(age)
print(message)



# Example 3: Comparison Operator Mistake
num = 10
if num == 10:
    print("Number is 10")




# Example 4: Logical Operator Mistake
x = 5
y = 10
if x > 0 or y < 15:
    print("Condition met: x is positive or y is less than 15")


# Example 5: Exponentiation Operator Mistake
value = 4 * 3
print("Value of 4 * 3 is:", value)




# Example 6: Modulus Operator Mistake
# Incorrect: Using / instead of % to check if a number is even.
number = 10
if number % 2 == 0:
    print("Number is even")

# Example 7: Logical NOT Operator Mistake
# Incorrect: Using "not" inappropriately with a comparison.

is_logged_in = False
if not is_logged_in:
    print("User is not logged in")
else:
    print("User is logged in")


# Example 8: Bitwise Operator Mistake
# Incorrect: Using & (bitwise AND) instead of and (logical AND).
a = 5
b = 10
if a > 0 and b < 15:
    print("Condition met")

    
# Example 9: Increment Operator Mistake
# Incorrect: Trying to use ++ (not valid in Python).
counter = 0
counter += 1
print("Counter is:", counter)

# Example 10: Assignment Operator Mistake
# Incorrect: Trying to use the compound assignment operator with a string and integer.
text = "Score: "
score = 10
text += str(score)
print(text)
