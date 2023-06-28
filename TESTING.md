## Table of Contents

- [Responsiveness](#responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Bugs](#bugs)
- [Lighthouse](#lighthouse)
- [Validators](#validators)
- [User Stories](#user-stories)
- [Features](#features) <br><br>


### Responsiveness

| Device| Screenshort|
|:-------:|:-------:|
|Desktop|![Desktop](/readme-img/testing/responsive-desktop.png)|
|Tablet |![Tablet](/readme-img/testing/responsive-tablet.png)|
|Mobile |![Mobile](/readme-img/testing/responsive-mobile.png)|

### Browser Compatibility
| Browser | Screenshot | Notes|
|:-------:|:-------:|:-------:|
| Chrome  | ![Chrome](/readme-img/testing/browser-chrome.png) |
| Mozilla Firefox|![Firefox](/readme-img/testing/browser-firefox.png)  |
| Microsoft Edge|![Edge](/readme-img/testing/browser-edge.png) |


### Bugs

| Description | Action | Status |
|:-----|:------|:------:|
|The display of form fields derived from models with predefined choices is not visible| Initialize Materialize select element| Closed|
|The Delete Confirmation modal fails to delete the category| Pass `category.id` to the modal and its trigger; set modal inside 'for-loop'| Closed|
|Unable to edit categories, that are predefined by models|Remove choices option from the model|Closed|
|User sees categories created by other users|Filters the queryset of the 'expense_category' field in the form to include only the categories of the current user| Closed|
|When attempting to add or create a category with a duplicated name, the application does not throw a ValidationError| Using `django-materializecss-form` resolved the issue| Closed|
|After receiving a ValidationError while attempting to add a duplicated category, entering a new valid name does not redirect the user to the previous page|This issue still needs to be resolved| Open|
|Static files are not served at deployed app version| Move `static` folder to root directory, set up settings.py, change links for static files in templates, add cloudinary library| Closed|
|Login page: checkbox for 'Remember me' does not display'|This issue still needs to be resolved|Open|


### Lighthouse
![Lighthouse test](/readme-img/testing/lighthouse.png)


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
  - script.js [file](https://github.com/e-kai00/expense-tracker/blob/main/static/js/script.js):
      - __Metrics__:
        - There are 4 functions in this file.
          Function with the largest signature take 3 arguments, while the median is 0.
          Largest function has 16 statements in it, while the median is 3.5.
          The most complex function has a cyclomatic complexity value of 6 while the median is 1.
      - __Undefined variable__:
        - $ (used for jQuery)
      - I received 15 warnings attributed to the Chart.js plagin:
        - 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). (x8)
        - 'concise methods' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
        - 'destructuring binding' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). (x3)
        - 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). (x2)
Unexpected use of '|='.
  - Chart instantiation in [index.html](https://github.com/e-kai00/expense-tracker/blob/main/templates/trackerapp/index.html):
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
    - E501 line too long (91 > 79 characters) - `AUTH_PASSWORD_VALIDATORS` (x4) <br><br>



### User Stories 

"*As a User I want to be able to___________________*"
- [x] - *successfully implemented*
- [ ] - *yet to be implemented* <br><br>

- [x] register my account, so that my personal finance data is secured
- [x] log in
- [x] log out
- [x] intuitively navigate through different sections and features of the application
- [x] access the app on various devices (mobiles, tablets, desktop)
- [x] add transactions to keep track of my financial activities
- [x] see my current balance to stay informed about my financial status
- [x] see all my transactions for the current period to review my financial activities 
- [x] filter my transactions by month
- [x] add new expense categories
- [x] update existing expense categories
- [x] delete expense categories
- [x] see chart/ diagram so that I better understand my spending habits
- [ ] update or delete a transaction
- [ ] create and manage accounts (e.g. Cash, Cards, Savings)


### Features

| Page | User action | Expected result | Status|
|:-----|:------------|:----------------|:-----:|
|**User Registration and Authentication**| | |
| Sign up | Enter username | Field will only accept letters, numbers, and @/./+/-/_ characters| pass|
| | Enter valid email| Field will only accept email address format | pass|
| | Enter valid password (x2)| Field will only accept password format: min. 8 characters|pass|
| | Click Sing in link | Redirect to sign-in page|pass|
| | Click Sign up button| Register user and redirect to home page|pass|
|Sign in| Enter valid username| Filed only accept valid username|pass|
| | Enter valid password| Field will only accept existing password format|pass|
| | Click Sign up link| Redirect to sign-up page|pass|
| | Click Sign in button| Redirect to home page|pass|
|Sign out| Click Sign out link|Redirect to confirmation page|pass|
| | Click Sign out button| Sign out and redirect to Log-in page|pass|
|**Transaction Creation**| | |
|Add expense|Click expense "-" button|Prompt to enter amount, category and note. New expense created| pass|
| | Click 'Add new category' link| Redirect to 'Add new category' page|pass|
|Add income| Click income "+" button|Prompt to enter amount, notes. New income created|pass|
|**Reports**| | |
|Visual expense chart| Add expense|Update distribution of expenses across different categories|pass|
|**Transaction Filtering**| | |
|Filter transactions| Click Balance button| Redirect to detailed transactions list|pass|
| | Chose month from dropdown and press filter icon|Display transactions for selected month|pass|
|**Expense Category Management**| | |
|List of categories|Click Category icon in navbar|Redirect to expense category page|pass|
|Create category |Click 'Add new' button| Prompt  to enter new category name. Create new category. Redirect to list of categories|pass|
|Edit category|Click Edit icon|Prompt  to update category name. Update. Redirect to list of categories|pass|
|Delete category|Click Delete icon|Prompt to confirm delete action. Delete. Redirect to list of categories|pass|
|**Navbar**| | |
|| Click Logo|Redirect to home page|pass|
| |Click Home icon|Redirect to home page|pass|
| |Click Category icon|Redirect to categories page|pass|
|**404 page** | |
| | Click 'Go to home' button|Redirect to homepage|pass|
|**Confirmations**| | |
| | On Registration| Flash message|pass|
| | On Login| Flash message|pass|
| | On Logout| Flash message|pass|
| | On category created|Flash message|pass|
| | On category updated|Flash message|pass|
| | On category deleted| Delete confirmation modal|pass|
| | |Flash message|pass|
|**Error messages**| | |
|Enter existing category name| On category created| Message: "This category is already exists. Enter another category name."|pass|
| | On category updated|Message: "This category is already exists. Enter another category name."|pass|





Back to [README.md](https://github.com/e-kai00/expense-tracker/blob/main/README.md)