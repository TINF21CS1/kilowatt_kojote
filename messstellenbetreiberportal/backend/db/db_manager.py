import os
import sqlite3

con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "database.db"))
cursor = con.cursor()

def smartmeter_register(uuid, type):

    query = "INSERT INTO Stromzaehler (serial_number, counter_type) VALUES(?, ?);"
    try:
        cursor.execute(query, (uuid, type))
        con.commit()
    except sqlite3.IntegrityError:
        # Don't return error so that an attacker, having compormised a reader, does not get any feedback as to whether their operation worked
        print("Integrity error")
        pass

def init_db():

    with open(os.path.join(os.path.dirname(__file__), "schema.sql")) as schema:
        con.executescript(schema.read())
        con.commit()

if __name__ == "__main__":
    init_db()
