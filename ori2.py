def fibonacci_sequence(last):
    any_number = []
    for i in range(last):
        any_number.append(fibonacci(i))
    return any_number

def fibonacci(last):
    if last == 0:
        return 0
    elif last == 1:
        return 1
    else:
        return fibonacci(last - 1) + fibonacci(last - 2)

try:
    last = int(input("Please enter an number: "))
    if last < 0:
        print("number must be a non-negative integer.")
    else:
        any_number = fibonacci_sequence(last)
        print(any_number)
except ValueError:
    print("Input must be an integer.")





