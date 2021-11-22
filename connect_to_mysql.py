from getpass import getpass
from mysql.connector import connect, Error


def get_connection(HOST, USERNAME, PASSWORD, DATABASE):
    try:
        connection = connect(
            host=HOST,
            user=USERNAME,
            password=PASSWORD,
            database=DATABASE,
        )
        print("Connection successful!")
        return connection
    except Error as e:
        print(e)
        return None
