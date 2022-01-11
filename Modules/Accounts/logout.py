import __main__


def logout():
    __main__.current_user = None
    print("You have been logged out.")
    return True
