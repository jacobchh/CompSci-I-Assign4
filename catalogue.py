# Hello this is Jacob Chun
# Today is December 1, 2019
# The following program initializes a CountryCatalogue object which allows users to store and access data

import sys
from .country import Country


class CountryCatalogue:

    def __init__(self, countryFile):

        # creates an empty list which is the basic data structure used to store information
        self._countryCat = []

        # try block for dealing with processing a file in case it is in the wrong format and raises an error
        try:
            file = open(countryFile, "r", encoding="utf‐8")
            for line in file:

                # deals with some files containing headers and some not
                if ("Country" or "Continent" or "Population" or "Area") in line:
                    continue

                # deals with random blank lines in the file
                if line != ("\n" or ""):
                    lst = line.strip().split("|")
                    length = len(lst)

                    # if there are more than four values, we will ignore this line
                    if length > 4:
                        continue

                    # deals with the error of the file not having all three vertical bars
                    elif length == 1:
                        self._countryCat.append(Country(lst[0], "", "", ""))
                    elif length == 2:
                        self._countryCat.append(Country(lst[0], "", "", lst[1]))
                    elif length == 3:
                        self._countryCat.append(Country(lst[0], lst[2], "", lst[1]))
                    elif length == 4:
                        self._countryCat.append(Country(lst[0], lst[2], lst[3], lst[1]))

        # handles the error of an unreadable file
        except ValueError:
            print("Error: File in the incorrect format!")
            sys.exit()

        # handles the error of an unreadable file
        except IndexError:
            print("Error: File in the incorrect format!.")
            sys.exit()

        # handles the error of the program crashing for any reason
        except RuntimeError as error:
            print("Error:", str(error))
            sys.exit()

    # finds the object in countryCat with the same name and updates that object's population
    def setPopulationOfCountry(self, countryName, population):
        for element in self._countryCat:
            if element.getName() == countryName:
                element.setPopulation(population)
                return True
        return False

    # finds the object in countryCat with the same name and updates that object's area
    def setAreaOfCountry(self, countryName, area):
        for element in self._countryCat:
            if countryName == element.getName():
                element.setArea(area)
                return True
        return False

    # finds the object in countryCat with the same name and updates that object's continent
    def setContinentOfCountry(self, countryName, continent):
        for element in self._countryCat:
            if countryName == element.getName():
                element.setContinent(continent)
                return True
        return False

    # simply checks to see if a country (based on name) exists in the countryCat
    def findCountry(self, country):
        tempLst = []
        for element in self._countryCat:
            tempLst.append(element.getName())
        if country.getName() in tempLst:
            return country
        else:
            return None

    # method for adding any countries that were not initialized originally
    def addCountry(self, countryName, pop, area, cont):
        country = Country(countryName, pop, area, cont)
        if country not in self._countryCat:
            self._countryCat.append(country)
            return True
        else:
            return False

    # displays a representation of all country objects in the catalogue
    def printCountryCatalogue(self):
        # sorts the objects alphabetically based on their name
        lst = sorted(self._countryCat, key=lambda country: country.getName())
        for element in lst:
            print(element)

    # saves the catalogue into a data file
    def saveCountryCatalogue(self, fname):

        # try block in case the file raises and error
        try:
            output = open(fname, "w", encoding="utf-8")
            count = 0

            # sorts the list to print alphabetically
            lst = sorted(self._countryCat, key=lambda country: country.getName())
            output.write("Country|Continent|Population|Area\n")
            for element in lst:
                output.write(
                    element.getName() + "|" + element.getContinent() + "|" +
                    element.getPopulation() + "|" + element.getArea() + "\n")
                count = count + 1
            output.close()
            return count

        # handles the error of a file that cannot be opened or written in
        except IOError:
            print("Error: File could not opened or written in!")
            return -1

        # catches all errors
        except:
            print("Error: File could not opened or written in!")
            return -1
