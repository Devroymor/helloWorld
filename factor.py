def find_factors(number):
    """
    Find factors of a given number.

    Args:
    number (int): The number to find the factors of.

    Returns:
    list: A list of factors of the number.
    """
    factors = []
    i = 1

    while i <= number:
        if number % i == 0:
            factors.append(i)
        i += 1

    return factors

def main():
    num = int(input("Enter a number to find its factors: "))
    factors = find_factors(num)
    print(f"The factors of {num} are: {factors}")

if __name__ == "__main__":
    main()