"""
This program will take user input and then convert it into a different unit of measure
Name: Sufyan Chaudhry
"""
name= input("What is your full name? ")
print("Hello,",name)

print("This program will ask you to input measurments and will display them converted")
print(" ")

try:
    f1= eval(input("What is the temperature in Fahrenheit? "))
    c1= (f1-32)/1.8
    print(f1,"F is equal to: %.2f" % c1,"C")

except:
    print("Invalid Input")

        
try:
    c2= eval(input("What is the temperature in Celsius? "))
    f2=c2*1.8+32
    print(c2,"C is equal to: %.2f" % f2,"F")
    
except:
    print("Invalid Input")

try:
    p1= eval(input("How many pounds do you want to convert to kilograms? "))
    kg1= p1/2.2046
    print(p1,"LB is eqaul to: %.2f" % kg1, "KG")

except:
    print("Invalid Input")

try:
    p2= eval(input("How many pounds do you want to convert to grams? "))
    g2= p2*453.592
    print(p2,"LB is eqaul to: %.2f" % g2, "G")
except:
    print("Invalid Input")

try:
    mi1= eval(input("How many miles do you want to convert to kilometers? "))
    km1= mi1 * 1.6
    print(mi1,"MI is equal to: %.2f" % km1,"KM")
except:
    print("Invalid Input")

try:
    ft1= eval(input("How many feet do you want to convert to meters? "))
    m1= ft1/3.208
    print(ft1,"FT is equal to: %.2f" % m1,"M")

except:
    print("Invalid Input")
    
try:
    gal1= eval(input("How many gallons do you want to convert to liters? "))
    l1= gal1 * 3.785412
    print(gal1,"GAL is equal to: %.2f" % l1,"L")
except:
    print("Invalid Input")

try:
    pt1= eval(input("How many pints do you want to convert to milliliters? "))
    ml1= pt1 * 473.176473
    print(pt1,"PT is equal to: %.2f" % ml1,"ML")
except:
    print("Invalid Input")
print("Thank you for your time!")
