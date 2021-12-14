#!/usr/bin/node
/*script that prints 3 lines: but by using an array of string and a loop*/
const array = ['C', 'Python', 'JavaScript', 'fun', 'cool', 'amazing'];

for (let i = 0; i < 3; i++) {
  console.log(array[i] + ' is ' + array[i + 3]);
}
