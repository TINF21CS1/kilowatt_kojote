import os
import sqlite3

# TODO: check_supplier_owns_reader fertigstellen und supplier_reading_history fertigstellen und in supplier.py funktion beide aufrufen und checken ob dem supplier der stromzähler zugeordnet ist. Außerdem noch in allen funktionen die integration mit den headern die von nginx mitkommen fertigstellen, sodass supplier_serial und stromzähler uuid direkt daraus gelesen und verwendet werden

db_path = os.path.join(os.path.dirname(__file__), "database.db")

def smartmeter_register(serial_number, type, latitude, longitude):

    query = "INSERT OR IGNORE INTO Stromzaehler (serial_number, counter_type, latitude, longitude) VALUES(?, ?, ?, ?);"

    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    cursor.execute(query, (serial_number, type, latitude, longitude))
    con.commit()
    cursor.close()

def smartmeter_data(serial_number, timestamp, actual_timestamp, reading):

    query = "INSERT OR IGNORE INTO Zaehlerstaende (serial_number, record_timestamp, actual_timestamp, reading) VALUES(?, ?, ?, ?);"

    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    cursor.execute(query, (serial_number, timestamp, actual_timestamp, reading))
    con.commit()
    cursor.close()

# Here we only take a serial number, not the supplier serial number, because it should be checked before if a supplier owns this serial number
def supplier_reading_history(serial_number):

    query = "SELECT record_timestamp, reading FROM Zaehlerstaende WHERE serial_number = ?"

    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    res = cursor.execute(query, (serial_number,))
    return res.fetchall()

def supplier_reading_current(serial_number):

    query = "SELECT MAX(record_timestamp), reading FROM Zaehlerstaende WHERE serial_number = ?"

    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    res = cursor.execute(query, (serial_number,))
    return res.fetchone()

def supplier_smartmeter(supplier_serial):

    query = "SELECT z.serial_number, z.counter_type, z.latitude, z.longitude, a.supplier_name FROM Stromzaehler z INNER JOIN Stromanbieter a ON z.supplier_serial_number = a.supplier_serial_number WHERE z.supplier_serial_number = ?"

    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    res = cursor.execute(query, (supplier_serial,))

    return res.fetchall()

def frontend_smartmeter():

    query = "SELECT z.serial_number, z.counter_type, z.latitude, z.longitude, a.supplier_name FROM Stromzaehler z INNER JOIN Stromanbieter a ON z.supplier_serial_number = a.supplier_serial_number"

    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    res = cursor.execute(query)

    return res.fetchall()

def check_supplier_owns_reader(supplier_serial, serial_number):

    query = "SELECT * FROM Stromzaehler WHERE serial_number = ? AND supplier_serial_number = ?"

    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    res = cursor.execute(query, (serial_number, supplier_serial))

    return res.fetchone() is not None

def init_db():

    con = sqlite3.connect(db_path)

    with open(os.path.join(os.path.dirname(__file__), "schema.sql")) as schema:
        con.executescript(schema.read())
        con.commit()

def init_test_data():

    import random
    
    for i in range(10):
        smartmeter_register(str(i), random.randint(0, 2))

        for j in range(10):
            smartmeter_data(str(i), timestamp := random.randint(5, 1000000000), timestamp, random.randint(1, 1000000))

    

if __name__ == "__main__":
    
    import sys

    init_db()
    if len(sys.argv) > 1 and sys.argv[1] == "-test":
        init_test_data()

        query = "SELECT * FROM Stromzaehler"

        con = sqlite3.connect(db_path)
        cursor = con.cursor()

        res = cursor.execute(query)

        print(res.fetchone())   # fetchone returns one tuple, fetchall a list of tuples
