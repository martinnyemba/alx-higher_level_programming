# Project: 0x11.Python - Network #1

This repository includes examples of how to fetch internet resources with Python and manipulate data from external services. 
The examples cover various topics related to internet resources and the Python packages urllib and requests.

## How to fetch internet resources with the Python package urllib
The urllib package is a standard Python library used for opening URLs. 
This example shows how to fetch internet resources using the urllib.request.urlopen() method. It also provides examples of how to handle exceptions and how to read and decode the response.

## How to decode urllib body response
In this example, we cover how to decode the body response from urllib using the urllib.request.urlopen() method. 
We use the decode() method to convert the bytes object to a string object.

## How to use the Python package requests
The requests package is an alternative to urllib and is considered easier to use. 
This example shows how to use requests to fetch internet resources. 
It covers how to handle exceptions, how to read and decode the response, and how to pass parameters and headers.

## How to make HTTP GET request
This example shows how to make HTTP GET requests using both urllib and requests. 
We cover how to pass parameters and headers, how to handle exceptions, and how to read and decode the response.

## How to make HTTP POST/PUT/etc. request
In this example, we cover how to make HTTP POST, PUT, DELETE, and PATCH requests using requests. 
We cover how to pass data, headers, and authentication information, how to handle exceptions, and how to read and decode the response.

## How to fetch JSON resources
This example shows how to fetch JSON resources using both urllib and requests. 
We cover how to read and decode the JSON response and how to handle exceptions.

## How to manipulate data from an external service
In this example, we show how to manipulate data from an external service using the requests package.
 We use the JSONPlaceholder API to demonstrate how to fetch data, filter and sort the data, and perform calculations on the data.

## Requirements
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly #!/usr/bin/python3
- A README.md file at the root of the repo is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All files must be executable
- The length of your files will be tested using wc
- All modules should have documentation (python3 -c 'print(import("my_module").doc)')
- You must use get to access dictionary values by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- Documentation should be a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)
- Your code should not be executed when imported (by using if name == "main":)

## File Structure
All files should be contained within a folder at the root of the repo.

## Code Execution
To execute any of the code files, ensure that the file has executable permissions, then simply run the file from the command line.

For example:
```
$ ./my_script.py
```

## Tasks :

* **0. What's my status? #0**
  * [0-hbtn_status.py](./0-hbtn_status.py): Python script that fetches
  `https://intranet.hbtn.io/status`.
  * Uses `urllib`.

* **1. Response header value #0**
  * [1-hbtn_header.py](./1-hbtn_header.py): Python script that displays the
  `X-Request-Id` response header variable of a request to a given URL.
  * Usage: `./1-hbtn_header.py <URL>`
	* Uses `urllib`.

* **2. POST an email #0**
  * [2-post_email.py](./2-post_email.py): Python script that sends a `POST`
  request to a given URL with a given email, and displays the response body.
  * Usage: `./2-post_email.py <URL> <email>`.
	* Uses `urllib`.

* **3. Error code #0**
  * [3-error_code.py](./3-error_code.py): Python script sends a request to
  a given URL and displays the response body.
  * Handles HTTP errors.
	* Uses `urllib`.

* **4. What's my status? #1**
  * [4-hbtn_status.py](./4-hbtn_status.py): Python script that fetches
  `https://intranet.hbtn.io/status`.
  * Uses `requests`.

* **5. Response header value #1**
  * [5-hbtn_header.py](./5-hbtn_header.py): Python script that displays the
  `X-Request-Id` response header variable of a request to a given URL.
  * Usage: `./5-hbtn_header.py <URL>`
	* Uses `requests`.

* **6. POST an email #1**
  * [6-post_email.py](./6-post_email.py): Python script that sends a `POST`
  request to a given URL with a given email, and displays the response body.
  * Usage: `./6-post_email.py <URL> <email>`.
	* Uses `requests`.

* **7. Error code #1**
  * [7-error_code.py](./7-error_code.py): Python script sends a request to
  a given URL and displays the response body.
  * Handles HTTP errors.
	* Uses `requests`.

* **8. Search API**
  * [8-json_api.py](./8-json_api.py): Python script that sends a `POST` request
  to `http://0.0.0.0:5000/search_user` with a letter passed as parameter.
  * Usage: `./8-json_api.py <letter>`
	* The letter is sent as the value of the variable `q`.
	* If no letter is given, sets `q=""`.
	* If the response body is properly formatted and non-empty, displays it as
  `[<id>] <name>`.
  * Uses `requests`.

* **9. My Github!**
  * [10-my_github.py](./10-my_github.py): Python script that takes GitHub
  credentials (username and password) and uses the Github API to display the
  corresponding ID.
  * Usage: `./10-my_github.py <username> <password>`
	* Uses `requests`.

* **10. Time for an interview!**
  * [100-github_commits.py](./100-github_commits.py): Python script that lists
  the 10 most recent comments of a given GitHub repository using the GitHub API.
  * Usage: `./100-github_commits.py <repository name> <owner name>`
	* Uses `requests`.

## Author
This repository was created by Martin Nyemba <martinnyemba@gmail.com>