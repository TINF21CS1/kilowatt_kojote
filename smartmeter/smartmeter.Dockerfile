FROM python

COPY ./smartmeter/ /app/smartmeter/
COPY ./smartmeter.py /app/smartmeter.py
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "smartmeter.py"]