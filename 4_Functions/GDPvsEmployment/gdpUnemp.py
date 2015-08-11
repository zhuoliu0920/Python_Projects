#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt

class Error(Exception):
    """General error"""
    pass

class InvalidInputError(Error):
    """Error with invalid error"""
    pass

def findAvgGDP(filename, year):
    with open(filename, 'r') as gdp_file:
        gdp_quantitles = gdp_file.read().strip().split()
        year_index = [i for i,x in enumerate(gdp_quantitles) if year in x]
        gdp_index = [i+1 for i in year_index]
        gdps_in_year = list(map(float, [gdp_quantitles[x] for x in gdp_index]))       
        gdp = sum(gdps_in_year) / len(gdps_in_year)
        return(gdp)

def findAvgUnemp(filename, year):
    with open(filename, 'r') as unemp_file:
        all_unemp = csv.reader(unemp_file, delimiter=',', quotechar='|')
        unemp_in_year = [row for row in all_unemp if row[0] == year]
        unemp = sum(list(map(float, (unemp_in_year[0])[1:12]))) / 12
        return(unemp)

def getPlot(filename1, filename2):
    # extract information from file1 (GDP file)
    with open(filename1, 'r') as gdp_file:
        gdp_quantitles = gdp_file.read().strip().split()
        gdp_time = [x for i,x in enumerate(gdp_quantitles) if i%2 == 0]
        gdp_value = list(map(float, [x for i,x in enumerate(gdp_quantitles) if i%2 != 0]))
        qq = ['q1', 'q2', 'q3', 'q4']
        for i,x in enumerate(gdp_time):
            for j,q in enumerate(qq):
                if q in x:
                    gdp_time[i] = float(x.replace(q, "")) + 0.125 + j*0.25

    # extract information from file2 (Unemp file)
    with open(filename2, 'r') as unemp_file:
        all_unemp = csv.reader(unemp_file, delimiter=',', quotechar='|')
        next(all_unemp, None)  # skip the headers
        unemp_time = []
        unemp_value = []
        for row in all_unemp:
            for i in range(0,12):
                unemp_time.append(float(row[0])+(i/12)+1/24)
            unemp_value.extend(row[1:13])

    # Plotting
    fig, ax1 = plt.subplots()
    ax1.plot(gdp_time, gdp_value, 'b-')
    ax1.set_xlabel('year')
    ax1.set_ylabel('GDP', color='b')

    ax2 = ax1.twinx()
    ax2.plot(unemp_time, unemp_value, 'r-')
    ax2.set_ylabel('Unemployment rate', color='r')

    plt.show()
            
    

def main():
    gdp_file = input("GDP File Name:")
    unemp_file = input("Unemployment File Name:")
    getPlot(gdp_file, unemp_file)
    while True:
        try:
            year = input('Year to examine:')
            if (int(year) > 2008 or int(year) < 1948):
                raise InvalidInputError
            else:
                gdp = findAvgGDP(gdp_file, year)
                unemp = findAvgUnemp(unemp_file, year)
                print("For {0}, average GDP: {1:.3f} and average unemployment: {2:.2f}\n".format(year, gdp, unemp))
                break
        except (InvalidInputError, ValueError):
            print("Bad year, try again")

def test():
    gdp_file = 'gdp.txt'
    unemp_file = 'unemp.csv'
    getPlot(gdp_file, unemp_file)

if __name__ == "__main__":
    main()
        
    

