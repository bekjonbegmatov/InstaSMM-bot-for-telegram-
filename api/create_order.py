import requests

class Order:
    def __init__(self):
        # self.url = url
        # self.count = count
        self.key = '7dbdb2323c085e5acb97d55c1f415ef0'
        # self.type_id = type_id
    
    def check_order(self, idv:str):
        url = f'https://venro.ru/api/orders?action=check&key=7dbdb2323c085e5acb97d55c1f415ef0&id={idv}'
        status = requests.get(url)
        return status.json()

    def create_instagram_order(self, url:str, count:int, type_id:str):
        aurl = f'https://venro.ru/api/orders?action=add&key={self.key}&url={url}&count={count}&type={type_id}'
        status = requests.get(url=aurl)
        return status.json()


# Order(url='https://www.instagram.com/zohid.mee/').create_test_order()
# Order(url='https://www.instagram.com/behedgkosfhvdfiusvh/', count=12, type_id='7').create_instagram_order()
# Order(url='https://www.instagram.com/behedgkosfhvdfiusvh/', count=12, type_id='7').check_order(idv=476056159)


# https://www.instagram.com/behruz.beg/
# https://venro.ru/api/orders?action=check&key=7dbdb2323c085e5acb97d55c1f415ef0&id=13073
# {'id': 475590203, 'url': 'https://www.instagram.com/behruz.beg/', 'start': 0, 'count': 200, 'remains': 200, 'status': 'Pending', 'charge': 0.038, 'currency': 'USD'}
