FROM python

COPY ./environment/ /app/environment/
COPY ./environment.py /app/environment.py
COPY ./smartmeter/ /app/smartmeter/
COPY ./requirements_env.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "environment.py"]