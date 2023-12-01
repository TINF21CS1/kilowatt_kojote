FROM debian

# CRON
RUN apt update && apt install cron rsync -y
RUN echo "0 4 * * * rsync -b /in /out > /proc/1/fd/1 2>/proc/1/fd/2" > /etc/cron.d/backup.cron
RUN crontab /etc/cron.d/backup.cron

# ENTRYPOINT
CMD cron -f
