import sqlite3
import atexit
from sqlite3 import Error


class Movie:
    def __init__(self, id, overview, release_date, title, popularity, vote_average, vote_count):
        self.id = id
        self.overview = overview
        self.release_date = release_date
        self.title = title
        self.popularity = popularity
        self.vote_average = vote_average
        self.vote_count = vote_count

class Keyword:
    def __init__(self, id, keyword):
        self.id = id
        self.keyword = keyword

class _Movies:
    def __init__(self, conn):
        self._conn = conn

class _Keywords:
    def __init__(self, conn):
        self.conn = conn

class _Movies_Keywords:
    def __init__(self, conn):
        self.conn = conn

class MovieRepo:
    def __init__(self):
        self._conn = sqlite3.connect("movies.db")
        self.movies = _Movies(self._conn)
        self.keywords = _Keywords(self._conn)
        self.movies_keywords = _Movies_Keywords(self._conn)

    def close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        _create_movies_table(self)
        _create_keywords_table(self)
        _create_movies_keywords_table(self)
        
    def _create_movies_table(self):
        self._conn.execute(""" 
            CREATE TABLE movies (
                id              INT         PRIMARY_KEY,
                overview        TEXT        NOT_NULL,
                release_date    INT         NOT_NULL,
                title           TEXT        NOT_NULL,
                popularity      REAL        NOT_NULL,
                vote_average    REAL        NOT_NuLL,
                vote_count      INT         NOT_NULL
            );
        """)
    def _create_keywords_table(self):
        self._conn.execute(""" 
            CREATE TABLE keywords (
                id              INT         PRIMARY_KEY,
                keyword         TEXT        NOT_NULL    
            )
        """)

    def _create_movies_keywords_table(self):
        self._conn_execute(""" 
            CREATE TABLE movies_keywords (
                movie_id        INT,
                keyword_id      INT,
                PRIMARY_KEY(movie_id, keyword_id)
            )
        """)

    def count_movies(self):
        pass

    def insert_movies(self):
        pass

    def insert_keywords(self):
        pass

    def insert_movie_keywords(self):
        pass

movies_repo = MovieRepo()
atexit.register(movies_repo.close)