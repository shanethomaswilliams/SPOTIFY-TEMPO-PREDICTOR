import db_connect
import query


default_audio_features = {
    'tempo': None,
    'key': -1,
    'mode': -1,
    'acousticness': None,
    'danceability': None,
    'energy': None,
    'instrumentalness': None,
    'liveness': None,
    'valence': None
}


def extract_album_tuples(items):
    values = list()
    for obj in items:
        date = obj['release_date']
        while date.count("-") < 2:
            date = date + "-1"
        values.append((obj['id'], obj['name'], obj['popularity'],
                       date, obj['release_date_precision']))
    return values


def album_tuple_command():
    return "INSERT INTO Album VALUES (%s, %s, %s, %s, %s)"


def extract_artist_tuples(items):
    values = list()
    for obj in items:
        values.append((obj['id'], obj['name'], obj['followers']['total'],
                       obj['popularity']))
    return values


def artist_tuple_command():
    return "INSERT IGNORE INTO Artist VALUES (%s, %s, %s, %s)"


# takes in album objects, where the artist objects should already exist
def extract_artist_for_album_tuples(items):
    values = list()
    for obj in items:
        album_id = obj['id']
        for artist in obj['artists']:
            values.append((album_id, artist['id']))
    return values


def artist_for_album_tuple_command():
    return "INSERT IGNORE INTO Artist_For_Album VALUES (%s, %s)"


# takes in track objects, where the artist objects already exist
def extract_artist_for_track_tuples(items):
    values = list()
    for obj in items:
        track_id = obj[0]['id']
        for artist in obj[0]['artists']:
            values.append((track_id, artist['id']))
    return values


def artist_for_track_tuple_command():
    return "INSERT IGNORE INTO Artist_For_Track VALUES (%s, %s)"


# takes in artist objects, returns a list of 2 lists
# the first sub-list is for Genre, the second is for Artist_In_Genre
def extract_genre_from_artists(items):
    values = [[], []]
    for artist_obj in items:
        artist_id = artist_obj['id']
        for genre_string in artist_obj['genres']:
            values[0].append((genre_string,))
            values[1].append((artist_id, genre_string))
    return values


def genre_tuple_command():
    return "INSERT IGNORE INTO Genre VALUES (%s)"


def artist_in_genre_tuple_command():
    return "INSERT INTO Artist_In_Genre VALUES (%s, %s)"


# takes in album objects, returns a list of 2 lists
# the first sub-list is for Genre, the second is for Album_In_Genre
def extract_genre_from_album(items):
    values = [[], []]
    for album_obj in items:
        album_id = album_obj['id']
        for genre_string in album_obj['genres']:
            values[0].append(genre_string)
            values[1].append((album_id, genre_string))
    return values


def album_in_genre_tuple_command():
    return "INSERT INTO Album_In_Genre VALUES (%s, %s)"


def convert_tempo(api_value):
    if api_value is None:
        return None
    else:
        return round(api_value, 2)


def note_int_to_string(note):
    if note == 0:
        return "C"
    elif note == 1:
        return "C#"
    elif note == 2:
        return "D"
    elif note == 3:
        return "D#"
    elif note == 4:
        return "E"
    elif note == 5:
        return "F"
    elif note == 6:
        return "F#"
    elif note == 7:
        return "G"
    elif note == 8:
        return "G#"
    elif note == 9:
        return "A"
    elif note == 10:
        return "A#"
    elif note == 11:
        return "B"
    else:
        return None


def mode_int_to_string(mode):
    if mode == 1:
        return "Major"
    elif mode == 0:
        return "Minor"
    else:
        return None


def extract_track_tuples(items):
    values = list()
    for obj in items:
        track = obj[0]
        features = obj[1]
        if features is None:
            features = default_audio_features
        values.append((track['id'], track['name'], track['album']['id'],
                       track['duration_ms'], track['track_number'],
                       track['disc_number'], track['popularity'],
                       convert_tempo(features['tempo']),
                       note_int_to_string(features['key']),
                       mode_int_to_string(features['mode']),
                       features['acousticness'], features['danceability'],
                       features['energy'], features['instrumentalness'],
                       features['liveness'], features['valence']))
    return values


def track_tuple_command():
    return "INSERT INTO Track VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
           " %s, %s, %s, %s, %s, %s)"


def is_ascii(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True


def album_query(limit, offset):
    params = {
        'type': 'album',
        'q': 'year:2019',
        'limit': str(limit),
        'offset': str(offset)
    }
    return query.run_search_query(params)


def get_popular_albums():
    limit = 50
    offset = 0
    popular = list()
    result = album_query(limit, offset)
    while result.status_code == 200:
        items = result.json()['albums']['items']
        album_ids = list()
        for item in items:
            album_ids.append(item['id'])
        full_albums = []
        full_albums.extend(query.get_full_albums(album_ids[0:20]))
        full_albums.extend(query.get_full_albums(album_ids[20:40]))
        full_albums.extend(query.get_full_albums(album_ids[40:]))
        for full_item in full_albums:
            if full_item is not None \
                    and full_item['popularity'] >= 75 \
                    and is_ascii(full_item['name']):
                popular.append(full_item)
        offset += limit
        result = album_query(limit, offset)
    return popular


def get_artists_from_albums(albums):
    artists = list()
    for item in albums:
        for artist in item['artists']:
            if is_ascii(artist['name']):
                artists.append(query.get_artist(artist['id']).json())
    return artists


def get_tracks_from_albums(albums):
    tracks = list()
    for item in albums:
        track_ids = list()
        for track in item['tracks']['items']:
            if is_ascii(track['name']):
                track_ids.append(track['id'])
        tracks.extend(query.get_tracks(track_ids))
    return tracks


def load_database():
    db = db_connect.connect_to_db()
    cursor = db.cursor()
    # get the albums
    albums = get_popular_albums()
    values = extract_album_tuples(albums)
    cursor.executemany(album_tuple_command(), values)
    db.commit()
    # get the genres from albums and the album_in_genre relationship
    values = extract_genre_from_album(albums)
    cursor.executemany(genre_tuple_command(), values[0])
    cursor.executemany(album_in_genre_tuple_command(), values[1])
    print("albums done. loading artists...")
    # get the artists for those albums
    artists = get_artists_from_albums(albums)
    values = extract_artist_tuples(artists)
    cursor.executemany(artist_tuple_command(), values)
    db.commit()
    # get the artist_for_album relationship
    values = extract_artist_for_album_tuples(albums)
    cursor.executemany(artist_for_album_tuple_command(), values)
    db.commit()
    # get the genres from artists and the artist_in_genre relationship
    values = extract_genre_from_artists(artists)
    cursor.executemany(genre_tuple_command(), values[0])
    cursor.executemany(artist_in_genre_tuple_command(), values[1])
    db.commit()
    print("artists done. loading tracks...")
    # get the tracks on those albums
    tracks = get_tracks_from_albums(albums)
    values = extract_track_tuples(tracks)
    cursor.executemany(track_tuple_command(), values)
    db.commit()
    # get the artist_for_track relationship
    values = extract_artist_for_track_tuples(tracks)
    cursor.executemany(artist_for_track_tuple_command(), values)
    db.commit()
    print("tracks done")


load_database()
