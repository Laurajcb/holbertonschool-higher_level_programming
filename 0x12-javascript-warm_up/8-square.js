#!/usr/bin/node
// script that prints a square
const x = parseInt(process.argv[2]);
if (isNaN(x) && !x ) {
    console.log('Missing size');
} else { 
    for (let i = 0; i < x; i++) {
        console.log('X'.repeat(x));
    }
}
