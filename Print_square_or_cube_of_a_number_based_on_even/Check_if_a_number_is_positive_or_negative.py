def check_positive_negative(num):
    if num > 0:
        return "Positive"
    elif num < 0:
            return"Negative"
    else:
         return "Zero"
number = int(input("Enter an integer: "))
print(check_positive_negative(number))