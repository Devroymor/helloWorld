def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

n = 6  # Defines the number of items in the sequence
sequence = fibonacci_sequence(n)
print(sequence)







