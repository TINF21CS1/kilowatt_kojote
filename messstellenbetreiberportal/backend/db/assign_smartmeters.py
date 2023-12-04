from . import db_manager
import os
import sqlite3

# Here, the database is in a subdirectory to work with the docker stuff
db_path = os.path.join(os.path.dirname(__file__), "db/database.db")

if __name__ == "__main__":

    supplier_serial = "138874517316312474711892333607071236412270376730"

    query = "SELECT serial_number FROM Stromzaehler;"

    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    res = cursor.execute(query)
    smartmeters = res.fetchall()

    for smartmeter in smartmeters:
        db_manager.frontend_supplier_assign(supplier_serial, smartmeter)

    