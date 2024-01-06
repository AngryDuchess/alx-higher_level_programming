#!/usr/bin/node

const fs = require('fs');
const [, , filePath, content] = process.argv;

fs.writeFile(filePath, content, 'utf-8', (err) => {
  console.log(err);
});
