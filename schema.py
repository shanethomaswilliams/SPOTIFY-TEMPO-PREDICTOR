import db_connect


def drop_all_tables(cursor):
    cursor.execute("DROP TABLE IF EXISTS Plays_Instrument")
    cursor.execute("DROP TABLE IF EXISTS Instrument")
    cursor.execute("DROP TABLE IF EXISTS Artist_Voice")
    cursor.execute("DROP TABLE IF EXISTS Voice")
    cursor.execute("DROP TABLE IF EXISTS Artist_Influenced_By")
    cursor.execute("DROP TABLE IF EXISTS Artist_Award")
    cursor.execute("DROP TABLE IF EXISTS Award")
    cursor.execute("DROP TABLE IF EXISTS Artist_Member")
    cursor.execute("DROP TABLE IF EXISTS Artist_Student")
    cursor.execute("DROP TABLE IF EXISTS Album_In_Genre")
    cursor.execute("DROP TABLE IF EXISTS Artist_In_Genre")
    cursor.execute("DROP TABLE IF EXISTS Genre")
    cursor.execute("DROP TABLE IF EXISTS Artist_For_Album")
    cursor.execute("DROP TABLE IF EXISTS Artist_For_Track")
    cursor.execute("DROP TABLE IF EXISTS Track")
    cursor.execute("DROP TABLE IF EXISTS Album")
    cursor.execute("DROP TABLE IF EXISTS Artist")
    
    
def create_album_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS Album")
    create_album = "CREATE TABLE Album ( ID VARCHAR(22) NOT NULL, " \
                   "Name VARCHAR(255) NOT NULL, " \
                   "Popularity INTEGER NOT NULL, " \
                   "Release_Date DATE NOT NULL, " \
                   "Date_Precision VARCHAR(5) NOT NULL, " \
                   "PRIMARY KEY (ID) )"
    cursor.execute(create_album)


def create_album_in_genre_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS Album_In_Genre")
    create_aig = "CREATE TABLE Album_In_Genre ( Album_ID VARCHAR(22) NOT NULL, " \
                 "Genre VARCHAR(63) NOT NULL, " \
                 "FOREIGN KEY (Album_ID) REFERENCES Album(ID), " \
                 "FOREIGN KEY (Genre) REFERENCES Genre(Name) )"
    cursor.execute(create_aig)


def create_artist_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS Artist")
    create_artist = "CREATE TABLE Artist ( ID VARCHAR(22) NOT NULL, " \
                    "Name VARCHAR(255) NOT NULL, " \
                    "Num_Followers INTEGER NOT NULL, " \
                    "Popularity INTEGER NOT NULL, " \
                    "PRIMARY KEY (ID) )"
    cursor.execute(create_artist)


def create_artist_in_genre_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS Artist_In_Genre")
    create_aig = "CREATE TABLE Artist_In_Genre ( Artist_ID VARCHAR(22) NOT NULL, " \
                 "Genre VARCHAR(63) NOT NULL, " \
                 "FOREIGN KEY (Artist_ID) REFERENCES Artist(ID), " \
                 "FOREIGN KEY (Genre) REFERENCES Genre(Name) )"
    cursor.execute(create_aig)


def create_artist_for_album_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS Artist_For_Album")
    create_afa = "CREATE TABLE Artist_For_Album ( Album_ID VARCHAR(22) NOT NULL, " \
                 "Artist_ID VARCHAR(22) NOT NULL, " \
                 "FOREIGN KEY (Album_ID) REFERENCES Album(ID), " \
                 "FOREIGN KEY (Artist_ID) REFERENCES Artist(ID) )"
    cursor.execute(create_afa)


def create_artist_for_track_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS Artist_For_Track")
    create_aft = "CREATE TABLE Artist_For_Track ( Track_ID VARCHAR(22) NOT NULL, " \
                 "Artist_ID VARCHAR(22) NOT NULL, " \
                 "FOREIGN KEY (Track_ID) REFERENCES Track(ID), " \
                 "FOREIGN KEY (Artist_ID) REFERENCES Artist(ID) )"
    cursor.execute(create_aft)


def create_genre_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS Genre")
    create_genre = "CREATE TABLE Genre ( Name VARCHAR(63)," \
                   "PRIMARY KEY (Name) )"
    cursor.execute(create_genre)


def create_track_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS Track")
    create_track = "CREATE TABLE Track ( ID VARCHAR(22) NOT NULL, " \
                   "Name VARCHAR(255) NOT NULL, " \
                   "Album_ID VARCHAR (22) NOT NULL, " \
                   "Duration INTEGER NOT NULL, " \
                   "Number INTEGER NOT NULL, " \
                   "Disc INTEGER, " \
                   "Popularity INTEGER NOT NULL, " \
                   "Tempo DECIMAL(5, 2), " \
                   "Key_Root VARCHAR(2), " \
                   "Key_Mode VARCHAR(5), " \
                   "Acousticness DECIMAL(5, 4), " \
                   "Danceability DECIMAL(5, 4), " \
                   "Energy DECIMAL(5, 4), " \
                   "Instrumentalness DECIMAL(5, 4), " \
                   "Liveness DECIMAL(5, 4), " \
                   "Valence DECIMAL(5, 4), " \
                   "PRIMARY KEY (ID)," \
                   "FOREIGN KEY (Album_ID) REFERENCES Album(ID) )"
    cursor.execute(create_track)


