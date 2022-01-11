from Modules.clear_scr import clr_scr


def check_strength():
    clr_scr()
    print("Welcome to Password Strength Checker 💪\n")
    password = input("Enter your password: ")
    clr_scr()
    if len(password) < 8:
        print("Your password is too short")
    elif password.isalpha():
        if password.isupper() or password.islower():
            print("Your password is weak",
                  "Try including upper and lower case alphabets and numbers along with special characters to make your password strong", sep="\n")
        else:
            print("Your password is weak",
                  "Try including numbers along with special characters to make your password strong", sep="\n")
    elif password.isdigit():
        print("Your password is weak",
              "Try including mixture of upper and lower case alphabets along with special characters to make your password strong", sep="\n")
    elif password.isalnum():
        print("Your password is weak",
              "Try including special characters to make your password strong", sep="\n")
    elif password.isupper() or password.islower():
        print("Your password is strong",
              "Try including mixture of upper and lower case alphabets to make your password stronger", sep="\n")
    else:
        print("Your password is very strong")
    return True
