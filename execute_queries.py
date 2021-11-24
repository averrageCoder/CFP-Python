from connect_to_mysql import get_connection
from dotenv import dotenv_values

from sql_queries import create_movies_table_query, create_reviewers_table_query, create_ratings_table_query, \
    insert_reviewers_query, show_table_query

config = dotenv_values(".env")
HOST = config["HOST"]
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']
DATABASE = config['DATABASE']


class MySQLUtil:
    def __init__(self, HOST, USERNAME, PASSWORD, DATABASE):
        self.connection = get_connection(HOST, USERNAME, PASSWORD, DATABASE)
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        """
        to execute query to database
        :param query: sql query to be executed
        :return:
        """
        self.cursor.execute(query)
        self.connection.commit()

    def executemany_query(self, query, values):
        """
        to execute many queries at once
        :param query: query to be executed
        :param values: values to be used in the query
        :return:
        """
        self.cursor.executemany(query, values)
        self.connection.commit()

    def execute_and_fetch_query(self, query):
        """
        to execute a query and fetch the result from the query
        :param query: query to be executed and fetched
        :return:
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.connection.commit()
        return result

    def close_connection(self):
        """
        function that closes the connection to mysql
        :return:
        """
        self.connection.close()


if __name__ == "__main__":
    mysql_util = MySQLUtil(HOST, USERNAME, PASSWORD, DATABASE)
    mysql_util.execute_query(create_movies_table_query)
    mysql_util.execute_query(create_reviewers_table_query)
    mysql_util.execute_query(create_ratings_table_query)
    result = mysql_util.execute_and_fetch_query(show_table_query)
    for row in result:
        print(row)
    mysql_util.executemany_query(insert_reviewers_query["query"], insert_reviewers_query["values"])
    mysql_util.close_connection()
