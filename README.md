To run:
```bash

docker-compose build
docker-compose up -d # run in detached mode

```
Assuming your your docker-machine ip is 192.168.99.100:
- `http://192.168.99.100:8080` for the front end (React SPA - ES6, webpack, socketio, basscss, etc)


- `http://192.168.99.100:80` for the nginx proxy to back end (enable CORS)
- `http://192.168.99.100:5000` for the back end (Flask - CORS, socketio / celery / redis / worker tasks)
- `http://192.168.99.100:5555` for [flower](http://flower.readthedocs.org) monitoring server

To scale the workers, now run `docker-compose scale worker=5` will create `4` more containers each running a worker, check the flower to show the workers waiting for jobs.
