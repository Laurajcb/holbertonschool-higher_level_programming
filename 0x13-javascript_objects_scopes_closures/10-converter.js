#!/usr/bin/node
// Function that converts a numb from base 10 to another base passed as arg

exports.converter = function (base) {
  return number => number.toString(base);
};
