from mysql.connector import connect, Error


def get_connection(HOST, USERNAME, PASSWORD, DATABASE):
    """
    function to create and return the connection to database
    :param HOST: HOST name of the database
    :param USERNAME:  username to use in the database
    :param PASSWORD: password for the username
    :param DATABASE: database to be used
    :return:
    """
    connection = connect(
        host=HOST,
        user=USERNAME,
        password=PASSWORD,
        database=DATABASE,
    )
    return connection
