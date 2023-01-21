#!/usr/bin/node

const request = require('request');
const episodeNum = process.argv[2];
const API = 'https://swapi-api.hbtn.io/api/films/';

request(API + episodeNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
