#!/usr/bin/node
//Script that prints x times “C is fun”

const myArgs = process.argv[2];
if (!myArgs) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myArgs; i++) {
    console.log('C is fun');
  }
}
