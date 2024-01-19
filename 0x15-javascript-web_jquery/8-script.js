#!/usr/bin/node
/* 
Fetches and lists all movies title by using this 
URL: https://swapi-api.hbtn.io/api/films/?format=json
*/

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data){
    for (const movie of data.results) {
        $('UL#list_movies').append($('<li></li>').text(movie.title));
    }
})