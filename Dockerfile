FROM python:3.6.8-slim

ENV USER=user UID=1000

RUN mkdir /pbp-assessment

RUN groupadd -g ${UID} -r ${USER} \
    && useradd -u ${UID} -r -g ${USER} ${USER}

ADD requirements.txt /pbp-assessment

WORKDIR /pbp-assessment

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY app /pbp-assessment/app
COPY settings.py /pbp-assessment/settings.py
COPY entrypoint.sh /pbp-assessment/entrypoint.sh
COPY wsgi.py /pbp-assessment/wsgi.py

ENV FLASK_APP=wsgi.py

RUN chmod +x entrypoint.sh

RUN chown -R ${USER}:${USER} /pbp-assessment/logs

EXPOSE 9000

USER ${USER}

CMD ["./entrypoint.sh"]