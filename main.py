#!/bin/env python3
from time import sleep
from colorama import Fore, Style
import os
import sys
import configparser



def fprint(text,color):
    """Log Function"""
    if color == "red":
        print(Fore.RED + " [LOG]", Style.RESET_ALL, "==>", text, Style.RESET_ALL)
    else:
        print(Fore.YELLOW + " [LOG]", Style.RESET_ALL, "==>", text, Style.RESET_ALL)


class Other:
    def start_message(self):
        """Simple Hello World Programm"""
        my_message = "<=== Welcome to VK2TG ===>"
        my_message2 = "Author Telegram: @th3end0f3v4ng3l10n"
        my_string = ""

        os.system("clear")
        for i in my_message:
            my_string += i
            print(my_string)
            sleep(0.15)
            os.system("clear")
        print(my_message)
        fprint(my_message2, "yellow")

    def parse_config(self):
        global login, password, vk_token, tg_token
        """Config Grabber"""
        config = configparser.ConfigParser()
        config.read('config.ini')
        
        login = config['Vk']['Password']
        password = config['Vk']['Login']
        vk_token = config['Vk']['Vk_Token']

        tg_token = config['Telegram']['Tg_Token']
        fprint("Read data from config.ini...", "yellow")
        



class Send_to_Telegram:
    def __init__(self):
        pass


class Get_message:
    def __init__(self):
        pass

def test():
    print(login, password, vk_token, tg_token)


if __name__ == "__main__":
    root = Other()
    root.parse_config()
    test()
