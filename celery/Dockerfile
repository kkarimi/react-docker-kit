FROM python:2.7

ADD ./requirements.txt /celery/requirements.txt
WORKDIR /celery
RUN pip install -r requirements.txt

Add . /celery

# run the worker
ENTRYPOINT celery -A tasks worker --loglevel=info
