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
    elif color == "yellow":
        print(Fore.YELLOW + " [LOG]", Style.RESET_ALL, "==>", text, Style.RESET_ALL)
    elif color == "green":
        print(Fore.GREEN + " [LOG]", Style.RESET_ALL, "==>", text, Style.RESET_ALL)

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

class Message():
    def send_sticker(self,link):
        print('https://vk.com/sticker/1-'+str(link)+'-352b')
        #print('sticker!')


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
        #print("server:",server);print("key:",key);print("ts:",ts) 

    def get_messages(self):

        """Get Messages From vk"""
        Work = Message()
        response = requests.get('https://im.vk.com/n'+str(server)+'?act=a_check&key='+str(key)+'&wait=25&mode=2&ts='+str(ts)+'&version=3')
        self.data = response.json()
 
        user_id = self.data['updates'][0][3]
        username = requests.get('https://api.vk.com/method/users.get?access_token='+str(vk_token)+'&user_ids='+str(user_id)+'&v=5.21')
        name = username.json()
  
    
        if name['response'][0]['first_name'] != "DELETED":
            print(Fore.GREEN + name['response'][0]['first_name'], name['response'][0]['last_name'], ":",Style.RESET_ALL, self.data['updates'][0][5] )

        """CHECK ON STICKER"""
        try:
            if self.data['updates'][0][7]['attach1_type'] == 'sticker':
                username = name['response'][0]['first_name'] + name['response'][0]['last_name']
                link = self.data['updates'][0][7]['attach1']
                Work.send_sticker(link)
        except:
            pass

class Send_to_Telegram:
    def __init__(self):
        pass

if __name__ == "__main__":
    root = Other()
    #!-------------------------------------------------
    try:
        fprint("Parsing config.ini...", "yellow")
        root.parse_config() #Parsing COnfig File
        fprint("All OK", "green")
    except:
        fprint("Error while read data from config.ini", "red")

    #----------------------------------------------------
    try:
        fprint("Connecting to vk api...", "yellow")
        bb = WorkWithVkApi()
    except:
        pass

    #)====================================================
    while True:
        try:
            bb.get_parametrs() #get params
        except:
            fprint("Error while connecting to vk api", "red")

        try:
            bb.get_messages() #get messages
        except:
            pass