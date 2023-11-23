FROM python

COPY ./frontend /app/frontend
COPY ./backend /app/backend
COPY ./static /app/static
COPY ./templates /app/templates
COPY requirements.txt /app/requirements.txt
COPY __init__.py /app/__init__.py

RUN pip install -r /app/requirements.txt
RUN python /app/backend/db/db_manager.py

EXPOSE 8080

CMD ["waitress-serve", "--call", "app:create_app"]