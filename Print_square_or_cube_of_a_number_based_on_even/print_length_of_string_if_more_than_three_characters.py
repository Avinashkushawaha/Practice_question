def string_length_or_original(s):
    if len(s) > 3:
        return len(s)
    else:
        return s
    
user_string = input("Enter a string: ")    
print(string_length_or_original(user_string))