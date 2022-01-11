from Modules.clear_scr import clr_scr
import __main__
import random
import string


def password_generator():
    # Generate a password of a given length
    clr_scr()
    print('Welcome to the Password Generator 🔑\n')

    # Initialize password preferences
    chr_include = True
    digits_include = True
    spcial_chr_include = True
    lower_case = True
    upper_case = True
    # Ask user for type of password
    length = int(input('Enter the length of the string: '))
    if length < 8:
        print('**Password too short**')
        if input("Enter 'r' to renter the length, else press any other key to suppress this warning: ") == 'r':
            return password_generator()
    chr_include = True if input(
        'Do you want to include alphabetical letters in your password ? (y/n): ').lower() == 'y' else False
    if chr_include:
        case_include = True if input(
            'Do you want characters in mixed case in your password? (y/n): ').lower() == 'y' else False
        if not case_include:

            lower_case = True if input(
                'Do you want to include lower case characters in your password? (y/n): ').lower() == 'y' else False
            upper_case = not lower_case

    digits_include = True if input(
        'Do you want to include digits? (y/n): ').lower() == 'y' else False
    spcial_chr_include = True if input(
        'Do you want to include special characters? (y/n): ').lower() == 'y' else False
    password_lst = []  # List of characters in the password
    if not (chr_include or digits_include):
        print("Invalid password request, password should atleast contain alphabets or numbers.",
              "Please try again", sep="\n")
        return password_generator()
    elif spcial_chr_include:
        for i in range(2):
            # Add special characters to the password
            password_lst.append(random.choice(string.punctuation))

    for i in range(length-len(password_lst)):
        password_lst.append(random.choice(
            (((string.ascii_lowercase if lower_case else '') + (string.ascii_uppercase if upper_case else '')) if chr_include else '') + (string.digits if digits_include else '')))  # Add alphabets and digits to the password

    password_string = ""  # Password string
    temp_num_list = list(range(length))
    # Running this loop to ensure randomness of the password
    while temp_num_list:
        temp_ind = (random.choice(temp_num_list))
        temp_num_list.remove(temp_ind)
        password_string += password_lst[temp_ind]
    like_to_save = True if input(
        'Do you want to save this password? (y/n): ').lower() == 'y' else False
    if like_to_save:
        site = input("Enter the site you'd like your password for: ")
        while not site:
            site = input(
                "Site cannot be blank\nPlease enter the site you'd like your password for: ")
        # Check if the site already exists in the database
        for i in __main__.password_manager_dict.keys():
            if i == __main__.current_user and site in __main__.password_manager_dict[i].keys():
                print(f"Password for {site} is saved already")

                if input(
                        "Would you like to update the existing password? (y/n) ").lower() == 'y':
                    print("Password updated.")
                    break
                else:
                    print("Password not updated.")
                    return True

        __main__.password_manager_dict[__main__.current_user][site] = password_string

    clr_scr()
    print(f"Your password is: {password_string}")
    return True
