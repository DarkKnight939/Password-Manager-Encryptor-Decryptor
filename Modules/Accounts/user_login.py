import __main__
from Modules.clear_scr import clr_scr


def user_login():
    clr_scr()
    print("User Login👤")
    username = input("Enter your username: ")
    password = input("Enter the master password: ")
    if username in __main__.users.keys():
        if __main__.users[username] == password:
            __main__.current_user = username
            clr_scr()
            print("You have successfully logged in.")
    print("Invalid username or password")
    return True
