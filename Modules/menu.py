from Modules.clear_scr import clr_scr
import __main__
from Modules.Password_Manager.password_generator import password_generator
from Modules.Password_Manager.check_strength import check_strength
from Modules.Password_Manager.view_passwords import view_passwords
from Modules.Password_Manager.search_password import search_password
from Modules.Password_Manager.update_password import update_password
from Modules.Password_Manager.delete_password import delete_password


def menu():
    print("\nChoose the action you want to perform:")
    print("1. Enter Password Manager")
    print("2. Enter Encryptor/ Decryptor")
    while True:
        choice = input("Enter your choice: ")
        if choice in ['1', '2']:
            break
    clr_scr()
    if choice == "1":
        print("\nYou have chosen to enter the Password Manager")
        print("Enter the action you want to perform:")
        print("1. Generate a password")
        print("2. Check the strength of your password")
        print("3. View all passwords")
        print("4. Search for a password")
        print("5. Update a password")
        print("6. Delete a password")
        choice = input("Enter your choice: ")
        while choice not in ['1', '2', '3', '4', '5', '6']:
            choice = input("Enter your choice: ")
        if choice == "1":
            return password_generator()
        elif choice == "2":
            return check_strength()
        elif choice == "3":
            return view_passwords()
        elif choice == "4":
            search_password()
        elif choice == "5":
            update_password()
        elif choice == "6":
            delete_password()

    elif choice == "2":
        __main__.encryptor_decryptor()
