
print("Enter first number")
num1 = int(input("-->"))

print("Enter second number")
num2 = int(input("-->"))

print("Addition")
Addition = num2 + num1

print(f"the sum of the numbers is {Addition}")

print("subtraction")
subtraction = num1 - num2

print(f"the sum of the numbers is {subtraction}")

print("multiplication")
multiplication = num1 * num2

print(f"the sum of the numbers is {multiplication}")

print("division")
division = num1 / num2

print(f"the sum of the numbers is {division}")

results = Addition,subtraction,multiplication,division
smallest_result = min(results)
largest_result = max(results)

print(f"smallest result is {min(results)}")
print(f"largest_result is {max(results)}")


