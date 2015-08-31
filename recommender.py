# -*- coding: utf-8 -*-

from math import sqrt
from sqlite3 import dbapi2 as sqlite
import os

dirpath = os.path.dirname(os.path.abspath(__file__))

movielens_db = "movielens.db"

class criticsDB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite.connect(dirpath + "/db/" + db_name)

    def __del__(self):
        self.connection.close()

    def db_commit(self):
        self.connection.commit()

    def select_entry_id(self, table, column, value):
        table = self.connection.execute("select rowid from %s where %s = '%s'"
                                        % (table, column, value))
        result = table.fetchone()
        if result is None:
            return None
        else:
            return result[0]

    def insert_entry_id(self, table, column, value):
        result = self.select_entry_id(table, column, value)
        if result is None:
            table = self.connection.execute("insert into %s (%s) values ('%s')"
                                        % (table, column, value))
            return table.lastrowid
        else:
            result

    def get_user_id(self, user):
        return self.select_entry_id("userlist", "name", user)

    def add_user(self, user):
        return self.insert_entry_id("userlist", "name", user)

    def get_movie_id(self, movie):
        return self.select_entry_id("movielist", "name", movie)

    def add_movie(self, movie):
        return self.insert_entry_id("movielist", "name", movie)

    def get_score_id(self, user, movie):
        user_id = self.get_user_id(user)
        movie_id = self.get_movie_id(movie)
        table = self.connection.execute("select rowid from scorelist where userid = %s and movieid = %s"
                                        % (user_id, movie_id))
        result = table.fetchone()
        if result is None:
            return None
        else:
            return result[0]

    def add_score(self, user, movie, score):
        user_id = self.get_user_id(user)
        if user_id is None:
            user_id = self.add_user(user)

        movie_id = self.get_movie_id(movie)
        if movie_id is None:
            movie_id = self.add_movie(movie)

        score_id = self.get_score_id(user, movie)
        if score_id is None:
            table = self.connection.execute("insert into scorelist (userid, movieid, score) values (%d, %d, %f)"
                                            % (user_id, movie_id, score))
            return table.lastrowid
        else:
            table = self.connection.execute("update scorelist set score = %f where userid=%d and movieid=%d"
                                            % (score, user_id, movie_id))
            return score_id


    def store_data(self, data):
        """
        data : dict[ critic -> dict[ movie -> score ]  ]
        @critic is a string
        @movie is a string
        @score is a float
        """
        for user in data:
            for movie in data[user]:
                self.add_score(user, movie, data[user][movie])
        self.db_commit()

    def db_create_tables(self):
        self.connection.execute("create table userlist(name)")
        self.connection.execute("create table movielist(name)")
        self.connection.execute("create table scorelist(userid, movieid, score)")
        self.connection.execute("create index useridx on userlist(name)")
        self.connection.execute("create index movieidx on movielist(name)")
        self.connection.execute("create index userscoridx on scorelist(userid)")
        self.connection.execute("create index moviescoreidx on scorelist(movieid)")
        self.db_commit()

    
