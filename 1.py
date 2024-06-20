def check_number(number):
    if number % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    
    if number > 0:
        pos_neg_zero = "positive"
    elif number < 0:
        pos_neg_zero = "negative"
    else:
        pos_neg_zero = "zero"
    
    return even_odd, pos_neg_zero

number = float(input("Enter a number: "))
even_odd, pos_neg_zero = check_number(number)
print(f"The number is {even_odd} and {pos_neg_zero}.")
