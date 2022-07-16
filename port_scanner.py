
#       __              _          _____        _           _         
#       \ \ _   _ _ __ (_) ___  _ _\_   \_ __  (_) ___  ___| |_ ___   
#        \ \ | | | '_ \| |/ _ \| '__/ /\/ '_ \ | |/ _ \/ __| __/ __|  
#     /\_/ / |_| | | | | | (_) | /\/ /_ | | | || |  __/ (__| |_\__ \  
#     \___/ \__,_|_| |_|_|\___/|_\____/ |_| |_|/ |\___|\___|\__|___/ v1.0
#                                            |__/  Port Scanner       

import socket
import subprocess
import sys
from datetime import datetime

#setting up PortScanner
target = input(str("Target IP: "))
portStart = int(input("start PortScanner from Port: "))
portStop = int(input("check to Port: "))

print("-" * 50)
print("\033[92mScanning Target:\033[0m " + "\033[96m" + str(target) + "\033[0m")
print("\033[92mScanning started at:\033[0m " + "\033[96m" + str(datetime.now()) + "\033[0m")
print("-" * 50)

try:
    
    #scanning every port between portStart & portStop
    for port in range(portStart, portStop):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #return Port if is open
        result = s.connect_ex((target, port))
        if result == 0:
            print("[\033[92m+\033[0m] Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n \033[91m Closing... :P\033[0m")
    sys.exit()

except socket.error:
    print("\n \033[91m Host is not online :(\033[0m")
    sys.exit()

print("finished PortScanner from " + str(target) + " with PortRange: " + str(portStart) + " - " + str(portStop))
