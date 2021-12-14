#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.
const array = process.argv.slice(2).map(element => Number.parseInt(element));
const array = process.argv.slice(2);

if (array.length <= 1) {
  console.log('0');
} else {
  array.sort((a, b) => a - b);
  const len = array.length;
  console.log(array[len - 2]);
}
