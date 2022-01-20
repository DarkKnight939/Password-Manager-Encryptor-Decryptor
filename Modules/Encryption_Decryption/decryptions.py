
from base64 import decode


def basic_decryption(text):
    result = ""
    sh = int(input("Enter the number by which it was shifted: "))
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            x = ord(char)-sh
            if char.isupper():
                if x < 65:
                    x = 91-(65-x)
            if char.islower():
                if x < 97:
                    x = 123-(97-x)
            result = result+chr(x)
    print("The decrypted data is: ", result)
    return True


def standard_decryption(text):
    result = ""
    key = input("Enter the number the key used: ").upper()
    l, j = len(key), 0
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            sh = key[j]
            x = (ord(char)-65)-(ord(sh)-65)
            j += 1
            if(j == l):
                j = 0
            if x < 0:
                x = 26+x
            tem = chr(x+65)
            result = result+tem
        else:
            result = result+char
    print("The decrypted data is:", result)
    return True


def advanced_decryption(text):
    decoded = ""
    decrypted = ""
    i = 0
    key_h = str(input("Enter horizontal key:")).upper()
    key_v = str(input("Enter vertical key:")).upper()
    grid = [['A', 'B', 'C', 'D', 'E', 'F'], ['G', 'H', 'I', 'J', 'K', 'L'], ['M', 'N', 'O', 'P', 'Q', 'R'], [
        'S', 'T', 'U', 'V', 'W', 'X'], ['Y', 'Z', '0', '1', '2', '3'], ['4', '5', '6', '7', '8', '9']]
    while i < len(text):
        if (text[i].isalpha()) == True:
            if text[i+1].isalpha() == True:
                sublist_index = i
                mainlist_index = i+1
                char = grid[mainlist_index][sublist_index]
                decoded += char
                i += 2
        else:
            decoded += text[i]
            i += 1
    for i in range(len(decoded)):
        if decoded[i].isalpha() == True:
            x = ord(decoded[i])-64
            if x % 2 == 0:
                a = int((x/2)+64)
            elif x % 2 != 0:
                a = int(((x+1)/2)+13+64)
            a = a-decoded.index(decoded[i])-1
            if a < 65:
                el = chr(a+26)
            else:
                el = chr(a)
            decrypted += el
        elif decoded[i].isdigit() == True:
            a = int(decoded[i])-decoded.index(decoded[i])-1
            while a < 0:
                a += 9
            el = str(a)
            decrypted += el
        else:
            decrypted += decoded[i]
    print("The decrypted data is:", decrypted)
    return True


if __name__ == "__main__":
    choice = input("Enter 1 for basic, 2 for standard and 3 for advanced: ")
    data = input("Enter the data to be decrypted: ")
    if choice == "1":
        basic_decryption(data)
    elif choice == "2":
        standard_decryption(data)
    elif choice == "3":
        advanced_decryption(data)
