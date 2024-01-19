#!/usr/bin/node

$.ajax($('#update_header').click(function(){
    $('header').text('New Header!!!');
}))