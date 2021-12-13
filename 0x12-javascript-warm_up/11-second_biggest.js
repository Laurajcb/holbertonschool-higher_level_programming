#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.

const array = process.argv.slice(2).map(element => Number.parseInt(element));
if (array.length < 2) {
  console.log(0);
} else {
  array.sort((a, b) => a - b);
  console.log(array[array.length - 2]);
}
