
#       __              _          _____        _           _         
#       \ \ _   _ _ __ (_) ___  _ _\_   \_ __  (_) ___  ___| |_ ___   
#        \ \ | | | '_ \| |/ _ \| '__/ /\/ '_ \ | |/ _ \/ __| __/ __|  
#     /\_/ / |_| | | | | | (_) | /\/ /_ | | | || |  __/ (__| |_\__ \  
#     \___/ \__,_|_| |_|_|\___/|_\____/ |_| |_|/ |\___|\___|\__|___/ v1.0
#                                            |__/  Password Checker   

import random
import time
import sys

password = input(str("Password: "))

chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '\\', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
tryPassword = ""
tryPasswordTries = 0
timeStart = time.time()

try:

    while True:
        tryPasswordTries += 1

        for char in range(len(password)):
            tryPassword = tryPassword + chars[random.randint(0, len(chars)-1)]
        timeStop = time.time()
        timeTotal = round(timeStop - timeStart, 1)

        if tryPassword == password:
            print(f"{tryPasswordTries} | \033[96mValid\033[0m | {tryPassword} (\033[93m{timeTotal}s\033[0m)")
            break
        else:
            print(f"{tryPasswordTries} | Invalid | {tryPassword}")
    
        tryPassword = ""

except KeyboardInterrupt:
    print("\n \033[91m Stopping after " + f"{timeTotal}s" + "\033[0m")
    sys.exit()
