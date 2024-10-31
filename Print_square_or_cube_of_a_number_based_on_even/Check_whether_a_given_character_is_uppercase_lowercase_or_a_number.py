def check_char_type(c):
    if c.isupper():
        print("Uppercase")
    elif c.islower():
        print(f"ASCII number: {ord(c)}")
    else:
        print("Special character")    

check_char_type('A')        