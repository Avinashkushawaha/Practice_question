def is_multiple_of_ten(num):
    return num % 10 == 0


number = int(input("Enter an integer: "))
print(is_multiple_of_ten(number))