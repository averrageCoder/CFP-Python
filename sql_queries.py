create_movies_table_query = """
    CREATE TABLE if not exists movies(
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100),
        release_year YEAR(4),
        genre VARCHAR(100),
        collection_in_mil INT
    )
"""

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

show_table_query = "DESCRIBE movies"

insert_reviewers_query = {
    "query": """
        INSERT INTO reviewers
        (first_name, last_name)
        VALUES ( %s, %s )
        """,
    "values": [
        ("Chaitanya", "Baweja"),
        ("Mary", "Cooper"),
        ("Marlon", "Crafford")
    ]
}

insert_movies_query = """
INSERT INTO movies (title, release_year, genre, collection_in_mil)
VALUES
    ("Forrest Gump", 1994, "Drama", 330.2),
    ("3 Idiots", 2009, "Drama", 2.4),
    ("Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5),
    ("Gladiator", 2000, "Action", 188.7)
"""

insert_ratings_query = {
    "query": """
        INSERT INTO ratings
        (rating, movie_id, reviewer_id)
        VALUES ( %s, %s, %s)
    """,
    "values": [
        (6.4, 1, 2), (5.6, 1, 1), (6.3, 2, 3),
        (6.4, 3, 1), (8.1, 4, 2), (5.7, 2, 2),
        (9.8, 3, 3)
    ]
}

create_reviewers_table_query = """
    CREATE TABLE if not exists reviewers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100)
    )
"""

# id,author,title,image,quantity,price,description
create_books_table_query = """
    CREATE TABLE if not exists books (
        id INT,
        author VARCHAR(100),
        title VARCHAR(100),
        image VARCHAR(100),
        quantity INT,
        price NUMERIC,
        description TEXT
    )
"""

select_query_with_join = """
select m.title, r.first_name, ra.rating   
from reviewers r, ratings ra, movies m
where ra.movie_id = m.id and ra.reviewer_id = r.id
"""

update_query = """
update reviewers
set first_name='Harsh', last_name='R'
where id=2
"""

delete_query = """
delete from reviewers where id=129
"""