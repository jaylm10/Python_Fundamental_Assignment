def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n = n // 10
    return sum_digits

number = int(input("Enter a positive integer: "))
if number >= 0:
    total_sum = sum_of_digits(number)
    print(f"The sum of the digits of {number} is {total_sum}.")
else:
    print("Please enter a non-negative integer.")
