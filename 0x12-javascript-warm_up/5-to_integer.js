#!/usr/bin/env node
//Script that prints My number: <first argument converted in integer>

const toNumber = process.argv[2];
if (Number(toNumber)) {
  console.log('My number: ' + toNumber);
} else {
  console.log('Not a number');
}
