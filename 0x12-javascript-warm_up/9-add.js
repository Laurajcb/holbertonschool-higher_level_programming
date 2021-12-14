#!/usr/bin/node
//Script that prints the addition of 2 integers
const args = process.argv;
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

add(args[2], args[3]);
