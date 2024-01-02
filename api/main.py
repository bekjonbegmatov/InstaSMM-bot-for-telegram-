# from api_config import VENRO_API_KEY , VENRO_URL_API
import requests
import json

class Smm :

    def __init__(self):
        self.api_key = '7dbdb2323c085e5acb97d55c1f415ef0'     
        self.api_url = 'https://venro.ru/api/orders?'
    
    def set_services (self):
        data = requests.get(f'{self.api_url}action=services&key={self.api_key}')
        print(f'{self.api_url}action=services&key={self.api_key}')
        data = data.json()
        self.data = data
        self.__print_name()
        # with open('sevice.json' , 'w' , encoding='utf-8') as f:
        #     json.dump(data, f , ensure_ascii=False)

    def __print_name(self):
        for ser in self.data:
            print(ser['name'])
    
    def print_from_file(self):
        data = open('sevice.json')
        data = json.load(data)
        folowers = []
        likes = []
        video_vievs = []
        seves = []
        for i in data:
            # if i['name'].split()[0] == 'Followers':folowers.append(i)
            # elif i['name'].split()[0] == 'Likes':likes.append(i)
            # elif i['name'].split()[0] == 'Video':video_vievs.append(i)
            # elif i['name'].split()[0] == 'Saves':seves.append(i)
            print(i['name'])

        # [print(f['name']) for f in folowers]

S = Smm()
S.print_from_file()