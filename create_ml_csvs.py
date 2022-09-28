import db_connect
import csv
import pandas as pd

def Artists_select():
    db = db_connect.connect_to_db()
    cursor = db.cursor()
    command = "SELECT A.*, B.num_award FROM (SELECT Artist.*, count(ID) AS num_inst FROM Artist LEFT JOIN Plays_Instrument ON Artist.ID=Plays_Instrument.Artist_Id GROUP BY ID) AS A LEFT JOIN (SELECT Artist.*, count(Award) AS num_award FROM Artist JOIN Artist_Award ON Artist.ID=Artist_Award.Artist_Id GROUP BY Artist.ID) AS B ON A.ID=B.ID"
    cursor.execute(command)
    return cursor.fetchall()

def Track_select():
    db = db_connect.connect_to_db()
    cursor = db.cursor()
    command = "SELECT Artist_ID, Avg(Tempo) FROM (SELECT Track.Tempo, Artist_For_Album.Artist_ID FROM Track JOIN Artist_For_Album ON Track.Album_ID=Artist_For_Album.Album_ID) AS A GROUP BY Artist_ID"
    cursor.execute(command)
    return cursor.fetchall()

artists = Artists_select()
tracks = Track_select()

ml_artist = pd.DataFrame(artists)
ml_track = pd.DataFrame(tracks)

ml_artist.to_csv("ml_artists.csv", index=False)
ml_track.to_csv("ml_track.csv", index=False)
