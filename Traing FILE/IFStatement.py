a = 200
b = 60
c = 500
if a > b and c > a:
    print("Both conditions are True")



a = 10
b = 33
c = 200
if a > b and c > a:
  print("Both conditions are True")



a = 500
b = 330
print("A") if a > b else print("=") if a == b else print("B")


a = 15
b = 500
print("A") if a > b else print("B")


age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


    # Using break and continue in a loop
for number in range(1, 11):
    if number == 5:
        print("Found 5, breaking the loop.")
        break  # Exit the loop when the number is 5
    if number % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {number}")
    