from math import *
print("Enter first number")
num1 = int(input("-->"))

print("Enter second number")
num2 = int(input("-->"))

result1 = sqrt(num1)
result2 = sqrt(num2)

results  = result1 , result2

print("The results are", result1, "and", result2)
print(f"Largest result is {max(results)}")
