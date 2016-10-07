# Take a csv file and transform into a sqlite table
# asks for the file to input and create a new file.sqlite
# asks for complete cases (no NA)

import csv
import sqlite3


print "\nHello!\n This program takes a CSV file cleans it from NA values and puts into a table (SQLITE) format\n for easy viewing."

conn = sqlite3.connect('tdgunlaws.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Gunlaws;

CREATE TABLE Gunlaws (
    year     INTEGER,
    id       INTEGER NOT NULL,
    sex      TEXT,
    race     TEXT,
    age      INTEGER,
    region   TEXT,

    gunlaw   TEXT
)
''')

with open('tdgunlaw.csv', 'rb') as csvfile:
    gunlaws = csv.reader(csvfile, delimiter=',')
    next(gunlaws)
    for entry in gunlaws:
        year     = entry[1];
        uniqueid = entry[2];
        sex      = entry[3];
        race     = entry[4];
        age      = entry[5];
        region   = entry[6];

        gunlaw   = entry[7];
        print year

        cur.execute('''INSERT INTO Gunlaws (year, id, sex, race, age, region, gunlaw) VALUES ( ?, ?, ?, ?, ?, ?, ? )''', (year, uniqueid, sex, race, age, region, gunlaw))
        cur.execute('''DELETE FROM Gunlaws WHERE gunlaw = 'NA' OR year = 'NA' OR sex = 'NA' OR race = 'NA' OR age = 'NA' OR region = 'NA'; ''')
        conn.commit()
