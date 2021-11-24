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
        ("Marlon", "Crafford"),
    ]
}

create_reviewers_table_query = """
    CREATE TABLE if not exists reviewers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100)
    )
"""