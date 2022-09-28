import db_connect
import query
import csv
import pandas as pd

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


## Extracting from CSV files
with open('voice.csv', newline='') as f:
    reader = csv.reader(f)
    voice = list(reader)

def voice_tuple_command():
    return "INSERT IGNORE INTO Voice VALUES (%s)"



with open('instrument.csv', newline='') as f:
    reader = csv.reader(f)
    instrument = list(reader)

def instrument_tuple_command():
    return "INSERT IGNORE INTO Instrument VALUES (%s)"



with open('award.csv', newline='') as f:
    reader = csv.reader(f)
    award = list(reader)

def award_tuple_command():
    return "INSERT IGNORE INTO Award VALUES (%s)"



with open('artist_award.csv', newline='') as f:
    reader = csv.reader(f)
    artist_award = list(reader)

def artist_award_tuple_command():
    return "INSERT IGNORE INTO Artist_Award VALUES (%s, %s)"



with open('artist_voice.csv', newline='') as f:
    reader = csv.reader(f)
    artist_voice = list(reader)

def artist_voice_tuple_command():
    return "INSERT IGNORE INTO Artist_Voice VALUES (%s, %s)"



with open('artist_inst.csv', newline='') as f:
    reader = csv.reader(f)
    artist_inst = list(reader)

def artist_instrument_tuple_command():
    return "INSERT IGNORE INTO Plays_Instrument VALUES (%s, %s)"



with open('artist_inf.csv', newline='') as f:
    reader = csv.reader(f)
    artist_inf = list(reader)

def artist_influence_tuple_command():
    return "INSERT IGNORE INTO Artist_Influenced_By VALUES (%s, %s)"



with open('artist_mem.csv', newline='') as f:
    reader = csv.reader(f)
    artist_mem = list(reader)

def artist_member_tuple_command():
    return "INSERT IGNORE INTO Artist_Award VALUES (%s, %s)"



with open('artist_stud.csv', newline='') as f:
    reader = csv.reader(f)
    artist_stud = list(reader)

def artist_student_tuple_command():
    return "INSERT IGNORE INTO Artist_Student VALUES (%s, %s)"


## Adding age field to Artist Table
artist_age = pd.read_csv("artist_age.csv")
new_age = []
for x in artist_age.values:
    new_age.append((x[1], x[0]))
print(new_age)
    

def load_database():
    db = db_connect.connect_to_db()
    cursor = db.cursor()
    cursor.execute("ALTER TABLE Artist ADD COLUMN Age INTEGER AFTER Popularity");
    cursor.executemany("UPDATE Artist SET Age = %s WHERE ID=%s", new_age)
    db.commit()
    # upload the voice
    cursor.executemany(voice_tuple_command(), voice)
    db.commit()
    # upload instrument
    cursor.executemany(instrument_tuple_command(), instrument)
    db.commit()
    # puload award
    cursor.executemany(award_tuple_command(), award)
    db.commit()
    # upload artist voice
    cursor.executemany(artist_voice_tuple_command(), artist_voice)
    db.commit()
    # upload artist instrument
    cursor.executemany(artist_instrument_tuple_command(), artist_inst)
    db.commit()
    # upload artist award
    cursor.executemany(artist_award_tuple_command(), artist_award)
    db.commit()
    # upload artist influence
    cursor.executemany(artist_influence_tuple_command(), artist_inf)
    db.commit()
    # upload artist student
    cursor.executemany(artist_student_tuple_command(), artist_stud)
    db.commit()
    # upload artist member
    cursor.executemany(artist_member_tuple_command(), artist_mem)
    db.commit()
    
load_database()
