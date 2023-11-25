FROM python
WORKDIR /app

# CRON
RUN apt update && apt install cron curl -y
COPY ./smartmeter_crontab /etc/cron.d/meter.cron
RUN crontab /etc/cron.d/meter.cron

# ENTRYPOINT
COPY ./smartmeter_entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

# METER_SIMULATION
COPY ./smartmeter/ /app/smartmeter/
COPY ./smartmeter.py /app/smartmeter.py
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# METER_SOFTWARE
COPY ./meter_software/ /app2/meter_software/
COPY ./meter_software_run.py /app2/run.py
COPY ./meter_software_init.py /app2/init.py
COPY ./requirements_meter_software.txt /app2/requirements.txt
RUN pip install -r /app2/requirements.txt

# ENTRYPOINT
CMD /bin/sh entrypoint.sh
