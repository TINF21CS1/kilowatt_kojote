DROP TABLE IF EXISTS Stromanbieter;
DROP TABLE IF EXISTS Stromzaehler;
DROP TABLE IF EXISTS Zaehlerstaende;

CREATE TABLE Stromanbieter (
  supplier_serial_number TEXT PRIMARY KEY,
  supplier_name TEXT UNIQUE NOT NULL
);

CREATE TABLE Stromzaehler (
  serial_number TEXT PRIMARY KEY,
  counter_type TINYINT NOT NULL,
  latitude REAL NOT NULL,
  longitude REAL NOT NULL,
  supplier_serial_number INTEGER,
  FOREIGN KEY (supplier_serial_number) REFERENCES Stromanbieter (supplier_serial_number)
);

CREATE TABLE Zaehlerstaende (
  serial_number INTEGER NOT NULL,
  record_timestamp INTEGER NOT NULL,
  actual_timestamp INTEGER NOT NULL,
  reading INTEGER,
  FOREIGN KEY (serial_number) REFERENCES Stromzaehler (serial_number),
  PRIMARY KEY (serial_number, record_timestamp)
);