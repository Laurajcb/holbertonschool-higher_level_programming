#!/usr/bin/node
//function that prints the number of argv already printed and the new argv value


let counter = 0;
exports.logMe = function (item) {
  console.log(`${counter}: ${item}`);
  counter++;
};
