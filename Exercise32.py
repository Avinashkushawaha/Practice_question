#wap to print factorial numbers given number using for loop.
num = int(input("Enter number here : "))
factorial = 1
for factor in range(1, num + 1):
    
    factorial *= factor
    print("Factorial of", num, "is", factorial)
