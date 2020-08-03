# Computer Science Fundamentals I - Assignment 4

## Description
Data files are very common in many disciplines. They form the input for a variety of different kinds of processing, analysis, summaries, etc. An associated problem is to maintain these data files – to add information, update or correct information. Manually updating data files can be tedious and can lead to errors. A common approach is to use a program – an “update” program that takes a data file and a file of “updates” and then creates a new version of the data file with the updates applied. In this assignment you will create a complete program that will update an existing data file containing information about countries.

## Learning Outcomes
- Strings and text files
- Writing and using your own classes
- Testing code
- Using complex data structures (i.e., lists, sets and dictionaries)

## Tasks
Task 1
- Implement a class Country that holds the information about a single country; name the file country.py.

Task 2
- Implement a class called CountryCatalogue; name the file catalogue.py. This class will use a file to build the data structures to hold the information about countries. The file data.txt contains information about a number of countries.

Task 3
- Implement a Python module, called processUpdates.py, that has a function processUpdates(cntryFileName, updateFileName). This function takes two parameters: the first parameter will be the name of a file containing country data (e.g. data.txt). The second file will contain the name of a file containing updates. Each record in the update file specifies updates for a single country. 
