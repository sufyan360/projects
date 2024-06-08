"""
This program uses data and displays it into a graph.
Name: Sufyan Chaudhry

Department Name       , Total number of employees
Marketing             , 50
Information Technology, 275
Management            , 230
Human Resources       , 250
Finance               , 92
Supply Chain          , 73
Manufacturing         , 30

Year ; Profit in $USD
2009 ; $175,000
2010 ; $250,000
2011 ; $525,000
2012 ; $239,000
2013 ; $1,000,000
2014 ; $1,000,500
2015 ; $500,000
2016 ; $740,000
2017 ; $5,625,000
2018 ; $100,000,000
"""

import matplotlib.pyplot as plt
def piechart():
    
    #pie chart
    employees = [50, 275, 230, 250, 92, 73, 30]

    slice_labels = ["Marketing", "Information Technology", "Management", "Human Resources","Finance", "Supply Chain", "Manufacturing"]

    plt.pie(employees, labels = slice_labels)
    plt.title("Total Number of Employees")

    plt.show()

def linegraph():
    
    #line graph
    x_coords = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    y_coords = [175000, 250000, 525000, 239000, 1000000, 1000500, 500000, 740000, 5625000, 100000000]

    plt.plot(x_coords, y_coords)

    plt.title("Profit by Year")

    plt.xlabel("Years")
    plt.ylabel("Profit in $USD")

    plt.show()

def bargraph():
    x = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    y = [175000, 250000, 525000, 239000, 1000000, 1000500, 500000, 740000, 5625000, 100000000]

    plt.xlabel("Years")
    plt.ylabel("Profit is $USD")
    plt.title("Profit by Year")
    
    plt.bar(x, y)

    plt.show()

def main():
    piechart()

    linegraph()

    bargraph()

main()

