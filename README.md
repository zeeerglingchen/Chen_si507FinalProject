# Project Title

Chenyang Lyu

[Link to this repository](https://github.com/zeeerglingchen/Chen_si507FinalProject)

---

## Project Description


My project will analyze any given account from the Chinese social media Weibo and enable people to know how many fake/robot followers the particular account has . The project will allow users to test any weibo account they want to test and get visualized results of the fake/robot fans from multiple aspects like the ratios, genders, locations, devices the fake fans are using and etc .

## How to run

1. run `python SI507project_run.py`

## How to use

1. input the id of the weibo account and click on submit, if you are not familiar with weibo, you can choose one id from here [1787211337, 1874279777,1905089717,6449716047]
2. it might take up to one minute to process, please wait
3. you will see a new page displaying the composition of fans of the weibo account if the id has not been tested before. Otherwise the page will tell you to go to the history page
4. if you go to the history page you will see a list of clickable id number, click on one of them
5. you will see the results of the weibo account you just selected


## Routes in this application
- `/` -> this is the home page where you can submit a new test or check the test history
- `/get_data` -> this route will display the composition of fans of the weibo account
- `/result` -> this route will display the testing history
- `/result/<id>` -> this route will display a particular account's information that has been tested and stored in the results route

## How to run tests
1. make sure you have tested the id 1787211337 before run tests, you should have a
1787211337.csv in your directory by running `python SI507project_run.py` and inputting the id 1787211337
2. run `python SI507project_tests.py`

## In this repository:

- SI507project_tools.py
- SI507project_tests.py
- SI507project_run.py

- templates
  - index.html
  - error.html
  - getdata.html
  - result.html

- db example
  - fans.db

- README.md
- requirements.txt
- database_schema.jpg
- ifcodeworkswell.pdf
---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [x] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [ ] Project includes at least 1 test suite file with reasonable tests in it.
- [x] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [x] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [x] At least one form in your Flask application
- [x] Templating in your Flask application
- [ ] Inclusion of JavaScript files in the application
- [x] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [x] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [ ] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [x] Caching of data you continually retrieve from the internet in some way

### Submission
- [x] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [x] I included a summary of my project and how I thought it went **in my Canvas submission**!
