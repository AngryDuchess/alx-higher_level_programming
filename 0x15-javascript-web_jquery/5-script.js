#!/usr/bin/node

$('DIV#add_item').click(function(){
    $('UL.my_list').append('<li>Item</li>');
})