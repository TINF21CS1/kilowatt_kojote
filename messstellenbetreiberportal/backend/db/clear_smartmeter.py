import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "database.db")

if __name__ == "__main__":
    query = "DELETE FROM Stromzaehler; VACUUM;"

    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    res = cursor.execute(query)
    con.commit()