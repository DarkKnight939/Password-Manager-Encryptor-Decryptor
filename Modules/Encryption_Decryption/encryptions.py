def basic_encryption(text):
    result = ""
    sh = int(input("Enter the number by which it is to be shifted: "))
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            x = ord(char)+sh
            if char.isupper():
                if x > 90:
                    x = (x-90)+64
            if char.islower():
                if x > 122:
                    x = (x-122)+96
            result = result+chr(x)
    print("The encrypted data is:", result)
    return True


def standard_encryption(text):
    text = text.upper()
    result = ""
    key = input("Enter a key (alphabets only): ").upper()
    while not key.isalpha():
        key = input(
            "Key can't have any other character other than alphabets\nEnter a key (alphabets only): ").upper()
    l, j = len(key), 0
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            sh = key[j]
            x = (ord(char)-65)+(ord(sh)-65)
            j += 1
            if(j == l):
                j = 0
            if x > 25:
                x = (x-26)
            tem = chr(x+65)
            result = result+tem
        else:
            result = result+char
    print("The encrypted data is:", result)
    return True


def advanced_encryption(text):
    encoded = ""
    encrypted = ""
    for i in range(len(text)):
        if text[i].isalpha() == True:
            caps = text[i].capitalize()
            x = (ord(caps))+(i)+1
            if x > 90:
                x = x-26
            a = x-64
            if x > 64 and x < 78:
                el = chr((2*a)+64)
                encoded = encoded+el
                pass
            elif x > 77 and x < 91:
                el = chr(((a-13)*2)-1+64)
                encoded += el
                pass
        elif text[i].isdigit() == True:
            el = int(text[i])+(i)+1
            while el > 9:
                el = el-9
            encoded += str(el)
        else:
            encoded += text[i]
    key_h = str(input(
        "Enter a 6-letter key for security purpose (For future reference, note as horizontal key): ")).upper()
    while not key_h.isalpha() or len(key_h) != 6:
        if key_h.isalpha() == False:
            print("Key can't have any other character other than alphabets")
        if len(key_h) != 6:
            print("Key must be 6 letters long")
        key_h = str(input(
            "Enter a 6-letter key for security purpose: ")).upper()

    key_v = str(input(
        "Enter a 6-letter key for security purpose (For future reference, note as vertical key): ")).upper()
    while not key_v.isalpha() or len(key_v) != 6:
        if key_v.isalpha() == False:
            print("Key can't have any other character other than alphabets")
        if len(key_v) != 6:
            print("Key must be 6 letters long")
        key_v = str(input(
            "Enter a 6-letter key for security purpose: ")).upper()

    grid = [['A', 'B', 'C', 'D', 'E', 'F'], ['G', 'H', 'I', 'J', 'K', 'L'], ['M', 'N', 'O', 'P', 'Q', 'R'], [
        'S', 'T', 'U', 'V', 'W', 'X'], ['Y', 'Z', '0', '1', '2', '3'], ['4', '5', '6', '7', '8', '9']]
    for i in range(len(encoded)):
        char = encoded[i]
        for j in range(len(grid)):
            a = list(grid[j])
            if char in a:
                vertical = a.index(char)
                horizontal = j
                encrypted += key_h[vertical]+key_v[horizontal]+""
        if char.isspace() == True:
            encrypted += " "
        elif char.isalnum() == False:
            encrypted += char
    print("The encrypted data is:", encrypted)
    return True


