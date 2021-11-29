from dotenv import dotenv_values
from fastapi import FastAPI
from model import Book

from mysql_util import MySQLUtil

app = FastAPI()
config = dotenv_values(".env")
HOST = config["HOST"]
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']
DATABASE = config['DATABASE']
mysql_util = MySQLUtil(HOST, USERNAME, PASSWORD, DATABASE)


@app.get("/read_books/{id}")
def read_book(id: int):
    out_dictionary = {}
    query = "select * from books where id={}".format(id)
    result, description = mysql_util.execute_and_fetch_query(query)
    field_names = [i[0] for i in description]
    out_record = []
    for row in result:
        out_dictionary = dict(zip(field_names, row))
        out_record.append(out_dictionary)
    return out_record


@app.put("/add_books/")
def create_book(book: Book):
    book_set = (book.id, book.author, book.title, book.image, book.quantity, book.price, book.description,)
    query = "insert into books(`id`, `author`, `title`, `image`, `quantity`, `price`, `description`) values(%s,%s,%s,%s,%s,%s,%s)"
    mysql_util.execute_query(query, book_set)
    return {"status": "success"}


@app.delete('/delete_books/{id}')
def delete_book(id: int):
    query = "delete from books where id={}".format(id)
    mysql_util.execute_query(query)
    return {"status": "success"}


@app.put("/update_books/{id}")
def update_book(id: int, book: Book):
    book_set = (book.id, book.author, book.title, book.image, book.quantity, book.price, book.description,)
    query = "update books set `id` = %s, `author` = %s, `title` = %s, `image` = %s, `quantity` = %s, `price` = %s, " \
            "`description` = %s where id={}".format(id)
    mysql_util.execute_query(query, book_set)
    return {"status": "success"}
