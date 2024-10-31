def check_character(c):
    c = input("Enter a character: ")

    if c.isupper():
        print("uppercase")
    elif c.islower():
        print("lowercase")
    elif c.isdigit():
        print(f"Number: {c}")
    else:
        print("special character")        

check_character('@')        
