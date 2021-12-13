#!/usr/bin/node
//prints My number: <first argv into int>

if (isNaN(process.argv[2])) {
    console.log('Not a number');
} else {
    console.log('My number: ' + parseInt(process.argv[2]));
}
