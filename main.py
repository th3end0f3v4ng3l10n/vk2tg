#!/bin/env python3
from time import sleep
from colorama import Fore, Style
import os
import sys
import configparser
import requests
import json
import telebot
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
        global login, password, vk_token, tg_token, chat_id
        """Config Grabber"""
        config = configparser.ConfigParser()
        config.read('config.ini')
        
        login = config['Vk']['Password']
        password = config['Vk']['Login']
        vk_token = config['Vk']['Vk_Token']

        tg_token = config['Telegram']['Tg_Token']
        chat_id = config['Telegram']['Chat_id']

class Send_to_Telegram:
    def send_message(self, message):
        string = 'https://api.telegram.org/bot'+str(tg_token)+'/sendMessage?chat_id='+str(chat_id)+'&text=' + str(message)
        requests.post(string)

    def send_sticker(self, username, stickername):
        make_string = 'curl -s -X POST "https://api.telegram.org/bot'
        make_string += tg_token
        make_string += '/sendPhoto?chat_id='
        make_string += chat_id
        make_string += '" -F photo="@./packs/'
        make_string += stickername
        make_string += '"'
        make_string += " -F caption='"
        make_string += username
        make_string += ":'"
        os.system(make_string)
        os.system("rm -rf ./packs/*")
        


class Message():
    def get_sticker(self,username,link):
        print(Fore.GREEN + username, ":",Style.RESET_ALL,'https://vk.com/sticker/1-'+str(link)+'-352b')
        sticker_link = 'https://vk.com/sticker/1-'+str(link)+'-352b'
        sticker_name = '1-' + str(link) + '-352b'
        os.system('wget -P ./packs/ '+ sticker_link)
        StT = Send_to_Telegram()
        StT.send_sticker(username, sticker_name)


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
        Telega = Send_to_Telegram()

        response = requests.get('https://im.vk.com/n'+str(server)+'?act=a_check&key='+str(key)+'&wait=25&mode=2&ts='+str(ts)+'&version=3')
        self.data = response.json()
 
        user_id = self.data['updates'][0][3]
        username = requests.get('https://api.vk.com/method/users.get?access_token='+str(vk_token)+'&user_ids='+str(user_id)+'&v=5.21')
        name = username.json()
        try:
            if self.data['updates'][0][7]['attach1_type'] == 'sticker':
                username = name['response'][0]['first_name']
                username += " "
                username += name['response'][0]['last_name']
                print(username)
                link = self.data['updates'][0][7]['attach1']
                print('stick')
                Work.get_sticker(username,link)
        except:
            if name['response'][0]['first_name'] != "DELETED":
                print(Fore.GREEN + name['response'][0]['first_name'], name['response'][0]['last_name'], ":",Style.RESET_ALL, self.data['updates'][0][5])
                message = name['response'][0]['first_name'] + ' ' + name['response'][0]['last_name'] + ': ' + self.data['updates'][0][5]
                Telega.send_message(message)




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