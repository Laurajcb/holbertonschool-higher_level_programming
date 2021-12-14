#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const array = [];
  while (list.length > 0) {
    array.push(list.pop());
  }
  return array;
};
