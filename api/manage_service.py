import requests
import json 

class Smm:
    def __init__(self):
        self.api_url = ''
        self.api_key = ''

    def update_services_json(self):
        data = requests.get('')
        data = data.json()
        self.data = data
        self.__save_to_json()
        return True

    def __save_to_json(self):
        with open('sevice.json' , 'w' , encoding='utf-8') as f :
            json.dump(self.data, f , ensure_ascii=False)

    def __read_json(self):
        f = open('sevice.json')
        data = json.load(f)
        self.readed_json = data

    def __split_services(self):
        data = self.readed_json
        followers = []
        likes = []
        views = []
        comments = []
        saves = []
        reach = []
        for el in data:
            e = el['name'].split()[0]
            if e == 'Followers' : followers.append(el)
            elif e == 'Likes' : likes.append(el)
            elif e == 'Views' : views.append(el)
            elif e == 'Comments' : comments.append(el)
            elif e == 'Saves' : saves.append(el)
            elif e == 'Reach' : reach.append(el)
        self.j_followers
        self.j_likes
        self.j_views
        self.j_comments
        self.j_saves
        self.j_reach

    def create_new_servicees(self):

        self.__read_json()
        self.__split_services()

        data = []

        flw = []
        like = []
        views = []
        comen = []
        statis = []

        for f in self.j_followers:
            temp = {
                'id' : f['id'],
                'service' : f['service'],
                'name' : '',
            }
class ManageBot:
    def __int__(self):
        pass
    def get_all(self):
        f = open('sevice.json')
        data = json.load(f)
        return data

    def get_from_category(self,category:str):
        data = self.get_all()
        f_data = []
        for d in data:
            if d['category'] == category:
                f_data.append(d)
        return f_data

    def get_from_id(self, idv:str):
        data = self.get_all()
        f_data = []
        for d in data:
            if d['ID'] == idv:
                f_data.append(d)
        return f_data