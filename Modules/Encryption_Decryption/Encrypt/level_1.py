def enc_level_1(text):
    result = ""
    sh = int(input("Enter the number by which it is shifted: "))
    for i in range(len(text)):
        char = text[i]
        if char.isalnum():
            x = ord(char)+sh
            if char.isupper():
                if x > 90:
                    x = (x-90)+64
                if char.islower():
                    if x > 122:
                        x = (x-122)+96
                result = result+chr(x)
