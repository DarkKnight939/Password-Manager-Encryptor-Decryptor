import __main__


def logout():
    """Log the user out of their account."""
    __main__.current_account = None
    print("You have been logged out.")
