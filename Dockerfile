FROM python:3.6-alpine

ENV APP_HOME=/app/

# sqlite config:
# ENV SOCKSESS_DB=sqlite+pysqlite:///$APP_HOME/myorders.db

# postgres config:
ENV SOCKSESS_DB=postgresql+psycopg2://socksess:socksess@postgres:5432/socksess
ENV FLASK_APP=$APP_HOME/frontend.py
ENV FLASK_DEBUG=1

WORKDIR $APP_HOME

COPY . $APP_HOME

RUN \
  apk update && \
  apk upgrade && \
  apk add --no-cache bash && \
  apk add --no-cache postgresql-libs && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
  apk add g++

#  apk add install gcc python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev g++ && \
  
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
