FROM python

COPY ./meter_software/ /app/meter_software/
COPY ./meter_software_run.py /app/run.py
COPY ./meter_software_init.py /app/init.py
COPY ./requirements_meter_software.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "run.py"]
# replace with init.sh