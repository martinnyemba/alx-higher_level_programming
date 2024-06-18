#!/usr/bin/node

// Get the first argument from the command line and convert it to a number
const x = Math.floor(Number(process.argv[2]));

// Check if x is NaN (not a number)
if (isNaN(x)) {
  // If x is NaN, print an error message
  console.log('Missing number of occurrences');
} else {
  // If x is a number, loop x times
  for (let i = 0; i < x; i++) {
    // Print "C is fun" to the console during each iteration
    console.log('C is fun');
  }
}
