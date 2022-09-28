import db_connect
import csv
import pandas as pd

def Artists_select():
    db = db_connect.connect_to_db()
    cursor = db.cursor()
    command = "SELECT ID FROM Artist"
    cursor.execute(command)
    return cursor.fetchall()

artists = Artists_select()

ml_artist = pd.DataFrame(artists)

ml_artist.to_csv("ml_artists.csv", index=False)




