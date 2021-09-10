import __main__


def change_password():
    """Change the password of the current user."""
    print("Change the password for a user.")
    password = input("Enter the password: ")
    confirm_password = input("Confirm password: ")
    while confirm_password != password or not password:
        print("Passwords do not match/ Password cannot be empty. Please try again.")
        password = input("Enter the password: ")
        confirm_password = input("Confirm password: ")
    __main__.users[__main__.username] = password
    print("Password changed.")
