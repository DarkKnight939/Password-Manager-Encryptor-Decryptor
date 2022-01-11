from Modules.clear_scr import clr_scr
import __main__


def update_password():
    clr_scr()
    print("Update password🔏\n")
    site = input("Enter the site: ")
    if site in __main__.password_manager_dict[__main__.current_user].keys():
        print(
            "Current password for this site is: ", site, ":", __main__.password_manager_dict[__main__.current_user][site])
        print("What do you want to update?\n1. Password\n2. Site")
        choice = input("Your choice: ")
        while choice not in ['1', '2']:
            choice = input("Invalid input\nYour choice: ")
        if choice == "1":
            __main__.password_manager_dict[__main__.current_user][site] = input(
                "Enter the new password: ")
        elif choice == "2":
            __main__.password_manager_dict[__main__.current_user][input(
                "Enter the new site: ")] = __main__.password_manager_dict[__main__.current_user][site]
            del __main__.password_manager_dict[__main__.current_user][site]
        clr_scr()

        print("Database updated")
    else:
        print("No password for this site")
        choice = input("Do you want to add a new password? (y/n): ").lower()

        if choice == "y":
            __main__.password_manager_dict[__main__.current_user][site] = input(
                "Enter the new password: ")
            clr_scr()
            print("Password added")
        else:
            clr_scr()

    return True
