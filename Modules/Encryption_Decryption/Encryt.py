# -*- coding: utf-8 -*-
st=input("Do you want to Encrypt or Decrypt? ")
st1=input("What standard of encryption/decryption do you want? ")
if st1=="Level 1":
    if st=="Encrypt":
        text=input("Enter the data to be encrypted: ")
        result=""
        sh=int(input("Enter the number by which it is shifted: "))
        for i in range(len(text)):
            char = text[i]
            if char.isalnum():
                x=ord(char)+sh
                if char.isupper():
                    if x>90:
                        x=(x-90)+64
                if char.islower():
                    if x>122:
                        x=(x-122)+96
                result=result+chr(x)
        print("The encrypted data is: ",result)
    elif st=="Decrypt":   
        text=input("Enter the data to be decrypted: ")
        result=""
        sh=int(input("Enter the number by which it was shifted: "))
        for i in range(len(text)):
            char = text[i]
            if char.isalnum():
                x=ord(char)-sh
                if char.isupper():
                    if x<65:
                        x=91-(65-x)
                if char.islower():
                    if x<97:
                        x=123-(97-x)
                result=result+chr(x)
        print("The decrypted data is: ",result)    
elif st1=="Level 2":
    if st=="Encrypt":
        text=input("Enter the data to be encrypted: ")
        result=""
        key=input("Enter a key: ")
        l,j=len(key),0
        for i in range(len(text)):
            char = text[i]
            if char.isalnum():
                sh=key[j]
                x=(ord(char)-65)+(ord(sh)-65)
                j+=1
                if(j==l):
                    j=0
                if x>25:
                    x=(x-26)
                tem=chr(x+65)    
                result=result+tem
            else:
                result=result+char        
        print("The encrypted data is: ",result)
    elif st=="Decrypt":   
        text=input("Enter the data to be decrypted: ")
        result=""
        key=input("Enter the number the key used: ")
        l,j=len(key),0
        for i in range(len(text)):
            char = text[i]
            if char.isalnum():
                sh=key[j]
                x=(ord(char)-65)-(ord(sh)-65)
                j+=1
                if(j==l):
                    j=0
                if x<0:
                    x=26+x
                tem=chr(x+65)    
                result=result+tem
            else:
                result=result+char                        
        print("The decrypted data is: ",result)       
          
