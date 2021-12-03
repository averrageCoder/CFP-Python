from io import StringIO
from typing import Optional

import pandas as pd
from fastapi import FastAPI, File, UploadFile
from model import Book

from mysql_util import MySQLUtil

app = FastAPI()
mysql_util = MySQLUtil()


def to_df(file):
    return pd.read_csv(StringIO(str(file.file.read(), 'utf-8')), encoding='utf-8')


@app.get("/read_books/{id}/")
def read_book(id: int, extra: Optional[str] = None):
    """
    to output books from db
    :param id: id of the book to show, if none, show all
    :param extra: extra query parameter
    :return:
    """
    out_dictionary = {}
    query = "select * from books where id={}".format(id)
    if extra == 'all':
        query = "select * from books"

    try:
        result, description = mysql_util.execute_and_fetch_query(query)
        field_names = [i[0] for i in description]
        out_record = []
        for row in result:
            out_dictionary = dict(zip(field_names, row))
            out_record.append(out_dictionary)
    # raise("exception")
        return {"status": 200, "message": "OK", "data": out_record}
    except Exception as e:
        return {"status": 400, "message": "Error: {}".format(e), "data": id}


@app.post("/add_books/")
def create_book(book: Book):
    """
    to insert a create book to db
    :param book: book object to insert
    :return:
    """
    book_set = (book.author, book.title, book.image, book.quantity, book.price, book.description,)
    query = "insert into books(`author`, `title`, `image`, `quantity`, `price`, `description`) values(%s,%s," \
            "%s,%s,%s,%s) "
    try:
        mysql_util.execute_query(query, book_set)
        return {"status": 201, "message": "OK", "data": book_set}
    except Exception as e:
        return {"status": 400, "message": "Error: {}".format(e), "data": e}


@app.post("/add_books_csv/")
def create_book_csv(file: UploadFile = File(...)):
    """
    to add csv file to db
    :param file: csv file to be inserted
    :return:
    """
    if file.content_type == "text/csv":
        contents = file.read()
        df = to_df(file)
        try:
            mysql_util.read_csv_and_insert_to_db(df, "books")
            return {"status": 201, "message": "OK", "data": df.to_dict()}
        except Exception as e:
            return {"status": 400, "message": "Error: {}".format(e), "data": df.to_dict()}

    return {"status": 400, "message": "Error: {}".format("Invalid file type."), "data": None}


@app.delete('/delete_books/{id}')
def delete_book(id: int):
    """
    to delete an entry from db
    :param id: book id to delete
    :return:
    """
    query = "delete from books where id={}".format(id)
    try:
        mysql_util.execute_query(query)
        return {"status": 202, "message": "OK", "data": id}
    except Exception as e:
        return {"status": 400, "message": "Error: {}".format(e), "data": id}


@app.put("/update_books/{id}")
def update_book(id: int, book: Book):
    """
    to update an entry in db
    :param id: id of the book update
    :param book: book object to replace old values
    :return:
    """
    book_set = (book.author, book.title, book.image, book.quantity, book.price, book.description,)
    if book.author.isalpha():
        query = "update books set `author` = %s, `title` = %s, `image` = %s, `quantity` = %s, `price` = %s, " \
                "`description` = %s where id={}".format(id)
        try:
            mysql_util.execute_query(query, book_set)
            return {"status": 201, "message": "OK", "data": book_set}
        except Exception as e:
            return {"status": 400, "message": "Error: {}".format(e), "data": book_set}
    return {"status": 400, "message": "Error: {}".format("Invalid author"), "data": book_set}