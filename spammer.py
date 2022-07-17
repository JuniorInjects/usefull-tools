
#       __              _          _____        _           _         
#       \ \ _   _ _ __ (_) ___  _ _\_   \_ __  (_) ___  ___| |_ ___   
#        \ \ | | | '_ \| |/ _ \| '__/ /\/ '_ \ | |/ _ \/ __| __/ __|  
#     /\_/ / |_| | | | | | (_) | /\/ /_ | | | || |  __/ (__| |_\__ \  
#     \___/ \__,_|_| |_|_|\___/|_\____/ |_| |_|/ |\___|\___|\__|___/ v1.0
#                                            |__/  Spam Bot       

import time, pyautogui

confirm = input(str("Do you realy want to use this spam? [\033[92myes\033[0m/\033[91mno\033[0m] "))
if confirm == "yes":
    print("Spam is starting in 5 Secounds")
    time.sleep(5)
    while 1:
        file = open("spamm_messages.text", 'r')
        for word in file:
            pyautogui.typewrite(word)
            pyautogui.press("enter")
if confirm != "yes":
    print("cancled.")
