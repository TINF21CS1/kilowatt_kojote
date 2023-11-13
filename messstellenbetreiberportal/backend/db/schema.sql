DROP TABLE IF EXISTS Stromanbieter;
DROP TABLE IF EXISTS Stromzaehler;
DROP TABLE IF EXISTS Zaehlerstaende;

CREATE TABLE Stromanbieter (
  supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
  supplier_name TEXT UNIQUE NOT NULL
);

CREATE TABLE Stromzaehler (
  serial_number TEXT PRIMARY KEY,
  counter_type TINYINT NOT NULL,
  supplier_id INTEGER,
  FOREIGN KEY (supplier_id) REFERENCES Stromanbieter (supplier_id)
);

CREATE TABLE Zaehlerstaende (
  uuid INTEGER NOT NULL,
  record_timestamp INTEGER NOT NULL,
  actual_timestamp INTEGER NOT NULL,
  reading INTEGER,
  FOREIGN KEY (uuid) REFERENCES Stromzaehler (uuid),
  PRIMARY KEY (uuid, record_timestamp)
);