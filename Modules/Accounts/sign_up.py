import __main__
from Modules.clear_scr import clr_scr


def sign_up():
    clr_scr()
    print("**Sign up for an account**")
    username = input("Username: ")
    while not username:
        print("Username cannot be blank")
        username = input("Username: ")
        if username in __main__.users.key():
            print("Username already exists", "Please use a ")
            username = input("Username: ")
    password = input("Enter the password: ")
    confirm_password = input("Confirm password: ")
    while confirm_password != password or not password:
        print("Passwords do not match/ Password cannot be empty. Please try again.")
        password = input("Enter the password: ")
        confirm_password = input("Confirm password: ")
    __main__.users[username] = password
    __main__.current_user = username
    clr_scr()
    print(f"Account created for {username}")
    return True
