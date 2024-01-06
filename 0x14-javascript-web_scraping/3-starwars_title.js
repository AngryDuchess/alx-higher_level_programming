#!/usr/bin/node

const req = require('request');
const [, , ID] = process.argv;
const URL = `https://swapi-api.alx-tools.com/api/films/${ID}`;

req(URL, { json: true }, (err, res) => {
  if (err) console.log(err);
  console.log(res.body.title);
});
