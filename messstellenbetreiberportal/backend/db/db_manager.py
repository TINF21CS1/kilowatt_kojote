import os
import sqlite3

# TODO: check_supplier_owns_reader fertigstellen und supplier_reading_history fertigstellen und in supplier.py funktion beide aufrufen und checken ob dem supplier der stromzähler zugeordnet ist. Außerdem noch in allen funktionen die integration mit den headern die von nginx mitkommen fertigstellen, sodass supplier_serial und stromzähler uuid direkt daraus gelesen und verwendet werden

def smartmeter_register(serial_number, type):

    query = "INSERT OR IGNORE INTO Stromzaehler (serial_number, counter_type) VALUES(?, ?);"

    con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "database.db"))
    cursor = con.cursor()

    cursor.execute(query, (serial_number, type))
    con.commit()
    cursor.close()

def smartmeter_data(serial_number, timestamp, actual_timestamp, reading):

    query = "INSERT OR IGNORE INTO Zaehlerstaende (serial_number, record_timestamp, actual_timestamp, reading) VALUES(?, ?, ?, ?);"

    con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "database.db"))
    cursor = con.cursor()

    cursor.execute(query, (serial_number, timestamp, actual_timestamp, reading))
    con.commit()
    cursor.close()

# Here we only take a uuid, not the supplier id, because it should be checked before if a supplier owns this uuid
def supplier_reading_history(uuid):

    query = "SELECT record_timestamp, reading FROM Zaehlerstaende WHERE serial_number = ?"

    con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "database.db"))
    cursor = con.cursor()

    res = cursor.execute(query, (uuid,))
    return res.fetchall()

def check_supplier_owns_reader(supplier_serial, uuid):
def check_supplier_owns_reader(supplier_serial, serial_number):

    query = "SELECT * FROM Stromzaehler WHERE serial_number = ? AND supplier_serial_number = ?"

    con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "database.db"))
    cursor = con.cursor()

    res = cursor.execute(query, (serial_number, supplier_serial))

    return res.fetchone() is not None

def init_db():

    con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "database.db"))

    with open(os.path.join(os.path.dirname(__file__), "schema.sql")) as schema:
        con.executescript(schema.read())
        con.commit()

if __name__ == "__main__":
    init_db()
