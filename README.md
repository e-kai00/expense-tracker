## UX Design

### User Stories

"_As a website user, I would like to_: __________________"

<br>

### Design

### Framework

### Color Scheme

### Icons

### Typography

### Wireframes

<br>

## Features

### Existing Features

### Features to Implement

<br>

## Technologies

- [VS Code](https://code.visualstudio.com/) - used as my primary IDE.
- [GitHub](https://github.com/) - used as remote online storage of my code.

### Front-End 

- HTML
- CSS
- jQuery

### Back-End

- Django
- Heroku
- Python

<br>

## Testing



### Validators

**HTML**
- [W3C HTML Validator](https://validator.w3.org/)
  - One HTML file initially had a minor error that has been fixed (_base.html_) [Correction commit: e5680f0](https://github.com/e-kai00/expense-tracker/commit/e5680f020d3a508c025ba202106bf1a50f3bb61d)
  - Other warnings were due to the W3C not recognizing Django Templating:
    - Warning: Consider adding a `lang` attribute to the html start tag to declare the language of this document.

    - Error: Start tag seen without seeing a doctype first. Expected `<!DOCTYPE html>`.

    - Error: Element `head` is missing a required instance of child element `title`.

    - Error: Bad value `{% url 'index' %}` for attribute `href` on element `a`: Illegal character in path segment: `{` is not allowed.
    

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
  - No Error Found.
  - I received one warning: Imported style sheets are not checked in direct input and file upload modes


**JavaScript**
- [JShint](https://jshint.com/)
  - script.js [file](https://github.com/e-kai00/expense-tracker/blob/main/trackerapp/static/trackerapp/js/script.js):
      - __Metrics__:
        - There are 3 functions in this file.
Function with the largest signature take 3 arguments, while the median is 0.
Largest function has 16 statements in it, while the median is 3.
The most complex function has a cyclomatic complexity value of 6 while the median is 1.
      - __Undefined variable__:
        - $ (used for jQuery)
      - I received 15 warnings attributed to the Chart.js plagin:
        - 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). (x8)
        - 'concise methods' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
        - 'destructuring binding' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). (x3)
        - 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). (x2)
Unexpected use of '|='.
  - Chart instantiation in [index.html](https://github.com/e-kai00/expense-tracker/blob/main/trackerapp/templates/trackerapp/index.html):
    - __Metrics__:
      - There is only one function in this file.
It takes one argument.
This function contains 4 statements.
Cyclomatic complexity number for this function is 1.      
    - __Undefined variables__:
      - $ (used for jQuery)
      - Chart (used by Chart.js library)
      - plugin (Chart.js plagin)
    - __Unused variable__: myChart
      - It occurs because the variable myChart is defined to reference the canvas element with the ID "myChart" but is not further used in the code snippet. However, this variable is necessary to initialize the Chart.js chart on the canvas element.
    - I also received five warnings: Missing semicolon. They have been fexed.

**Python**
- [CI Python Linter](https://pep8ci.herokuapp.com/#)
  - All .py files are compliant with the guidelines outlined in PEP8, exept one:
    - built-in Django [settings.py ](https://github.com/e-kai00/expense-tracker/blob/main/tracker/settings.py)
    - E501 line too long (91 > 79 characters) - `AUTH_PASSWORD_VALIDATORS` (x4)

<br>

### Compatibility

### Known Issues

### Automated Testing

<br>

## Deployment

<br>

## Credits

### Content
### Media
### Code
### Acknowledgments

