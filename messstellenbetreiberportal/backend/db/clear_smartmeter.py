import sqlite3
import os

# Here, the database is in a subdirectory to work with the docker stuff
db_path = os.path.join(os.path.dirname(__file__), "db/database.db")

if __name__ == "__main__":
    query = "DELETE FROM Stromzaehler;"

    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    cursor.execute(query)
    con.commit()
    
    cursor.execute("VACUUM;")
