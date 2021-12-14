#!/usr/bin/node
//Function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
    const result = list.filter(element => element === searchElement);
    return result.length;
};
