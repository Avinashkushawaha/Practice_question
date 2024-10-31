def is_palindrome(s):
    return s == s[::-1]

user_string = input("Enter a string: ")
print(is_palindrome(user_string))