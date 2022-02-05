# Team Member: Aanchal Saraf, Shirshendu Sen Gupta and Shivansh Shalabh
# Project Name: Data Security and Storage Platform
from Modules.Accounts.sign_up import sign_up
from Modules.Accounts.user_login import user_login
from Modules.clear_scr import clr_scr
from Modules.menu import menu
import datetime


if __name__ == '__main__':
    # users is a dictionary with keys as username and values as password
    users = dict()
    # curent_user is the username of the username who is logged in
    current_user = None
    password_manager_dict = dict()
    clr_scr()
    print("Welcome to Data Security and Storage Platform🔐")
    print("Please sign up to continue\n")
    sign_up()
    last_time_active = datetime.datetime.now()
    while menu():
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
    print("\nThank you for using Data Security and Storage Platform🔐")
