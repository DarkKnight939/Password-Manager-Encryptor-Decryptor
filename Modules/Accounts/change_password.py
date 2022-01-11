import __main__


def change_password():
    print("Change password🔏\n")
    password, confirm_password = "-1", "0"
    while password != confirm_password:
        password = input("Enter the password: ")
        while not password:
            password = input("Password cannot be blank\nEnter the password: ")
        confirm_password = input("Confirm password: ")
        if confirm_password != password:
            print("Passwords do not match. Please try again.")
    __main__.users[__main__.current_user] = password
    print("Password updated successfully 🔐")
    return True
