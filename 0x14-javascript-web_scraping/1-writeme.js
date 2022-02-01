#!/usr/bin/nodejs
//fs module: File System.
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err) => {
  if (err) throw err;
});
