#!/bin/env python3
from time import sleep
from colorama import Fore, Style
import os
import sys
import configparser
import requests
import json
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



class WorkWithVkApi:
    
    def get_parametrs(self):
        """Get Server, Key, Ts"""
        global key, ts, server
        response = requests.get('https://api.vk.com/method/messages.getLongPollServer?access_token=' + vk_token + '&v=5.21')
        data = response.json()
        #print(data)
        server = data['response']['server']
        server = server.replace("api.vk.com/ru", "")
        key = data['response']['key']
        ts = data['response']['ts']
        print("server:",server);print("key:",key);print("ts:",ts) 

    def get_messages(self):
        """Get Messages From vk"""
        response = requests.get('https://im.vk.com/n'+str(server)+'?act=a_check&key='+str(key)+'&wait=25&mode=2&ts='+str(ts)+'&version=3')
        data = response.json()
        print(data)

    def 

class Send_to_Telegram:
    def __init__(self):
        pass

def test():
    print("--------------------------------")
    print(login, password, vk_token, tg_token)
    print("--------------------------------")


if __name__ == "__main__":
    root = Other() 
    root.parse_config() #Parsing COnfig File
    test() #Return to konsole data from config file
    bb = WorkWithVkApi()
    bb.get_parametrs()
    bb.get_messages()
