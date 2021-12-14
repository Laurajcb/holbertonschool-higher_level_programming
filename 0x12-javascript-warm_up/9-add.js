#!/usr/bin/node
//Script that prints the addition of 2 integers
function add (a, b) {
  return (Number.parseInt(a) + Number.parseInt(b));
}
console.log(add(process.argv[2], process.argv[3]));
