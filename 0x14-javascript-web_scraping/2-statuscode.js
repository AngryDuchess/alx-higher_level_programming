#!/usr/bin/node
const {error} = require('console')
const request = require('request')

const [, , URL] = process.argv

request(URL, (error, res) => {
    console.log(`code: ${res.statusCode}`);
})
