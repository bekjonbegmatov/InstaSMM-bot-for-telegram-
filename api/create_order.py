import requests

class Order:
    def __init__(self, url:str):
        self.url = url

    def create_test_order(self):
        # https://venro.ru/api/orders?action=add&key=7dbdb2323c085e5acb97d55c1f415ef0&url=https://www.instagram.com/instagram/&count=100&type=2

        url = f'https://venro.ru/api/orders?action=add&key=7dbdb2323c085e5acb97d55c1f415ef0&url={self.url}&count=200&type=7'

        status = requests.get(url=url)
        print(status.json())

    def check_order(self, idv:int):
        url = f'https://venro.ru/api/orders?action=check&key=7dbdb2323c085e5acb97d55c1f415ef0&id={idv}'
        status = requests.get(url)
        print(status.json())

# Order(url='https://www.instagram.com/behruz.beg/').create_test_order()
Order(url='https://www.instagram.com/behruz.beg/').check_order(idv=475590203)


# https://www.instagram.com/behruz.beg/
# https://venro.ru/api/orders?action=check&key=7dbdb2323c085e5acb97d55c1f415ef0&id=13073
# {'id': 475590203, 'url': 'https://www.instagram.com/behruz.beg/', 'start': 0, 'count': 200, 'remains': 200, 'status': 'Pending', 'charge': 0.038, 'currency': 'USD'}