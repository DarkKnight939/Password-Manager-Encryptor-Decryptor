import __main__

from Modules.clear_scr import clr_scr


def delete_account():
    choice = input(
        "Are you sure you want to delete your account? (y/n): ").lower()
    clr_scr()
    if choice == "y":
        del __main__.users[__main__.current_user]
        del __main__.password_manager_dict[__main__.current_user]

        __main__.current_user = None
        print("Account and all saved data deleted successfully🗑")
    else:
        print("Action cancelled by the user❌")
    return True
