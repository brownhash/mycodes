FROM python:3.6
LABEL maintainer="sharma1612harshit.github.io"

RUN pip install uwsgi
RUN pip install psutil
RUN pip install flask

COPY .. /app
WORKDIR /app

RUN mkdir /etc/logster
RUN mkdir /etc/logster/config
COPY config /etc/logster/config/

ENV LOG_DIR=/var/log/
EXPOSE 8081
CMD [ "uwsgi", "app.ini" ]

