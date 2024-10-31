def is_divisible_by_two_and_three(num):
    return num % 2 == 0 and num % 3 == 0

number = int(input("Enter an integer: "))
print(is_divisible_by_two_and_three(number))