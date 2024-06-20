def sum_of_natural_numbers(N):
    return N * (N + 1) / 2

N = int(input("Enter a positive integer N: "))
if N > 0:
    total_sum = sum_of_natural_numbers(N)
    print(f"The sum of the first {N} natural numbers is {total_sum}.")
else:
    print("Please enter a positive integer.")
