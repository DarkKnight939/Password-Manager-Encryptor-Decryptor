from Modules.Accounts.sign_up import sign_up
from Modules.menu import menu
from Modules.Password_Manager.password_generator import password_generator


if __name__ == '__main__':
    # users is a dictionary with keys as username and values as password
    users = dict()
    # curent_user is the username of the username who is logged in
    current_user = None
    pasword_manager_dict = dict()
    sign_up()
    while menu():
        pass
