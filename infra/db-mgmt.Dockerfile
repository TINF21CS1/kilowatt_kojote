FROM debian

COPY ./messstellenbetreiberportal/backend/db/clear_smartmeter.py /clear_smartmeter.py

RUN apt update && apt install sqlite3 nano python3 -y
