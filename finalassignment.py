import random
import string


## generate passwords from 
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "~!@#$%^&*()_+"

##concatenation of string scharacters
characters = list(lower_case + upper_case + digits + symbols)

while 1:
    ##while the following conditions are met, continue to run
    ##get length and count of generated password from user
    password_len = int(input("What should be the length of your password : "))
    password_count = int(input("What is the number of passwords you want to have : "))

    ##define range
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(characters)
            password      = password + password_char

        print("Hurray, this is your randomly generated password : " , password)
