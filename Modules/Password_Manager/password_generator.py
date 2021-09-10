from Modules.clear_scr import clr_scr
import __main__
import random
import string


def password_generator():
    """Generate a password of a given length."""
    clr_scr()
    print('Welcome to the Password Generator 🔑\n')
    password_lst = []
    chr_include = True
    digits_include = True
    spcial_chr_include = True
    lower_case = True
    upper_case = True
    length = int(input('Enter the length of the string: '))
    if length < 8:
        print('**Password too short**')
        if input("Enter 'r' to renter the length, else press any other key to supress this warning: ") == 'r':
            return password_generator()
    chr_include = input(
        'Do you want to include alphabetical letters in your password ? (y/n): ')
    chr_include = True if chr_include.lower() == 'y' else False
    if chr_include:
        case_include = input(
            'Do you want characters in mixed case in your password? (y/n): ')
        case_include = True if case_include.lower() == 'y' else False
        if not case_include:
            lower_case = input(
                'Do you want to include lower case characters in your password? (y/n): ')
            lower_case = True if lower_case.lower() == 'y' else False
            upper_case = not lower_case
    digits_include = input('Do you want to include digits? (y/n): ')
    digits_include = True if digits_include.lower() == 'y' else False
    spcial_chr_include = input(
        'Do you want to include special characters? (y/n): ')
    spcial_chr_include = True if spcial_chr_include.lower() == 'y' else False
    if not (chr_include or digits_include):
        print("Invalid password  request, password should either contain alphabets or numbers or both.",
              "Please try again", sep="\n")
        return password_generator()

    elif spcial_chr_include:
        for i in range(int(max(2, length*0.1))):
            password_lst.append(random.choice(string.punctuation))

    site = input("Enter the site you'd like your password for: ")
    while not site:
        site = input("Enter the site you'd like your password for: ")
    for i in range(length-len(password_lst)):
        password_lst.append(random.choice(
            (((string.ascii_lowercase if lower_case else '') + (string.ascii_uppercase if upper_case else '')) if chr_include else '') + (string.digits if digits_include else '')))
    n = length
    password_string = ""
    temp_num_list = list(range(n))
    while temp_num_list:
        temp_ind = (random.choice(temp_num_list))
        temp_num_list.remove(temp_ind)
        password_string += password_lst[temp_ind]
        n -= 1

    for i in __main__.pasword_manager_dict.keys():
        if i == __main__.current_user and __main__.pasword_manager_dict[i][0] == site:
            print(f"Password for {site} is {password_string}")
            choice = input(
                "Would you like to overwrite the existing password? (y/n) ")
            if choice.lower() == 'y':
                __main__.pasword_manager_dict[i] = [site, password_lst]
                print("Password saved.")
            else:
                print("Password not saved.")
                return True

    __main__.pasword_manager_dict[__main__.current_user] = [
        site, password_string]
    clr_scr()
    print(f"Your password for {site} is: {password_string}")
    return True


if __name__ == '__main__':
    print(password_generator())
