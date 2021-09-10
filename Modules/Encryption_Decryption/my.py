def Encrypt(text, step):
    text = list(char for char in text)
    for i in range(len(text)):
        text[i] = chr(ord(text[i]) + step)
    print(''.join(text))
    return "".join(text)


def Decrypt(text, step):
    text = list(char for char in text)
    for i in range(len(text)):
        text[i] = chr(ord(text[i]) - step)
    print(''.join(text))
    return "".join(text)


if __name__ == "__main__":
    string = input("Enter the string to be encrypted: ")
    step = int(input("Enter the step: "))
    Encrypt(string, step)
    Decrypt(string, step)
