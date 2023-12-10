FROM python

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./static /app/static
ADD https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css /app/static/bootstrap.min.css
ADD https://cdn.jsdelivr.net/npm/chart.js /app/static/chart.js
ADD https://code.jquery.com/jquery-3.6.0.min.js /app/static/jquery-3.6.0.min.js
ADD https://cdn.datatables.net/1.13.7/css/jquery.dataTables.css /app/static/jquery.dataTables.css
ADD https://cdn.datatables.net/1.10.25/js/jquery.dataTables.js /app/static/jquery.dataTables.js
ADD https://unpkg.com/leaflet@1.9.4/dist/leaflet.css /app/static/leaflet.css
ADD https://unpkg.com/leaflet@1.9.4/dist/leaflet.js /app/static/leaflet.js
ADD https://unpkg.com/leaflet@1.9.4/dist/images/layers.png /app/static/images/layers.png
ADD https://unpkg.com/leaflet@1.9.4/dist/images/layers-2x.png /app/static/images/layers-2x.png
ADD https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png /app/static/images/marker-icon.png
ADD https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png /app/static/images/marker-icon-2x.png
ADD https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png /app/static/images/marker-shadow.png

COPY ./frontend /app/frontend
COPY ./backend /app/backend
COPY ./templates /app/templates

COPY __init__.py /app/__init__.py

RUN python /app/backend/db/db_manager.py

EXPOSE 8080

CMD ["waitress-serve", "--call", "app:create_app"]
