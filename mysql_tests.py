import db_connect
import query
import schema


def test_select():
    db = db_connect.connect_to_db()
    cursor = db.cursor()
    command = "SELECT * FROM Dorm"
    cursor.execute(command)
    return cursor.fetchall()


def test_spotify_query():
    params = {
        'type': 'album',
        'q': 'artist:\"cory wong\"',
        'limit': '1'
    }
    return query.run_query(params)


def test_table_creation():
    db = db_connect.connect_to_db()
    schema.create_tables(db)


def test_insert_from_spotify():
    params = {
        'type': 'album',
        'q': 'year:2019'
    }
    spotify_output = query.run_query(params).json()
    test_obj = spotify_output['artists']['items'][0]
    db = db_connect.connect_to_db()
    cursor = db.cursor()
    command = "INSERT INTO Artist VALUES (%s, %s, %s, %s)"
    values = (test_obj['id'], test_obj['name'], test_obj['followers']['total'],
              test_obj['popularity'])
    cursor.execute(command, values)
    db.commit()


print(test_spotify_query().text)
