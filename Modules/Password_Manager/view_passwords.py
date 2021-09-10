from Modules.clear_scr import clr_scr
import __main__


def view_passwords():
    clr_scr()
    print("Welcome to the Password Viewer 👀\n")
    if __main__.current_user not in __main__.pasword_manager_dict.keys():
        print("You have no passwords saved.")
    else:
        print("Your passwords are:")
        passwod_keys = list(__main__.pasword_manager_dict.keys())
        passwod_values = list(__main__.pasword_manager_dict.values())
        for i in range(len(passwod_keys)):
            if passwod_keys[i] == __main__.current_user:
                print(f"{passwod_values[i][0]}: {passwod_values[i][1]}")
    return True
