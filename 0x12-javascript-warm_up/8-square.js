#!/usr/bin/node

// Get the size of the square from the command line arguments.
const size = Math.floor(Number(process.argv[2]));

// Check if the size is a valid number.
if (isNaN(size)) {
  // If the size is not a number, print an error message and exit the program.
  console.log('Missing size');
} else {
  // If the size is a valid number, create a square of X's with the given size.
  for (let r = 0; r < size; r++) {
    // For each row, create an empty string to store the X's.
    let row = '';
    for (let c = 0; c < size; c++) {
      // For each column in the row, add an X to the row string.
      row += 'X';
    }
    // Print the completed row string to the console.
    console.log(row);
  }
}
