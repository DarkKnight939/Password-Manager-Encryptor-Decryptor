
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
    text = text.upper()
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
                sublist_index = key_h.index(text[i])
                mainlist_index = key_v.index(text[i+1])
                char = grid[mainlist_index][sublist_index]
                decoded += char
                i += 2
        else:
            decoded += text[i]
            i += 1
    for i in range(len(decoded)):
        char = decoded[i]
        if char.isalpha() == True:
            x = ord(char)-64
            if x % 2 == 0:
                a = int((x/2)+64)
            elif x % 2 != 0:
                a = int(((x+1)/2)+13+64)
            a = a-i-1
            if a < 65:
                el = chr(a+26)
            else:
                el = chr(a)
            decrypted += el
        elif char.isdigit() == True:
            a = int(char)-i-1
            while a < 0:
                a += 9
            el = str(a)
            decrypted += el
        else:
            decrypted += char
    print("The decrypted data is:", decrypted)
    return True


