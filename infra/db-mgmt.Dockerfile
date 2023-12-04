FROM debian

RUN apt update && apt install sqlite3 nano python3 -y

COPY ./messstellenbetreiberportal/backend/db/clear_smartmeter.py /clear_smartmeter.py
COPY ./messstellenbetreiberportal/backend/db/assign_smartmeters.py /assign_smartmeters.py
COPY ./messstellenbetreiberportal/backend/db/db_manager.py /db_manager.py
