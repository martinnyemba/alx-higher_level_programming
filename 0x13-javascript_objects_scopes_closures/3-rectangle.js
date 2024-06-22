#!/usr/bin/node

// Define and export the Rectangle class
module.exports = class Rectangle {
  // Constructor method to initialize the Rectangle instance
  constructor(w, h) {
    // Check if both width and height are positive numbers
    if (w > 0 && h > 0) {
      // If valid, assign width and height to the instance
      [this.width, this.height] = [w, h];
    }
  }

  // Method to print the rectangle using the char 'X'
  print() {
    // Loop through the height
    for (let i = 0; i < this.height; i++) {
      // Print a row of 'X' chars equal to the width of the rectangle
      console.log('X'.repeat(this.width));
    }
  }
};
