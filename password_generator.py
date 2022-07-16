
#       __              _          _____        _           _         
#       \ \ _   _ _ __ (_) ___  _ _\_   \_ __  (_) ___  ___| |_ ___   
#        \ \ | | | '_ \| |/ _ \| '__/ /\/ '_ \ | |/ _ \/ __| __/ __|  
#     /\_/ / |_| | | | | | (_) | /\/ /_ | | | || |  __/ (__| |_\__ \  
#     \___/ \__,_|_| |_|_|\___/|_\____/ |_| |_|/ |\___|\___|\__|___/ v1.0
#                                            |__/  Password Generator 

import random

chars = ""

#setting up Password Generator
lowerLetters = input(str("Do you want to use lower Letters? [\033[92myes\033[0m/\033[91mno\033[0m] "))
if lowerLetters == "yes":
    chars = chars + "abcdefghijklmnopqrstuvwxyzäöü"   #adding lower Letters to password char
upperLetters = input(str("Do you want to use upper Letters? [\033[92myes\033[0m/\033[91mno\033[0m] "))
if upperLetters == "yes":
    chars = chars + "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ"   #adding upper Letters to password char
numbers = input(str("Do you want to use Numbers? [\033[92myes\033[0m/\033[91mno\033[0m] "))
if numbers == "yes":
    chars = chars + "0123456789"   #adding numbers to password char
special = input(str("Do you want to use Special Chars? [\033[92myes\033[0m/\033[91mno\033[0m] "))
if special == "yes":
    chars = chars + "!§$%&/()=`*+~#'-_.:,;"   #adding special Chars to password char

passwordlenght = int(input("How Long should your Password be? "))
passwordcount = int(input("How many Passwords do you want? "))

#confirm creation
confirm = input(str("Do you realy want to create " + str(passwordcount) + " Passwords? [\033[92myes\033[0m/\033[91mno\033[0m] "))

if confirm == "yes":
    for x in range(0, passwordcount):
        pw = ""
        for x in range(0, passwordlenght):
            pw_char = random.choice(chars)
            pw = pw + pw_char
        print(pw)
    print("\033[92mpasswords created.\033[0m")
if confirm != "yes":
    print("\033[91mcreation stopped.\033[0m")
