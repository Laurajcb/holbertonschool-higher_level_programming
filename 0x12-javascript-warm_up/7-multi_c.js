#!/usr/bin/node
// script that prints x times “C is fun”
const args = process.argv;

if (isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(args[2]); i++) {
    console.log('C is fun');
  }
}
