#!/usr/bin/node

const { argv } = require('node:process');
const num = parseInt(argv[2]);

if (!num) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
