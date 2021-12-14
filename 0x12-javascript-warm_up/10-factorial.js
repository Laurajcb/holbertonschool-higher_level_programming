#!/usr/bin/node
// script that computes and prints a factorial
const number = Number.parseInt(process.argv[2]);
function factorial (number) {
  if (!number) {
    return 1;
  }
  return number * factorial(number - 1);
}

console.log(factorial(number));