#!/usr/bin/node
//prints My number: <first argv into int>
if (parseInt(process.argv[2])) {
  console.log('My number:', parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
