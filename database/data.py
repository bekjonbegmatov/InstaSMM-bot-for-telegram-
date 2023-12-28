import sqlite3

class User:
    # Initialization class
    def __init__(self):

        # Conecting Database 
        self.conn = sqlite3.connect('data.sqlite3', check_same_thread=False)
        self.cursor = self.conn.cursor()

    # Method for closing the database connection
    def __close_connection(self):
        try:
            self.conn.close()
            return True
        except Exception as e:
            return False

    # The method for adding a new users
    def adding_user(self , username:str, first_name:str, second_name:str, chat_id:int, user_id:int, balance:str):
        # Adding values 
        self.cursor.execute(
            'INSERT INTO users (user_id, chat_id, username, first_name, second_name, balance) VALUES (?, ?, ?, ?, ?, ?)' ,
            (
                user_id,
                chat_id, 
                username, 
                first_name, 
                second_name, 
                balance
                ))
        self.conn.commit() # commit the conection
        return True
    # The method for getting all users
    def get_all_users(self):
        self.cursor.execute('SELECT * from users')
        return self.cursor.fetchall()

    # The method wil be check user in db if 404 , add tom db
    def check_user_if_not_add(self, username:str, first_name:str, second_name:str, chat_id:int, user_id:int, balance:str):

        # Getting all users
        users = self.get_all_users()
        # Checking user
        for user in users:
            if user[1] == user_id :
                # Return True if the user was found
                return True
        # Adding if user not found
        self.adding_user(
            username=username, 
            first_name=first_name, 
            second_name=second_name, 
            chat_id=chat_id, 
            user_id=user_id, 
            balance=balance
            )
        return False

    # The method for editing updating a balance     
    def update_balance(self, user_id: int, new_balance: str):
        try:
            self.cursor.execute("UPDATE users SET balance = ? WHERE user_id = ?", (new_balance, user_id))
            self.conn.commit()  # Commit the connection to save changes
            return True
        except Exception as e:
            print(f"Error updating balance: {e}")
            return False

    """
    THE METHODS FOR CREATING ORDERS
    """

    # Creating a new record of order
    def create_order(self, user_id:int, price:str, order_id:int, status:str, count:int, remains:int, url:str ):
        try:
            self.cursor.execute("INSERT INTO user_history (user_id, price, order_id, status, count, remains, url) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                user_id,
                price,
                order_id,
                status,
                count,
                remains,
                url
            ))
            self.conn.commit()
            return True # If all of OK
        except:
            return False # If something is not OK

    # The method for getting a list of history user
    def get_history(self, user_id:int):
        self.cursor.execute("SELECT * from user_history")
        history = self.cursor.fetchall()
        user_history = []
        for his in history:
            if his[1] == user_id : user_history.append(his)
        return user_history

    # The method for uploading a status of order
    def update_status_of_order(self, order_id:int, status:str):
        try:
            self.cursor.execute("UPDATE user_history SET status = ? WHERE order_id = ?", (status, order_id))
            self.conn.commit()
            return True
        except:
            return False