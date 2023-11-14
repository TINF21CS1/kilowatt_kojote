import os
import sqlite3

def smartmeter_register(uuid, type):

    query = "INSERT OR IGNORE INTO Stromzaehler (serial_number, counter_type) VALUES(?, ?);"

    con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "database.db"))
    cursor = con.cursor()

    cursor.execute(query, (uuid, type))
    con.commit()
    cursor.close()

def smartmeter_data(uuid, timestamp, actual_timestamp, reading):

    query = "INSERT OR IGNORE INTO Zaehlerstaende (uuid, record_timestamp, actual_timestamp, reading) VALUES(?, ?, ?, ?);"

    con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "database.db"))
    cursor = con.cursor()

    cursor.execute(query, (uuid, timestamp, actual_timestamp, reading))
    con.commit()
    cursor.close()


def init_db():

    con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "database.db"))

    with open(os.path.join(os.path.dirname(__file__), "schema.sql")) as schema:
        con.executescript(schema.read())
        con.commit()

if __name__ == "__main__":
    init_db()
