#!/usr/bin/env python3

import urllib.request
import re

class Tour(object):


    def __init__(self, *cities):
        """ Every elements in cities must be string. This checks that, otherwise,
            ignores those nonstrings.
        """
        self.__city = []
        for c in cities:
            if type(c) == str:
                self.__city.append(c)

    def __add__(self, other):
        """ Concatenate a tour to the end of other tour.
        """
        return Tour(*(self.__city + other.__city))
    
    def __mul__(self, other):
        """ Repeated concatenation of this tour, where the single argument
            indicates the number of times to cycle through the cities and must therefore be a nonnegative
            integer. (tour * number)
        """
        if type(other) != int:
            raise TypeError
        elif other < 0:
            raise ValueError
        elif other == 0:
            return Tour()
        else:
            city_list = []
            for i in range(other):
                city_list += self.__city
            return Tour(*(city_list))

    def __rmul__(self, other):
        """ Repeated concatenation of this tour, where the single argument
            indicates the number of times to cycle through the cities and must therefore be a nonnegative
            integer. (number * tour)
        """
        return self.__mul__(other)
    
    def __str__(self):
        """ Called by print() so you can print the tour, just like any other data structure.
        """
        return ' ==> '.join([c for c in self.__city])

    def __repr__(self):
        """ This method is called if you simply enter a tour name in the shell.
            It simply calls, the same method that prints a tour.
        """
        return self.__str__

    def __gt__(self, other):
        """ Compare the driving distance of this tour to that of another tour
        """
        return self.__distance > other.__distance

    def __lt__(self, other):
        """ Compare the driving distance of this tour to that of another tour
        """
        return self.__distance < other.__distance

    def __eq__(self, other):
        """ Compare this tour to another tour for equality, where the tours are considered
            equal if they visit precisely the same cities in the same order.
        """
        return self.__city == other.__city

    def distance(self, method = 'driving'):
        """ By using Google Map API to caculate the total distance for the tour
        """
        self.__distance = 0;
        for i in range(len(self.__city)-1):
            query = "http://maps.googleapis.com/maps/api/distancematrix/json?origins=" + re.sub(r'[\W]*\s', '+', self.__city[i]) + "&destinations=" + re.sub(r'[\W]*\s', '+', self.__city[i+1]) + "&mode=" + method + "&sensor=false"
            web = urllib.request.urlopen(query)
            result = str(web.read())
            self.__distance += dist_parse(result)
        return (self.__distance)

def dist_parse(page):
    m = re.search(r'(?<="value" : )[\d]+', page)
    return(float(m.group(0)))
            



def main():
    t1 = Tour("New York, NY", "Lansing, MI", "Sacramento, CA")
    t2 = Tour("Oakland, CA")
    t3 = Tour("Sacramento, CA", "Oakland, CA")
    print("t1: {}\nt2:{}\nt3:{}".format(t1,t2,t3))
    print("t1 distances: driving-{} km; biking-{} km; walking-{} km".format(
    round(t1.distance()/1000), round(t1.distance('bicycling')/1000),
    round(t1.distance('walking')/1000)))
    print("Using driving distances from here on.")
    t4 = t1 + t2
    print("t4:", t4)
    print("t4 driving distance:", round(t4.distance()/1000),"km")
    print("t4 == t1 + t2:", t4 == t1 + t2)

if __name__ == "__main__":
    main()

    
        

