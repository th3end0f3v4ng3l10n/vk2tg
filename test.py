import vk_api
from vk_api.longpoll import VkLongPoll
import requests
import telebot
import configparser



class ROOT:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.login = self.config['Vk']['Login']
        self.password = self.config['Vk']['Password']
        self.token1 = self.config['Vk']['Token']
        self.token2 = self.config['Telegram']['Token']

    def auth(self):
        vk_session = vk_api.VkApi(self.login, self.password)
        vk_session.auth()
        self.vk = vk_session.get_api()
        print('SUCCESS')


    def get_data(self):
        data = requests.get('https://api.vk.com/method/messages.getLongPollServer?access_token='+str(self.token1)+'&v=5.21')
        #print(data.json())
        data = data.json()
        self.server = data['response']['server']
        self.key = data['response']['key']
        self.ts = data['response']['ts']

    def get_messages(self):
        def generate_message(message,ids):
            response = requests.get('https://api.vk.com/method/users.get?access_token='+str(self.token1)+'&user_ids='+str(ids)+'&v=5.21')
            data = response.json()
            data1 = data['response'][0]['first_name']
            data2 = data['response'][0]['last_name']
            message_formatted = f'{data1} {data2} : {message}'
            if 'DELETED' in message_formatted:
                pass
            else:
                print(message_formatted)
                requests.post('https://api.telegram.org/bot'+str(self.token2)+'/sendMessage?chat_id=728156139&text={}'.format(message_formatted))

        self.server = self.server.replace('api.vk.com/ru','')
        response = requests.get('https://im.vk.com/n'+str(self.server)+'?act=a_check&key='+str(self.key)+'&wait=25&mode=2&ts='+str(self.ts)+'&version=3')
        #print(response.json())
        data = response.json()
        try:
            message = data['updates'][0]
            ids = message[3]
            generate_message(message[5], ids)
        except:
            pass

def main():
    root = ROOT()
    root.auth()
    while True:
        root.get_data()
        root.get_messages()

main()