def create_instrument_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS Instrument")
    create_instrument = "CREATE TABLE Instrument ( Name VARCHAR(63)," \
                   "PRIMARY KEY (Name) )"
    cursor.execute(create_instrument)

def create_artist_instrument_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS Plays_Instrument")
    create_ainst = "CREATE TABLE Plays_Instrument ( Artist_ID VARCHAR(22) NOT NULL, " \
                 "Instrument VARCHAR(63) NOT NULL, " \
                 "FOREIGN KEY (Artist_ID) REFERENCES Artist(ID), " \
                 "FOREIGN KEY (Instrument) REFERENCES Instrument(Name) )"
    cursor.execute(create_ainst)

def create_artist_voice_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS Voice")
    create_voice = "CREATE TABLE Voice ( Name VARCHAR(63)," \
                   "PRIMARY KEY (Name) )"
    cursor.execute(create_voice)

def create_voice_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS Artist_Voice")
    create_avoice = "CREATE TABLE Artist_Voice ( Artist_ID VARCHAR(22) NOT NULL, " \
                 "Voice VARCHAR(63) NOT NULL, " \
                 "FOREIGN KEY (Artist_ID) REFERENCES Artist(ID), " \
                 "FOREIGN KEY (Voice) REFERENCES Voice(Name) )"
    cursor.execute(create_avoice)

def create_artist_influenced(cursor):
    cursor.execute("DROP TABLE IF EXISTS Artist_Influenced_By")
    create_ainf = "CREATE TABLE Artist_Influenced_By ( Artist_ID VARCHAR(22) NOT NULL, " \
                 "Influenced_By VARCHAR(63) NOT NULL, " \
                 "FOREIGN KEY (Artist_ID) REFERENCES Artist(ID), " \
                 "FOREIGN KEY (Influenced_By) REFERENCES Artist(ID) )"
    cursor.execute(create_ainf)

def create_artist_member(cursor):
    cursor.execute("DROP TABLE IF EXISTS Artist_Member")
    create_amem = "CREATE TABLE Artist_Member ( Artist_ID VARCHAR(22) NOT NULL, " \
                 "Member_Of VARCHAR(63) NOT NULL, " \
                 "FOREIGN KEY (Artist_ID) REFERENCES Artist(ID), " \
                 "FOREIGN KEY (Member_Of) REFERENCES Artist(ID) )"
    cursor.execute(create_amem)

def create_artist_student(cursor):
    cursor.execute("DROP TABLE IF EXISTS Artist_Student")
    create_astud = "CREATE TABLE Artist_Student ( Artist_ID VARCHAR(22) NOT NULL, " \
                 "Student_Of VARCHAR(63) NOT NULL, " \
                 "FOREIGN KEY (Artist_ID) REFERENCES Artist(ID), " \
                 "FOREIGN KEY (Student_Of) REFERENCES Artist(ID) )"
    cursor.execute(create_astud)

def create_artist_award(cursor):
    cursor.execute("DROP TABLE IF EXISTS Artist_Award")
    create_aaward = "CREATE TABLE Artist_Award ( Artist_ID VARCHAR(22) NOT NULL, " \
                 "Award VARCHAR(63) NOT NULL, " \
                 "FOREIGN KEY (Artist_ID) REFERENCES Artist(ID), " \
                 "FOREIGN KEY (Award) REFERENCES Award(Name) )"
    cursor.execute(create_aaward)

def create_award(cursor):
    cursor.execute("DROP TABLE IF EXISTS Award")
    create_award = "CREATE TABLE Award ( Name VARCHAR(63)," \
                   "PRIMARY KEY (Name) )"
    cursor.execute(create_award)
    
def create_all_tables(db):
    cursor = db.cursor()
    drop_all_tables(cursor)  # does so in a safe way for foreign keys
    create_artist_table(cursor)
    create_album_table(cursor)
    create_track_table(cursor)
    create_genre_table(cursor)
    create_album_in_genre_table(cursor)
    create_artist_in_genre_table(cursor)
    create_artist_for_album_table(cursor)
    create_artist_for_track_table(cursor)
    create_instrument_table(cursor)
    create_artist_instrument_table(cursor)
    create_artist_voice_table(cursor)
    create_voice_table(cursor)
    create_artist_influenced(cursor)
    create_award(cursor)
    create_artist_award(cursor)
    create_artist_member(cursor)
    create_artist_student(cursor)
    

create_all_tables(db_connect.connect_to_db())
