'use strict';

var express = require('express');

var app = express();

app.use(express.static(__dirname + '/dist'));

app.get('/', function(req, res) {
  app.use(express.static(__dirname, '/dist'));
});

var server = app.listen(
  process.env.PORT || 8080,
  '0.0.0.0',
  function () {
    var address = server.address().address;
    var port = server.address().port;
    console.log('App listening at http://%s:%s', address, port);
    console.log('Press Ctrl+C to quit.');
  }
);
