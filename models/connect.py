from mysql.connector import connect, ProgrammingError


def connect_db():
    print("Connecting, please wait...")
    username = "root"
    password = "coderslab"
    hostname = "localhost"
    database = "message_server_db"
    try:
        cnx = connect(user=username, password=password,
                      host=hostname, database=database)
        print('Connection successful!')
        return cnx
    except ProgrammingError:
        print("Connection failed!")


def disconnect_db(cursor, cnx):
    cursor.close()
    cnx.close()
    print('Successfully disconnected!')

