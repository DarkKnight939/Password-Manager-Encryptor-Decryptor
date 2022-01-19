import __main__
from Modules.clear_scr import clr_scr


def sign_up():

    print("Sign up for an account📋")
    # Inputing username and password
    username = input("Username: ")
    while not username:
        username = input("Username cannot be blank\nUsername: ")
        if not username and username in __main__.users.key():
            username = input(
                "Username already exists\nPlease enter a different username\nUsername: ")
    password, confirm_password = "-1", "0"
    while password != confirm_password:
        password = input("Enter the master password: ")
        while not password:
            password = input("Password cannot be blank\nEnter the password: ")
        confirm_password = input("Confirm password: ")
        if confirm_password != password:
            print("Passwords do not match. Please try again.")
    # Adding username and password to the dictionary
    __main__.users[username] = password
    __main__.current_user = username
    # Creating password vault for new user
    __main__.password_manager_dict[username] = dict()
    clr_scr()
    print(f"Account created for {username}")
    return True
