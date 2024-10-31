def is_three_digit_number(num):
    return 100 <= abs(num) < 1000


number = int(input("Enter an integer: "))    
print(is_three_digit_number(number))