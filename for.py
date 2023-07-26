def is_factor(number, potential_factor):
    return number % potential_factor == 0


def find_factors(num):
    print(f"The factors of {num} are:")

    potential_factor = 1
    while potential_factor <= num:
        if is_factor(num, potential_factor):
            print(potential_factor)
        potential_factor += 1


num = 24
find_factors(num)