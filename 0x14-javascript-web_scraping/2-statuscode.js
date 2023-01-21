#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request(URL, function (err, response) {
    console.log('code: ' + response.statusCode);
});
