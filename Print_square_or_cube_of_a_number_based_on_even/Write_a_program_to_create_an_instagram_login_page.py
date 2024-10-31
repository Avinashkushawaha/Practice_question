def instagram_login():
    print("Welcome to instagram login page")
    print("=" * 40)

    valid_username = "user123"
    valid_password = "pass123"

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == valid_username and password == valid_password:
        print("=" * 40)
        print("login successful! Welcome to instagram.")
        print("=" * 40)
    else:
        print("=" * 40)
        print("login failed! invalid username or password.")
        print("=" * 40)

instagram_login()
