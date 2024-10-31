def check_digit(n):
    if 0 <= n <= 9:
        print("Single digit")
    elif 10 <= n <=99:
        print("Two digit")    
    elif 100 <= n <= 999:
        print("Three digit")
    else:
        print("More than three digits")


check_digit(0)        
