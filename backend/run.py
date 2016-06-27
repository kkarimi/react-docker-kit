#!/bin/env python

from app import create_app, socketio

app = create_app(debug=True)

host = app.config.get("HOST")
port = app.config.get("PORT")

if __name__ == '__main__':
    print "Server running at http://%s:%s" % (host, port)
    socketio.run(app, host, port=int(port))
