import mysql.connector

host = 'dbase.cs.jhu.edu'
user = '20fa_swill255'
password = 'OQMEGpMevd'
name = '20fa_swill255_db'


def connect_to_db():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=name
    )

