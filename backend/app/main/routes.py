from . import main
import time
from flask import session, redirect, url_for, render_template, request, url_for, jsonify
from worker import celery
from celery.task.control import inspect, revoke
import celery.states as states
from flask_cors import CORS, cross_origin

from .. import socketio


@main.route('/')
def hello():
    return "You should be using the SPA entry. But you can <a href='/add/1/2'>try me out</a>."


# echo for connection confirmation
@socketio.on('connect', namespace='/cruncher')
def connect():
    socketio.emit('connected', {'hello': 'there'}, namespace='/cruncher')
    print 'connected to client'


@socketio.on('disconnect', namespace='/cruncher')
def connect():
    socketio.emit('disconnected', namespace='/cruncher')
    print 'disconnected to client'


@main.route('/list')
def list():
    i = inspect()
    print i.registered_tasks()
    return jsonify(results=i.registered_tasks())


@cross_origin()
@main.route('/add/<int:param1>/<int:param2>', methods=['GET', 'POST'])
def add(param1, param2):
    #clientId = request.sid
    task = celery.send_task('mytasks.add', args=[param1, param2], kwargs={})

    # initiate progress
    socketio.emit('progress', {'status': 10}, namespace='/cruncher')
    time.sleep(1)

    # check progress
    res = celery.AsyncResult(task.id)
    if res.state == states.PENDING:
        socketio.emit('progress', {'status': 50}, namespace='/cruncher')
    time.sleep(2)
    #clientId.socketio.emit('progress', {'status': 100, 'result': str(res.result)}, namespace='/cruncher')
    socketio.emit('progress', {'status': 100, 'result': str(res.result)}, namespace='/cruncher')
    return jsonify(task_id=task.id, status_url=url_for('main.check_task', id=task.id, _external=True))


@main.route('/check/<string:id>')
def check_task(id):
    res = celery.AsyncResult(id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)


@main.route('/cancel/<string:id>')
def cancel_task(id):
    res = celery.AsyncResult(id)
    if res.state == states.PENDING:
        revoke(id, terminate=True)
        return "task '{id}' cancelled".format(id=id)
    else:
        return str(res.result)