coded in nvim btw
# Pre-Market Condition terminal (PMCt)
# The Specification and Analysis is --> [here](https://github.com/dannim272/Non-Exam-Assesment/tree/master/written-spec)

> [!WARNING]
> this software / project is supposed to be treated as a toy, DO NOT make any financial decisions with even partial help of this thing
> also for the love of G-d dont risk more than 1% of your capital per trade

## Overview:
- This program is designed to help those who are new to trading to minimise headache of 'cherry picking' stocks to trade; this is done with the help of APIs, filters and displays. The program is simple, and is intended to get rid of all the distractions by essentially leaving only one thing to the user - where to **buy** and where to **sell** stocks

## Table of Contents
- **Documentation + all theoretical**
    - [project ideas](https://github.com/dannim272/Non-Exam-Assesment/blob/master/theory/Project%20Ideas.md)
    - [specification](https://github.com/dannim272/Non-Exam-Assesment/blob/master/theory/Specification.md)
- [**Running the program**]
- [**Things to implement**](#things-to-implement)

## Running the program
- assuming you're in the Non-Exam-Assesment repo do following:
```bash
cd dist
./PMCt
```
- else, cd into the Non-Exam-Assesment repo and then do the same thing

## Things to implement
- Make the API work for current ticker price display - **DONE**
    - was a stupid mistake of infinite recursion
- Implement the regression model of some sort or something similar - **not going to work, so i'll do something less crazy**
- Make the interface more appealing (probably darker colors) - **get done ASAP**
- may implement graphs to compare spider (SP500) to other stocks
    - this will require checkbutton, may work later on this (like on the weekend haha) - **done with 'caviat'**
