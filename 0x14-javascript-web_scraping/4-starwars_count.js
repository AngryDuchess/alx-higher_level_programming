#!/usr/bin/node
const req = require("request");
const charURL = "https://swapi-api.alx-tools.com/api/people/18/";
const [, , URL] = process.argv;

req(URL, { json: true }, (_, res) => {
    const movieCount = res.body.results.filter((movie => {
        return movie.characters.includes(charURL);
    }));

    console.log(movieCount.length);
});
