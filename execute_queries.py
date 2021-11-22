from connect_to_mysql import get_connection
from dotenv import dotenv_values

config = dotenv_values(".env")
HOST = config["HOST"]
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']
DATABASE = config['DATABASE']

if __name__ == "__main__":
    connection = get_connection(HOST, USERNAME, PASSWORD, DATABASE)
    create_movies_table_query = """
    CREATE TABLE if not exists movies(
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100),
        release_year YEAR(4),
        genre VARCHAR(100),
        collection_in_mil INT
    )
    """
    cursor = connection.cursor()
    cursor.execute(create_movies_table_query)
    connection.commit()

    create_reviewers_table_query = """
    CREATE TABLE if not exists reviewers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100)
    )
    """
    cursor.execute(create_reviewers_table_query)
    connection.commit()

    create_ratings_table_query = """
    CREATE TABLE if not exists ratings (
        movie_id INT,
        reviewer_id INT,
        rating DECIMAL(2,1),
        FOREIGN KEY(movie_id) REFERENCES movies(id),
        FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
        PRIMARY KEY(movie_id, reviewer_id)
    )
    """
    cursor.execute(create_ratings_table_query)
    connection.commit()

    show_table_query = "DESCRIBE movies"
    cursor.execute(show_table_query)
    result = cursor.fetchall()
    for row in result:
        print(row)

    insert_reviewers_query = """
    INSERT INTO reviewers
    (first_name, last_name)
    VALUES ( %s, %s )
    """
    reviewers_records = [
        ("Chaitanya", "Baweja"),
        ("Mary", "Cooper"),
        ("Marlon", "Crafford"),
    ]

    cursor.executemany(insert_reviewers_query, reviewers_records)
    connection.commit()