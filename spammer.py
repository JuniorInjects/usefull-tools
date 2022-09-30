import time, pyautogui

confirm = input(str("Do you realy want to use this spam? yes/no "))
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
