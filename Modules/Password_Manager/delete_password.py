import __main__
from Modules.clear_scr import clr_scr


def delete_password():
    clr_scr()
    print("Delete a password🗑\n")
    site = input("Enter the site: ")
    if site in __main__.password_manager_dict[__main__.current_user].keys():
        choice = input(
            "Are your sure you want to delete this password? (y/n): ").lower()
        clr_scr()
        if choice == "y":
            del __main__.password_manager_dict[__main__.current_user][site]
            print("Password deleted")
        else:
            print("Password not deleted")
    else:
        print("No password for this site")
    return True
