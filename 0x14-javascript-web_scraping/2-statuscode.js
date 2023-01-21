#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request(URL, function (err, response) {
  if (URL) {
    console.log('code: ' + response.statusCode);
  }
});
