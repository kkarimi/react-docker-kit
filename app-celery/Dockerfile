FROM python:2.7

ADD ./requirements.txt /app-celery/requirements.txt
WORKDIR /app-celery
RUN pip install -r requirements.txt

Add . /app-celery

# run the worker
ENTRYPOINT celery -A tasks worker --loglevel=info
