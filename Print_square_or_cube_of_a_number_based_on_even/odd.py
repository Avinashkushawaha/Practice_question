def square_or_cube(num):
    if num % 2 == 0:
        return num ** 2
    else:
        return num ** 3

number = int(input("Enter a number here: "))    
print(square_or_cube(number))    
