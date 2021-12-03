import logging
import pandas as pd
from dotenv import dotenv_values

from connect_to_mysql import get_connection

logging.basicConfig(filename='mysql.log', filemode='a', level=logging.DEBUG, format='%(asctime)s %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')

config = dotenv_values(".env")
HOST = config["HOST"]
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']
DATABASE = config['DATABASE']

class MySQLUtil:
    def __init__(self):
        try:
            self.connection = get_connection(HOST, USERNAME, PASSWORD, DATABASE)
            logging.info("Database connection successful!")
            self.cursor = self.connection.cursor()
        except Exception as e:
            logging.error(str(e))
            raise e

    def execute_query(self, query, values=None):
        """
        to execute query to database
        :param values: value to be added in query
        :param query: sql query to be executed
        :return:
        """
        try:
            if not values:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, values)
            self.connection.commit()
        except Exception as e:
            logging.error("{} for query '{}' values '{}'".format(str(e), query, values))
            self.connection.rollback()
            raise e

    def executemany_query(self, query, values):
        """
        to execute many queries at once
        :param query: query to be executed
        :param values: values to be used in the query
        :return:
        """
        try:
            self.cursor.executemany(query, values)
            self.connection.commit()
        except Exception as e:
            logging.error("{} for query '{}'".format(str(e), query))
            self.connection.rollback()
            raise e

    def execute_and_fetch_query(self, query):
        """
        to execute a query and fetch the result from the query
        :param query: query to be executed and fetched
        :return:
        """
        try:
            self.cursor.execute(query)
            description = self.cursor.description
            result = self.cursor.fetchall()
            return result, description
        except Exception as e:
            logging.error("{} for query '{}'".format(str(e), query))
            self.connection.rollback()
            raise e

    def read_csv_and_insert_to_db(self, df, table_name):
        """
        to read csv and insert to db
        :param csvfile: path of csv file
        :param table_name: name of the table to be inserted into
        :return:
        """
        # df = pd.read_csv(csvfile)
        df.drop('id', axis=1, inplace=True)
        df.fillna(0, inplace=True)
        logging.debug(df.info())
        columns = df.columns.values.tolist()
        all_rows = []

        columns_str = ''
        value_format_specifier = ''
        for column in columns:
            columns_str += column + ','
            value_format_specifier += '%s,'
        columns_str = columns_str.rsplit(',', 1)[0]
        value_format_specifier = value_format_specifier.rsplit(',', 1)[0]

        for index, row in df.iterrows():
            row_value = ()
            for column in columns:
                # if pd.isna(row[column]):
                #     row[column] = None
                row_value += (row[column],)
            all_rows.append(row_value)
            query = "insert into {}({}) values({})".format(table_name, columns_str, value_format_specifier)
            # print(query)
            self.execute_query(query, row_value)

    def close_connection(self):
        """
        function that closes the connection to mysql
        :return:
        """
        try:
            self.connection.close()
        except Exception as e:
            self.connection.rollback()
            logging.error(str(e))
            raise e
