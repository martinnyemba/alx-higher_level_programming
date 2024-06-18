### 0x12. JavaScript - Warm up
**JavaScript**


### Background Context

JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:

- Scripting (same as we did with Python)
- Web front-end

For the moment, and for learning all basic concepts of this language, we will do some scripting. After, we will make our AirBnB project dynamic by using Javascript and JQuery.

### Resources

Read or watch:

- Writing JavaScript Code
- Variables
- Data Types
- Operators
- Operator Precedence
- Controlling Program Flow
- Functions
- Objects and Arrays
- Intrinsic Objects
- Module patterns
- var, let and const
- JavaScript Tutorial
- Modern JS

### Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

#### General

- Why JavaScript programming is amazing
- How to run a JavaScript script
- How to create variables and constants
- What are differences between var, const and let
- What are all the data types available in JavaScript
- How to use the if, if ... else statements
- How to use comments
- How to affect values to variables
- How to use while and for loops
- How to use break and continue statements
- What is a function and how do you use functions
- What does a function that does not use any return statement return
- Scope of variables
- What are the arithmetic operators and how to use them
- How to manipulate dictionary
- How to import a file

### Requirements

#### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant (version 16.x.x). Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All your files must be executable
- The length of your files will be tested using `wc`

### More Info

#### Install Node 14

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

#### Install semi-standard

Documentation

```bash
$ sudo npm install semistandard --global
```

### Tasks

#### 0. First constant, first print

**mandatory**

Write a script that prints “JavaScript is amazing”:

- You must create a constant variable called `myVar` with the value “JavaScript is amazing”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

```shell
guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/0x12$ 
```

**Repo:**

- **GitHub repository**: `alx-higher_level_programming`
- **Directory**: `0x12-javascript-warm_up`
- **File**: `0-javascript_is_amazing.js`

#### 1. 3 languages

**mandatory**

Write a script that prints 3 lines:

- The first line: “C is fun”
- The second line: “Python is cool”
- The third line: “JavaScript is amazing”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

```shell
guillaume@ubuntu:~/0x12$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
```

**Repo:**

- **GitHub repository**: `alx-higher_level_programming`
- **Directory**: `0x12-javascript-warm_up`
- **File**: `1-multi_languages.js`

#### 2. Arguments

**mandatory**

Write a script that prints a message depending of the number of arguments passed:

- If no arguments are passed to the script, print “No argument”
- If only one argument is passed to the script, print “Argument found”
- Otherwise, print “Arguments found”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- Reference: `process.argv`

```shell
guillaume@ubuntu:~/0x12$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/0x12$ 
```

**Repo:**

- **GitHub repository**: `alx-higher_level_programming`
- **Directory**: `0x12-javascript-warm_up`
- **File**: `2-arguments.js`

#### 3. Value of my argument

**mandatory**

Write a script that prints the first argument passed to it:

- If no arguments are passed to the script, print “No argument”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `length`

```shell
guillaume@ubuntu:~/0x12$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js School
School
guillaume@ubuntu:~/0x12$ 
```

**Repo:**

- **GitHub repository**: `alx-higher_level_programming`
- **Directory**: `0x12-javascript-warm_up`
- **File**: `3-value_argument.js`

#### 4. Create a sentence

**mandatory**

Write a script that prints two arguments passed to it, in the following format: “<arg1> is <arg2>”

- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

```shell
guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$ 
```

**Repo:**

- **GitHub repository**: `alx-higher_level_programming`
- **Directory**: `0x12-javascript-warm_up`
- **File**: `4-concat.js`

#### 5. An Integer

**mandatory**

Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:

- If the argument can’t be converted to an integer, print “Not a number”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `try/catch`

```shell
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js School
Not a number
guillaume@ubuntu:~/0x12$ 
```

**Repo:**

- **GitHub repository**: `alx-higher_level_programming`
- **Directory**: `0x12-javascript-warm_up`
- **File**: `5-to_integer.js`

#### 6. Loop to languages

**mandatory**

Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

- The first line: “C is fun”
- The second line: “Python is cool”
- The third line: “JavaScript is amazing”
- You must use `console.log(...)` to print all output

