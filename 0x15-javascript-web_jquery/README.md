# 0x15. JavaScript - Web jQuery

## Project Overview

In this project, I explored the use of JavaScript and jQuery to enhance front-end web development. The goal was to understand how jQuery simplifies DOM manipulation, event handling, and AJAX requests, making front-end programming more efficient and less error-prone.

## Concepts Covered

### JavaScript in the Browser
- **Static vs. Dynamic Data Handling**: Understanding the difference between handling data that doesn't change (static) and data that can change over time (dynamic).

### Resources
I referred to the following resources to understand the core concepts of jQuery and JavaScript:
- **What is JavaScript?**
- **Selectors**: How to use selectors in jQuery to target HTML elements.
- **Get and Set Content**: Methods to retrieve and update HTML content.
- **Manipulate CSS Classes**: Techniques to add, remove, and toggle CSS classes.
- **Manipulate DOM Elements**: How to dynamically change the structure of the DOM.
- **API Introduction**: Basics of using APIs in web development.
- **GET & POST Requests**: Understanding how to make HTTP requests using jQuery.
- **jQuery Ajax Tutorial**: Detailed tutorial on using AJAX with jQuery.
- **Troubleshooting JavaScript**: Common issues and their solutions.
- **jQuery Documentation**: Comprehensive guide to jQuery methods and features.

## Learning Objectives
By the end of this project, I was able to:
- Explain why jQuery simplifies front-end programming and tweet about it using the hashtag #ilovejquery.
- Select HTML elements using both JavaScript and jQuery.
- Understand the differences between ID, class, and tag name selectors.
- Modify the style of HTML elements.
- Retrieve and update HTML content.
- Manipulate the DOM dynamically.
- Make GET and POST requests using jQuery AJAX.
- Listen and bind to DOM and user events.

## Project Requirements
- **Editors**: Used vi, vim, or emacs for coding.
- **Browser**: Ensured compatibility with Chrome (version 57.0).
- **File Format**: All files end with a new line.
- **Code Standards**: Code is semistandard compliant.
- **jQuery Version**: Used jQuery version 3.x.
- **No Var**: Avoided the use of `var`.
- **DOM Manipulation**: HTML did not reload for each action; instead, used jQuery for dynamic updates.

## Implementation Details

### Importing jQuery
To use jQuery, I included the following script in the `<head>` section of my HTML:
```html
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

### Example Code Snippets
- **Selecting Elements**:
  ```javascript
  // Selecting elements by ID
  $('#myElement').css('color', 'blue');

  // Selecting elements by class
  $('.myClass').text('Hello, World!');

  // Selecting elements by tag name
  $('p').hide();
  ```

- **Event Handling**:
  ```javascript
  // Binding a click event
  $('#myButton').click(function() {
    alert('Button clicked!');
  });
  ```

- **AJAX Requests**:
  ```javascript
  // Making a GET request
  $.get('https://api.example.com/data', function(data) {
    console.log(data);
  });

  // Making a POST request
  $.post('https://api.example.com/data', { key: 'value' }, function(response) {
    console.log(response);
  });
  ```

## Tasks :

* **0. No jQuery**
  * [0-script.js](./0-script.js): JavaScript script that uses `document.querySelector`
  to update the text color of the HTML tag `HEADER` to red (`#ff0`).

* **1. With jQuery**
  * [1-script.js](./1-script.js): JavaScript script that uses jQuery to update the
  text color of the HTML tag `HEADER` to red (`#ff0`).

* **2. Click and turn red**
  * [2-script.js](./2-script.js): JavaScript script that uses jQuery to update the text color
  of the HTML tag `HEADER` to red (`#ff0`) when the user clicks on the tag `DIV#red_header`.

* **3. Add `.red` class**
  * [3-script.js](./3-script.js): JavaScript script that uses jQuery to add the class
  `.red` to the HTML tag `HEADER` when the user clicks on the tag `DIV#red_header`.

* **4. Toggle classes**
  * [4-script.js](./4-script.js): JavaScript script that uses jQuery to toggle the class
  of the HTML tag `HEADER` between `.red` and `.green` when the user clicks on the tag
  `DIV#red_header`.

* **5. List of elements**
  * [5-script.js](./5-script.js): JavaScript script that uses jQuery to add a `LI`
  element to a list when the user clicks on the tag `DIV#add_item`.
  * Adds the element `<li>Item</li>` to `UL.my_list`.

* **6. Change the text**
  * [6-script.js](./6-script.js): JavaScript script that uses jQuery to update the text
  of the HTML tag `HEADER` to "New Header!!!" when the user clicks on the tag
  `DIV#update_header`.

* **7. Star wars character**
  * [7-script.js](./7-script.js): JavaScript script that uses jQuery to fetch the Star
  Wars API `https://swapi.co/api/people/5/?format=json` and display the name in the HTML
  tag `DIV#character`.

* **8. Star Wars movies**
  * [8-script.js](./8-script.js): JavaScript script that uses jQuery to fetch and list
  all movie titles from the Star Wars API `https://swapi.co/api/films/?format=json`.
  * Titles are listed in the HTML tag `UL#list_movies`.

* **9. Say Hello!**
  * [9-script.js](./9-script.js): JavaScript script that uses jQuery to fetch and display
  how to say "Hello" in French using the API
  `https://fourtonfish.com/hellosalut/?lang=fr`.
  * Displays the translation in the HTML tag `DIV#hello`.
  * Works when imported in the `HEAD` tag.

* **10. No jQuery - document loaded**
  * [100-script.js](./100-script.js): JavaScript script that uses `document.querySelector`
  to update the text color of the HTML tag `HEADER` to red (`#ff0`).
  * Works when imported in the `HEAD` tag.

* **11. List, add, remove**
  * [101-script.js](./101-script.js): JavaScript script that uses jQuery to add, remove,
  and clear `LI` elements from a list based on user click input.
  * Adds a new element when the user clicks `DIV#add_item`.
    * Adds `<li>Item</li>` to the HTML tag `UL.my_list`.
  * Removes the last element when the user clicks `DIV#remove_item`.
  * Clears all elements when the user clicks `DIV#clear_list`.
  * Works when imported in the `HEAD` tag.

* **12. Say hello to everybody!**
  * [102-script.js](./102-script.js): JavaScript script that uses jQuery to fetch and
  display how to say "Hello" in a given language using the API
  `https://www.fourtonfish.com/hellosalut/hello/`.
  * Fetches the translation for the language entered in the HTML tag `INPUT#language_code`.
  * Fetches the translation when the user clicks on the HTML tag `INPUT#btn_translate`.
  * Displays the translation in the HTML tag `DIV#hello`.
  * Works when imported in the `HEAD` tag.

* **13. And press ENTER**
  * [103-script.js](./103-script.js): JavaScript script that uses jQuery to fetch and
  display how to say "Hello" in a given language using the API
  `https://www.fourtonfish.com/hellosalut/hello/`.
  * Identical to [102-script.js](./102-script.js) except that the tranlsation is fetched
  when either the user clicks on the HTML tag `INPUT#btn_translate` or presses `ENTER`
  when hovering over the tag `INPUT#language_code`.

## Tests :

* [tests](./tests): Folder of HTML files for testing DOM manipulation scripts.
## Conclusion
This project provided hands-on experience with jQuery, enhancing my understanding of front-end development. By leveraging jQuery, I was able to simplify complex JavaScript tasks, making my code more readable and maintainable.

## Manual QA Review
Once the project was completed, I requested a manual QA review to ensure all requirements were met and the implementation was correct.

---

Thank you for taking the time to read about my project! If you have any questions or feedback, please feel free to reach out.
