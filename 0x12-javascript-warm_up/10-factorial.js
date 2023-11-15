#!/usr/bin/node

const { argv } = require('process');

function fact (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  }
  return (fact(num - 1) * num);
}

const num = parseInt(argv[2]);
console.log(fact(num));
