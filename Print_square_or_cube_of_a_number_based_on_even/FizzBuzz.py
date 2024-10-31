def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("Buzz")    
    else:
        print(n)    

fizz_buzz(5)        