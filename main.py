from Modules.Accounts.sign_up import sign_up
from Modules.Accounts.user_login import user_login
from Modules.clear_scr import clr_scr
from Modules.menu import menu
from Modules.Password_Manager.password_generator import password_generator


if __name__ == '__main__':
    # users is a dictionary with keys as username and values as password
    users = dict()
    # curent_user is the username of the username who is logged in
    current_user = None
    password_manager_dict = dict()
    clr_scr()
    print("Welcome to Password Manager🔐")
    print("Please sign up to continue\n")
    sign_up()
    while menu():
        print("here", current_user)
        while current_user == None:
            print("\nYou have to login first")
            choice = input("1. Login\n2. Sign up\n3. Exit\nYour choice: ")
            if choice not in ['1', '2', '3']:
                choice = input("Invalid input\nYour choice: ")
            if choice == '1':
                user_login()
            elif choice == '2':
                clr_scr()
                sign_up()
            elif choice == '3':
                break
    print("\nThank you for using Password Managern🔐")
