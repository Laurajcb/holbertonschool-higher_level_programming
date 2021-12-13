#!/usr/bin/node
//prints My number: <first argv into int>

const args = process.argv;
if (isNaN(args[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args[2]));
}
