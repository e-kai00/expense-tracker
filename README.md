## UX Design



### Agile Development
I used the Agile methodology for the management of this project. 
- I utilized 'Issues' functionality on GitHub  to create user stories.

![Agile cards](/readme-img/agile/agile5.png)

- They were then organized into epics, stories, and tasks. 

![Agile epic](/readme-img/agile/agile.png)

![Agile task](/readme-img/agile/agile4.png)

- I used the Kanban Board to visualize and manage tasks throughout the project lifecycle.

![Kanban board](/readme-img/agile/agile2.png)

- Additionally, I used MoSCoW Prioritization to categorize and prioritize requirements.

![moscow method](/readme-img/agile/agile1.png)

*(Remark: this was my first encounter with Agile and MoSCoW methodologies. I tried to implement them as taught during the CI course, dividing tasks into Must Have (up to 60%), Should Have, and Could Have (both up to 20%). However, due to my limited experience, I slightly overestimated the project scope. As a result, I had to make adjustments along the way, and most of my tasks ended up falling into the Must Have category. I'll keep that in mind for my future projects.)*

<br>


## Features

### Existing Features

**Register Account**
- Allows users to create a new account by providing necessary information.

**Login and logout**
- Enables users to log in to access their account and securely log out when finished.

![Login](/readme-img/features/feat.png)

**Ceate transactions**
- Allows users to record and save their financial transactions, such as expenses or income. When adding an expense, users have the option to include a new category and seamlessly continue the process.

![Transactions](/readme-img/features/trans.png)
![Add transactions](/readme-img/features/transactions.png)

**See summary for the current month**
- Provides a summarized overview of the user's financial activity for the current month.

![Month transactions](/readme-img/features/month-summary.png)

**Detailed transactions**
- Displays a detailed view of individual transactions, including date, amount, category, and any additional details.

![Detailed transactions](/readme-img/features/detailed-transactions.png)

**Filter transactions by moth**
- Allows users to filter and view transactions based on specific months.

![Filters](/readme-img/features/filter1.png)

**List of categories**
- Shows a list of categories (have to be created 1st) that can be associated with transactions for easy organization.

![Category list](/readme-img/features/category-list.png)

**Create new category**
- Enables users to create categories to classify their transactions according to their specific needs.

![Create category](/readme-img/features/category-add.png)

**Edit existing category**
- Provides the option to update an existing category name.

![Edit category](/readme-img/features/category-edit.png)

**Delete category**
-  Allows users to remove unwanted categories from their list.

![Delete category](/readme-img/features/category-delete.png)

**Error 404**
- Displays a customized error page (404 Not Found) when a requested page or resource cannot be found.

![404 page](/readme-img/features/404-page.png)


### Features to Implement

**Update User Profile**
- Enable users to change their password, email and delete their profile.

**Manage individual transactions**
- Allow users to delete or modify their recorded transactions.

**Income categories** 
- Provide the ability to create income categories, offering the same functionality as expense categories.

**Create and manage accounts (e.g., Cash, Cards, Savings)**
- Allow users to create and switch between different accounts. I initially planned to include this feature right from the start, but due to my limited experience and time constraints, I had to postpone it. For now I left the `AccountCategory` model unused in my app and plan to return to implement it.



<br>

## Technologies

- [VS Code](https://code.visualstudio.com/) - used as my primary IDE.
- [GitHub](https://github.com/) - used as remote online storage of my code.
- [Balsamiq](https://balsamiq.com/) - used for wireframes

### Front-End 

- HTML - base markup language
- CSS - base cascading style sheets
- [jQuery](https://jquery.com/) - used for JavaScript functionality
- [Materialize](https://materializecss.com/) - used as frontend framework
- [Cart.js](https://www.chartjs.org/) - used for interactive chart
- [FontAwesome](https://fontawesome.com/) - used as icon library
- [Google Fonts](https://fonts.google.com/) - used for project fonts


### Back-End

- [Django](https://docs.djangoproject.com/en/3.2/) - used as main framework
- [Heroku](https://www.heroku.com/) - used as app remote hosting platform
- [Python](https://www.python.org/) - used as backend programming language
- [ElephantSQL](https://www.elephantsql.com/) - remote PostgreSQL database
- [Cloudinary](https://cloudinary.com/) - used for static files as remote storage


<br>

## Testing
For an overview of all the testing conducted, please refer to the [TESTING.md](https://github.com/e-kai00/expense-tracker/blob/main/TESTING.md) file.

<br>

## Deployment

### Local Deployment
 
**Clone the repositary:**
- go to the [expense-tracker](https://github.com/e-kai00/expense-tracker) repositary
- click on the "Code" button, located just above the file list
- in the dropdown menu, click on the clipboard icon to copy the repository's URL
- open the terminal in your code editor and navigate to the directory where you want to clone the repository
- run the following command:
  - `git clone https://github.com/e-kai00/expense-tracker.git`
- install packages from the [requirements.txt](https://github.com/e-kai00/expense-tracker/blob/main/requirements.txt) file using this command:
  - `pip3 install -r requirements.txt`
- create a `.env` file for your own credentials
- to launch the Django app, run command:
  - `python3 manage.py runserver`
- to stop the app:
  - `CTRL+C`
- make migrations to set up the database:
  - `python3 manage.py makemigrations`
  - `python3 manage.py migrate`  
- create superuser to access the Django Admin Panel:
  - `python3 manage.py createsuperuser`

**ElephantSQL Database**

To sign up with ElephantSQL and create a new database, you follow these steps:

- go to the ElephantSQL  [ElephantSQL](https://www.elephantsql.com/) website
- sign-up with your GitHub account
- click **Create new instance**
- enter a name and choose plan (recommended free Tiny Turtle)
- select the region and data center closest to you
- once created, click on the new database name to view the database URL
- use the database URL as a credential in your `.env` file

**Cloudinary**

To sign up for Cloudinary, follow these steps:
- go to the [Cloudinary](https://cloudinary.com/) website
- click on the "Sign Up" button and fill in the registration form
- in your dashboard copy your **API Environment variable**
- add the obtained API Environment variable to your `.env` file

### Heroku Deployment

This project is deployed on Heroku, a cloud platform. To deploy the project, follow these steps:

- create a [Heroku](https://www.heroku.com/) account
- click **Create New App**
- choose name for your app and region
- once app created, navigate to *Settings* and click **Reveal Config Vars**
- set your environment variables:
  | Key | Value |
  |-----|-------|
  | `SECRET_KEY`| *your_django_secret_key* |
  |`DATABASE_URL`| *your ElephantSQL database URL*|
  | `CLOUDINARY_URL`| *your API Environment variable*|

For proper deployment and execution of the application, Heroku needs *requirements.txt* and *Procfile*:
- `pip3 install -r requirements.txt` - to install project's requirements.txt
- `echo web: gunicorn tracker.wsgi > Procfile` - to create Procfile


*The files for this project can be found here: [requirements.txt](https://github.com/e-kai00/expense-tracker/blob/main/requirements.txt) and [Procfile](https://github.com/e-kai00/expense-tracker/blob/main/Procfile)*
  

- Navigate to **Deploy** tab
- Connect your GitHub account and choose needed repositary
- Scroll down and click **Deploy Branch** (this project deployed from main branch)
- Once succeesfully deployed, click **Open app** at the right top coner of the page



<br>

## Credits

### Content
### Media
### Code
### Acknowledgments

