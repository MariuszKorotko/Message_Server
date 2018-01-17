from clcrypto import password_hash
from connect import connect_db, disconnect_db


class User(object):

    __id = None
    email = None
    username = None
    __hashed_password = None

    def __init__(self):
        self.__id = -1
        self.username = ""
        self.email = ""
        self.__hashed_password = ""

    @property
    def id(self):
        return self.__id

    @property
    def hashed_password(self):
        return self.__hashed_password

    def set_password(self, password, salt):
        self.__hashed_password = password_hash(password, salt)

    def save_to_db(self, cursor):
        # saves new user or update
        if self.__id == -1:
            query = """INSERT INTO Users(username, email, hashed_password)
                       VALUES('{}', '{}', '{}')""".format(self.username,
                                                          self.email,
                                                          self.hashed_password)
            cursor.execute(query)
            self.__id = cursor.lastrowid
            print("Successfully saved!")
            return True
        else:
            query = """UPDATE User SET username='{}', emial='{}',
                       hashed_password='{}',
                       WHERE id='{}'""".format(self.username,
                                               self.email,
                                               self.hashed_password,
                                               self.id)
            cursor.execute(query)
            print("Successfully updated!")
            return True

    @staticmethod
    def load_user_by_id(cursor, id):
        query = """SELECT id, username, email, hashed_password
                   FROM Users WHERE id={}""".format(id)
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            loaded_user = User()
            loaded_user.__id = row[0]
            loaded_user.username = row[1]
            loaded_user.email = row[2]
            loaded_user.__hashed_password = row[3]
            return loaded_user
        else:
            return None

    @staticmethod
    def load_user_by_email(cursor, email):
        query = """SELECT id, username, email, hashed_password
                   FROM Users WHERE email='{}'""".format(email)
        row = cursor.execute(query).fetchone()
        if row is not None:
            loaded_user = User()
            loaded_user.__id = row[0]
            loaded_user.username = row[1]
            loaded_user.email = row[2]
            loaded_user.__hashed_password = row[3]
            return loaded_user
        else:
            return None

    @staticmethod
    def load_all_users(cursor):
        query = """SELECT id, username, email, hashed_password FROM Users"""
        all_users = []
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            loaded_user = User()
            loaded_user.__id = row[0]
            loaded_user.username = row[1]
            loaded_user.email = row[2]
            loaded_user.__hashed_password = row[3]
            all_users.append(loaded_user)
        return all_users

    @staticmethod
    def load_users_by_name(cursor, username):
        query = """SELECT id, username, email, hashed_password
                   FROM Users
                   WHERE username='{}'""".format(username)
        users = []
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            loaded_user = User()
            loaded_user.__id = row[0]
            loaded_user.username = row[1]
            loaded_user.email = row[2]
            loaded_user.__hashed_password = row[3]
            users.append(loaded_user)
        return users


if __name__ == "__main__":
    cnx = connect_db()
    cnx.autocommit = True
    cursor = cnx.cursor()

    # testing class User 1
    # user = User()
    # user.username = 'mariusz'
    # user.email = 'mariusz.korotko@wp.pl'
    # user.set_password('test_password1', salt=None)
    # print(user.id, user.username, user.email, user.hashed_password)

    # testing save to database User 1
    # user.save_to_db(cursor)

    # testing class User 2
    # user = User()
    # user.username = 'henryk'
    # user.email = 'henryk.sienkiewicz@wp.pl'
    # user.set_password('test_password2', salt=None)
    # print(user.id, user.username, user.email, user.hashed_password)

    # testing save to database User 2
    # user.save_to_db(cursor)

    # testing class User 3
    # user = User()
    # user.username = 'mariusz'
    # user.email = 'mariusz.wojciechowski@wp.pl'
    # user.set_password('test_password3', salt=None)
    # print(user.id, user.username, user.email, user.hashed_password)

    # testing save to database User 3
    # user.save_to_db(cursor)

    # testing load user by id
    # user = User.load_user_by_id(cursor, 1)
    # print(user.id, user.username, user.email, user.hashed_password)

    # testing load user by email
    # user = User.load_user_by_email(cursor, 'mariusz.korotko@wp.pl')
    # print(user.id, user.username, user.email, user.hashed_password)

    # testing load all users
    # users = User.load_all_users(cursor)
    # print(users[0].id, users[0].username, users[0].email,
    #       users[0].hashed_password)

    # testing load users by name
    # users = User.load_users_by_name(cursor, 'mariusz')
    # print(users[0].id, users[0].username, users[0].email,
    #       users[0].hashed_password)
    # print(users[1].id, users[1].username, users[1].email,
    #       users[1].hashed_password)

    # disconnect_db(cursor, cnx)
