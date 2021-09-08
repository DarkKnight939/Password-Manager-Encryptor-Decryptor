import __main__


def sign_up():
    print("\nSign up for an account")
    username = input("Username: ")
    while not username:
        print("Username cannot be blank")
        username = input("Username: ")
        if username in __main__.users.key():
            print("Username already exists","Please use a ")
            username = input("Username: ")
    password = input("Enter the password: ")
    confirm_password = input("Confirm password: ")
    while confirm_password != password or not password:
        print("Passwords do not match/ can. Please try again.")
        password = input("Enter the password: ")
        confirm_password = input("Confirm password: ")
    __main__.users[username] = password
    print(f"\nAccount created for {username}")
    return True
