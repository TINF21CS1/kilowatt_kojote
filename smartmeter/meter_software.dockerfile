FROM python

COPY ./meter_software/ /app/meter_software/
COPY ./meter_software.py /app/main.py
COPY ./requirements_meter_software.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
# replace with init.sh