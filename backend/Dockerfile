FROM python:2.7

ADD ./requirements.txt /backend/requirements.txt
WORKDIR /backend

RUN pip install -r requirements.txt

ADD . /backend

ENTRYPOINT ["python"]

CMD ["run.py"]

EXPOSE 5000
