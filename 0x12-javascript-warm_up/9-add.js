#!/usr/bin/node
function add (a, b) {
  return a + b;
}
// Use process.argv to collect the first and second arguments
const num1 = process.argv[2];
const num2 = process.argv[3];
// Print message to the console
console.log(add(Number(num1), Number(num2)));
