import sqlite3

class User:

    # Initialization class
    def __init__(self):

        # Conecting Database 
        self.conn = sqlite3.connect('database.sqlite', check_same_thread=False)
        self.cursor = self.conn.cursor()

    # The method for adding a new users
    def adding_user(self , username:str, first_name:str, second_name:str, chat_id:int, user_id:int, balance:str):

        # Adding values 
        self.cursor('INSERT INTO users (user_id, chat_id, username, furst_name, second_name, balance) VALUES (?, ?, ?, ?, ?, ?)' , (user_id, chat_id, username, first_name, second_name, balance))
        self.conn.commit() # commit the conection
    
    # The method for getting all users
    def get_all_users(self):
        self.cursor.execute('SELECT * from users')
        return self.cursor.fetchall()

    # The method wil be check user in db if 404 , add tom db
    def check_user_if_not_add(self, username:str, first_name:str, second_name:str, chat_id:int, user_id:int, balance:str):

        # Getting all users
        users = self.get_all_users()
        # Checking user
        for user in records:
            if user[1] == users :
                # Return True if the user was found
                return True
        # Adding if user not found
        self.adding_user(username=username, first_name=first_name, second_name=second_name , chat_id=chat_id, user_id=user_id, balance=balance)
        return False

    