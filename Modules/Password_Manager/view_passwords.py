from Modules.clear_scr import clr_scr
import __main__


def view_passwords():
    clr_scr()
    print("Welcome to the Password Viewer 👀\n")
    if not len(__main__.password_manager_dict[__main__.current_user].keys()):
        print("No passwords saved")
    else:
        print("What do you want to view?\n1. All passwords\n2. Password of a site")
        choice = input("Your choice: ")
        while choice not in ['1', '2']:
            choice = input("Invalid input\nYour choice: ")
        clr_scr()
        if choice == "1":
            print("\nSaved passwords:")
            print("Site | Password")
            for key, value in __main__.password_manager_dict[__main__.current_user].items():
                print(key, "|", value)
        elif choice == "2":
            site = input("Enter the site: ")
            if site in __main__.password_manager_dict[__main__.current_user].keys():
                print(
                    "Your password for", site, "is", __main__.password_manager_dict[__main__.current_user][site])
            else:
                print("No password for this site")

    return True
