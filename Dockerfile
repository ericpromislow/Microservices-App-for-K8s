FROM python:3.6-slim

ENV APP_HOME=/app/

WORKDIR $APP_HOME

COPY . $APP_HOME

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["/bin/bash", "info/run.sh"]
