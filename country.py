# Hello this is Jacob Chun
# Today is December 1, 2019
# The following program initializes a Country object with the given parameters


class Country:

    # initializes an object of class Country with various instance variables
    def __init__(self, name, pop, area, continent):
        self._name = name
        self._pop = pop
        self._area = area
        self._continent = continent

    # returns a string representation of a given country object
    def __repr__(self):
        return self._name + " (pop: " + str(self._pop) + ", size: " + str(self._area) + ") in " + self._continent

    # returns the name of a country object
    def getName(self):
        return self._name

    # returns the population of a country object
    def getPopulation(self):
        return self._pop

    # returns the area of a country object
    def getArea(self):
        return self._area

    # returns the continent of a country object
    def getContinent(self):
        return self._continent

    # sets the population of a country object
    def setPopulation(self, newPop):
        self._pop = newPop

    # sets the area of a country object
    def setArea(self, newArea):
        self._area = newArea

    # sets the continent of a country object
    def setContinent(self, newContinent):
        self._continent = newContinent
