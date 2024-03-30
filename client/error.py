from colorama import Fore
import os
import time
def server_not_online(exception):
    os.system("cls")
    print(Fore.RED + "Server is most likely not online, if you think this is not true\nPlease contact the developer." + Fore.RESET + f"\n{exception}")
    time.sleep(5)
    exit()

def cannot_send_message(exception):
    os.system("cls")
    print(Fore.RED + "The message couldn't be sent to the Server\nMost likely either\n- your wifi-connection is not working properly\n- the server isn't online" + Fore.RESET + f"\n{exception}")
    time.sleep(10)
    exit()