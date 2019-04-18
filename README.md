# Project Title

Chenyang Lyu

[Link to this repository](https://github.com/zeeerglingchen/Chen_si507FinalProject)

---

## Project Description


My project will analyze any given account from the Chinese social media Weibo and enable people to know how many fake/robot followers the particular account has . The project will allow users to test any weibo account they want to test and get visualized results of the fake/robot fans from multiple aspects like the ratios, genders, locations, devices the fake fans are using and etc .

## How to run

1. run `python SI507project_tests.py`
<!-- for now, you only need to run this file to see the test result, but in the future, you need to run by code like `server run`  -->

## How to use

1. type in the id of the weibo account and click on submit
2. click on
3. (Optional): Markdown syntax to include an screenshot/image: ![alt text](image.jpg)

## Routes in this application
- `/home` -> this is the home page
- `/account/<id>` -> this route will display the general information of the weibo account
- `/fake_fans/<id>` -> this route will display the overall fake fans information of the weibo account
- `/fans/homepage/<div>` -> this route will display a particular fan's information

## How to run tests
1. copy the proxy address and the id number into the tool files

## In this repository:

- SI507project_tools.py
- SI507project_tests.py
- README.md
---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [ ] Project is submitted as a Github repository
- [ ] Project includes a working Flask application that runs locally on a computer
- [ ] Project includes at least 1 test suite file with reasonable tests in it.
- [ ] Includes a `requirements.txt` file containing all required modules to run program
- [ ] Includes a clear and readable README.md that follows this template
- [ ] Includes a sample .sqlite/.db file
- [ ] Includes a diagram of your database schema
- [ ] Includes EVERY file needed in order to run the project
- [ ] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [ ] Includes at least 3 different routes
- [ ] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [ ] Interactions with a database that has at least 2 tables
- [ ] At least 1 relationship between 2 tables in database
- [ ] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [ ] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [ ] At least one form in your Flask application
- [ ] Templating in your Flask application
- [ ] Inclusion of JavaScript files in the application
- [ ] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [ ] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [ ] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [ ] Caching of data you continually retrieve from the internet in some way

### Submission
- [ ] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [ ] I included a summary of my project and how I thought it went **in my Canvas submission**!
