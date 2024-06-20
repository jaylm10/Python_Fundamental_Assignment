def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

terms = int(input("Enter the number of terms: "))
if terms > 0:
    fibonacci_sequence = generate_fibonacci(terms)
    print(f"The first {terms} terms of the Fibonacci sequence are: {fibonacci_sequence}")
else:
    print("Please enter a positive integer.")
