def last_digit_divisible_by_three(num):
    return (num % 10) % 3 == 0

number = int(input("Enter an integer: "))
print(last_digit_divisible_by_three(number))