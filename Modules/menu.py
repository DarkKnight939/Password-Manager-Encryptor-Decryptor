from Modules.Accounts.change_password import change_password
from Modules.Accounts.delete_accunt import delete_account
from Modules.Accounts.logout import logout
from Modules.clear_scr import clr_scr
import __main__
from Modules.Password_Manager.password_generator import password_generator
from Modules.Password_Manager.check_strength import check_strength
from Modules.Password_Manager.view_passwords import view_passwords
from Modules.Password_Manager.update_password import update_password
from Modules.Password_Manager.delete_password import delete_password


def menu():
    print("\nChoose the action you want to perform:", "1. Enter Password Manager 🔑",
          "2. Enter Encryptor/ Decryptor 🔏", "3. Manage Account 👤", "4. Logout 👥", "5. Exit 👋", sep="\n")
    choice = input("Your choice: ")
    while choice not in ['1', '2', '3', '4', '5']:
        choice = input("Invalid inout\nYour choice: ")
    clr_scr()
    if choice == "1":
        print("\nYou have chosen to enter the Password Manager", "Enter the action you want to perform:", "1. Generate a password 🔑",
              "2. Check the strength of your password 💪", "3. Get saved passwords 👀", "4. Update a saved password 🔏", "5. Delete a saved password 🗑", sep="\n")
        choice = input("Your choice: ")
        while choice not in ['1', '2', '3', '4', '5']:
            choice = input("Invalid input\nYour choice: ")
        if choice == "1":
            return password_generator()
        elif choice == "2":
            return check_strength()
        elif choice == "3":
            return view_passwords()
        elif choice == "4":
            return update_password()
        elif choice == "5":
            return delete_password()

    elif choice == "2":
        pass
    elif choice == "3":
        print("Enter the action you want to perform:",
              "1. Change master password 🔏", "2. Delete account 🗑", sep="\n")
        choice = input("Your choice: ")
        while choice not in ['1', '2']:
            choice = input("Invalid input\nYour choice: ")
        if choice == "1":
            return change_password()
        elif choice == "2":
            return delete_account()
    elif choice == "4":
        return logout()
    elif choice == "5":
        return False
