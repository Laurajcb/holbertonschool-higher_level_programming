#!/usr/bin/node
// prints a message depending of the number of arguments passed

const commands = process.argv;
if (commands.length < 3) {
  console.log('No argument');
} else if (commands.length < 4) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
