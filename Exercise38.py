#wap to validate username password  using while and for loop.

# actual_username = 'ek tha tiger'
# actual_password = '12345678'
# while True :
#     username = input('Enter your username: ')


#     if username == actual_username:
#       while True:
        
#         passward = input("enter password here :")


#         if passward == actual_password:
#             print("login successfull")
#             break
#         else:
#              print(" incorrect password, please try again.")
#         break
#     else:
#       print("incorrect username , please try again")



actual_username = 'ek tha tiger'
actual_password = '12345678'

while True:
    username = input('Enter your username: ')
    
    # Check if the username is correct
    if username == actual_username:
        while True:
            password = input("Enter your password here: ")
            
            # Check if the password is correct
            if password == actual_password:
                print("Login successful!")
                break  # Exit the password loop
            else:
                print("Incorrect password, please try again.")
        break  # Exit the outer loop after successful login
    else:
        print("Incorrect username, please try again.")
