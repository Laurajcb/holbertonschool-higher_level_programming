#!/usr/bin/node
/*
- Reads and prints the content of a file in utf-8.
- fs module: File System.
*/
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) throw err;
  else process.stdout.write(data);
});
