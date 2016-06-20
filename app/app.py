from gevent import monkey
monkey.patch_all()

import os
import time
from flask import Flask, url_for, jsonify
from worker import celery
from celery.task.control import inspect, revoke
import celery.states as states

from flask_socketio import SocketIO, emit

from flask.ext.cors import CORS, cross_origin


env=os.environ
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
socketio = SocketIO(app)


@app.route('/')
def hello():
    return "You should be using the SPA entry. But you can <a href='/add/1/2'>try me out</a>."


# echo for connection confirmation
@socketio.on('connect', namespace='/cruncher')
def connect():
    emit('connected', {'hello': 'there'}, namespace='/cruncher')
    print 'connected to client'


@socketio.on('disconnect', namespace='/cruncher')
def connect():
    emit('disconnected', namespace='/cruncher')
    print 'disconnected to client'


@app.route('/list')
def list():
    i = inspect()
    print i.registered_tasks()
    return jsonify(results=i.registered_tasks())


@cross_origin()
@app.route('/add/<int:param1>/<int:param2>', methods=['GET', 'POST'])
def add(param1, param2):
    task = celery.send_task('mytasks.add', args=[param1, param2], kwargs={})

    # initiate progress
    socketio.emit('progress', {'status': 10}, namespace='/cruncher')
    time.sleep(1)

    # check progress
    res = celery.AsyncResult(task.id)
    if res.state == states.PENDING:
        socketio.emit('progress', {'status': 50}, namespace='/cruncher')
    time.sleep(2)
    socketio.emit('progress', {'status': 100, 'result': str(res.result)}, namespace='/cruncher')
    return jsonify(id=task.id, url=url_for('check_task', id=task.id, _external=True))


@app.route('/check/<string:id>')
def check_task(id):
    res = celery.AsyncResult(id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)


@app.route('/cancel/<string:id>')
def cancel_task(id):
    res = celery.AsyncResult(id)
    if res.state == states.PENDING:
        revoke(id, terminate=True)
        return "task '{id}' cancelled".format(id=id)
    else:
        return str(res.result)


if __name__ == '__main__':
    socketio.run(app, "0.0.0.0", port=5000, debug=True)
