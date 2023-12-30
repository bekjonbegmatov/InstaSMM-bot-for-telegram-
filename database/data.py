import sqlite3
import json
"""
    CLASS FOR MANAGING WHITH USER_MODEL
"""

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
        self.conn.commit()
        return True

    # The method for getting all users
    def get_all_users(self):
        self.cursor.execute('SELECT * from users')
        return self.cursor.fetchall()

    # The method wil be check user in db if 404 , add tom db
    def check_user_if_not_add(self, username:str, first_name:str, second_name:str, chat_id:int, user_id:int, balance:str):
        users = self.get_all_users()
        for user in users:
            if user[1] == user_id :
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

    # The method for exporting all users to txt file
    def extport_to_txt(self):
        txt_file = open('users.txt', 'w')
        lis = self.get_all_users()
        for usr in lis:
            temp = []
            for i in range(6):
                temp.append(usr[i])  
            txt_file.write(str(temp) + '\n')
        txt_file.close
        return True

    # The method for eporting data to json file 
    def export_to_json(self):
        users = self.get_all_users()
        data = []
        for user in users:
            temp = {
                'id' : user[0],
                'user id' : user[1],
                'chat id' : user[2],
                'user name' : user[3],
                'first name' : user[4],
                'second name' : user[5],
                'balance' : user[6],
            }
            data.append(temp)
        with open( "users.json" , 'w' , encoding='utf-8') as f:
            json.dump(data , f , ensure_ascii=False , indent=7)
        return True

    # The method for exporting data array
    def export_to_array(self):
        users = self.get_all_users()
        data = ''
        i = 1
        for user in users:
            data += f'№{i}\n├id : {user[0]}\n├user id : {user[1]}\n├chat id : {user[2]}\n├user name : @{user[3]}\n├first name : {user[4]}\n├second name : {user[5]}\n└balance : {user[6]}\n\n'
            i+=1
        return data
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

"""
    CLASS FOR MANAGING WHITH ADMIN_MODEL
"""

class Admin:

    def __init__(self):
        self.conn = sqlite3.connect('data.sqlite3', check_same_thread=False)
        self.cursor = self.conn.cursor()

    # The method for creating admins
    def create_admin(self, new_admin_id:int, role:str):
        U = User()
        users = U.get_all_users()
        try:
            for admin in users:
                if admin[0] == new_admin_id:
                    user_id = admin[1]
                    chat_id = admin[2]
                    username = admin[3]

            self.cursor.execute("INSERT INTO admin (user_id, chat_id, username, role) VALUES (?, ?, ?, ?)", 
            (
                user_id,
                chat_id,
                username,
                role
            ))
            self.conn.commit()
            return True
        except:
            return False
    
    # The method for getting all admins list
    def get_all_admins(self):
        self.cursor.execute("SELECT * from admin")
        return self.cursor.fetchall()

    # The method for getting adminn whith roles
    def get_admin_with_role(self, role):
        admins = self.get_all_admins()
        ral = [] # Return admin list
        for adm in admins:
            if adm[4] == role: ral.append(adm)
        return ral

    # The method for changing role admins
    def set_role(self, user_id, new_role):
        try:
            self.cursor.execute("UPDATE admin SET role = ? WHERE user_id = ?", (new_role, user_id))
            self.conn.commit()
            return True
        except:
            return False

    # The method for removing admin whith user_id
    def remove_admin(self, user_id):
        try:
            self.cursor.execute("DELETE FROM admin WHERE user_id = ?", (user_id))
            self.conn.commit()
            return True
        except:
            return False
    
    # Check is user admin
    def is_admin(self, user_id:int):
        admins = self.get_all_admins()
        for admin in admins:
            if admin[1] == user_id:
                return admin[4]
        return 'user'

"""
    CLASS FOR MANAGING WHITH CHANALS_MODEL
"""

class Chanals:

    def __init__(self):
        self.conn = sqlite3.connect('data.sqlite3', check_same_thread=False)
        self.cursor = self.conn.cursor()

    # The method for creating chanals
    def create_chanal(self, chanal_name:str, current_trafic:int, final_trafic:int, is_active:bool):
        self.cursor.execute("INSERT INTO chanals (chanal_name, current_trafic, final_trafic, is_active) VALUES (?, ?, ?, ?)" , 
        (
            chanal_name,
            current_trafic,
            final_trafic,
            is_active,
        ))
        self.conn.commit()
        return True

    # The method for changing trafic 
    def change_trafic(self, final_trafic:int, idv:int):
        self.cursor.execute("UPDATE chanals SET final_trafic = ? WHERE id = ?", (final_trafic, idv))
        self.conn.commit()
        return True

    # The method for changing active | True or False
    def change_active(self, is_active:bool, idv:int):
        self.cursor.execute("UPDATE chanals SET is_active = ? WHERE id = ?", (is_active, idv))
        self.conn.commit()
        return True

    # The method for getting all chanals
    def get_all_chanals(self):
        self.cursor.execute("SELECT * from chanals")
        return self.cursor.fetchall()

# U = Admin()
# # U.set_role(5163141099 , 'super_admin')
# print(U.create_admin(1001 , 'moder'))