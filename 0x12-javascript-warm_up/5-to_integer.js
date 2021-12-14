#!/usr/bin/node
const argParse = parseInt(process.argv[2]);
if (isNaN(argParse )) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argParse);
}
