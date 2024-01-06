#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const [, , URL, path] = process.argv;

request(URL, (_, res) => {
  fs.writeFile(path, res.body, (err) => {
    if (err) console.log(err);
  });
});
