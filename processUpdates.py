# Hello this is Jacob Chun
# Today is December 1, 2019
# The following program takes a data file and creates a country catalogue with country objects
# It will then take an update file that can add, or replace the information of an individual object in the catalogue

from .country import *
from .catalogue import *


def processUpdates(cntryFileName, updateFileName):

    while True:
        # try block for opening the data file
        try:
            dataFile = open(cntryFileName, "r", encoding="utf-8")
            break

        # if the file cannot be opened, it will prompt the user to enter a new one until it is valid or exits
        except IOError:
            print("Error: Data file was not found!")
            answer = input("Would you like to quit? Type 'Y' (yes) or 'N' (no): ")
            if answer == "N":
                cntryFileName = input("Please enter the name of the data file you wish you process: ")

            # prints a response in an output file if the user chooses to quit
            else:
                output = open("output.txt", "w", encoding="utf-8")
                output.write("Update Unsuccessful\n")
                output.close()
                return False

    # if the data file is valid, it will initialize a country catalogue object
    data = CountryCatalogue(cntryFileName)

    while True:
        # try block for opening the update file
        try:
            updateFile = open(updateFileName, "r", encoding="utf‐8")
            break

        # if the file cannot be opened, it will prompt the user to enter a new one until it is valid or exits
        except IOError:
            print("Error: Update file was not found!")
            answer = input("Would you like to quit? Type 'Y' (yes) or 'N' (no): ")
            if answer == "N":
                updateFileName = input("Please enter the name of the data file you wish you process: ")

            # prints a response in an output file if the user chooses to quit
            else:
                output = open("output.txt", "w", encoding="utf-8")
                output.write("Update Unsuccessful\n")
                output.close()
                return False

    while True:
        # try loop processes the update file that the user has chose
        try:
            for line in updateFile:

                # sets blank variables each iteration
                pop = ""
                area = ""
                continent = ""
                if line != ("\n" or ""):
                    lst = line.strip().split(";")

                    # if the list is greater than length four, it will skip the line
                    if len(lst) > 4:
                        continue

                    # retrieves the  values of population, area, and continent
                    else:
                        for i in range(len(lst)):
                            lst[i] = lst[i].strip()
                            if lst[i].startswith("P="):
                                pop = lst[i].strip("P=")
                            if lst[i].startswith("A="):
                                area = lst[i].strip("A=")
                            if lst[i].startswith("C="):
                                continent = lst[i].strip("C=")

                        # if the country exists in the catalogue, it will proceed to update the values
                        # if the variables retrieved from the update file are not blank strings, it will update
                        name = Country(lst[0], "", "", "")
                        if data.findCountry(name) == name:
                            if pop != "":
                                data.setPopulationOfCountry(lst[0], pop)
                            if area != "":
                                data.setAreaOfCountry(lst[0], area)
                            if continent != "":
                                data.setContinentOfCountry(lst[0], continent)

                        # if the country does not exist in the catalogue, it will create a new object and add it
                        else:
                            data.addCountry(lst[0], pop, area, continent)

            # this saves the file and returns a value of True for an external main program
            data.saveCountryCatalogue("output.txt")
            return True

        # handles the error of an unreadable file
        except ValueError:
            print("Error: File in the incorrect format!")
            return False

        # handles the error of an unreadable file
        except IndexError:
            print("Error: File in the incorrect format!.")
            return False

        # handles the error of the program crashing for any reason
        except RuntimeError as error:
            print("Error:", str(error))
            return False

        # catches all other errors that may occur
        except:
            print("An issue has occurred! The program will now exit!")
            return False
