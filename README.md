# Stock Analysis and Forecast Terminal (S.A.F.T.)
## The Specification and Analysis is --> [here](https://github.com/dannim272/Non-Exam-Assesment/tree/master/written-spec)
coded in nvim btw

Overview: this program is designed to help the user with research of stocks for either early hours trading or investing - I will probably say this multiple times in the writing of this project but it must be noted that this program is only fit for use in the early hours of market

> [!WARNING]
> before **final** submit make sure to:
> 1. delete 'main()' from terminal.py
> 2. clear out the logins.db database (figure it out)
> 3. compile the whole thing and make sure it works - [this may work](https://www.geeksforgeeks.org/create-a-single-executable-from-a-python-project/)

## Table of Contents
- **Documentation + all theoretical**
    - [project ideas](https://github.com/dannim272/Non-Exam-Assesment/blob/master/theory/Project%20Ideas.md)
    - [specification](https://github.com/dannim272/Non-Exam-Assesment/blob/master/theory/Specification.md)
- [**Installation**](#installation)
    - [program](#program---download-the-program-repo)
    - [libraries](#libraries)
- [**Execution**](#execution)
- [**Things to implement**](#things-to-implement)

## Installation
### Program - download the program repo
```bash
git clone https://github.com/dannim272/Non-Exam-Assesment.git
```
### Libraries
pip:
```bash
pip install tkinter, sqlite3, smtplib, requests, sys, time
```
pip3:
```bash
pip3 install tkinter, sqlite3, smtplib, requests, sys, time
```

## Execution
python:
```bash
python terminal.py
```
python3:
```bash
python3 terminal.py
```

## Things to implement
- Make the API work for current ticker price display - **DONE**
    - was a stupid mistake of infinite recursion
- Implement the regression model of some sort or something similar - **not going to work, so i'll do something less crazy**
- Make the interface more appealing (probably darker colors) - **get done ASAP**
- may implement graphs to compare spider (SP500) to other stocks
    - this will require checkbutton, may work later on this (like on the weekend haha)
