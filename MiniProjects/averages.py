"""
Program uses looping to find averages for user inputed values.
Name: Sufyan 
"""
print("Welcome! This program with calculate the output voltage of your generators")
generators=int(input("How many generators do you want to average? "))
total=0 
for i in range(generators):
    print("Please enter three test voltages.")
    r1=eval(input("Voltage reading 1: "))
    r2=eval(input("Voltage reading 2: "))
    r3=eval(input("Voltage reading 3: "))
    avg= (r1+r2+r3)/3
    print("The average output voltage for generator",i+1,"is %.2f" % avg)
    total=total+avg
    i+=1
total=total/generators
print("The total average of your",generators,"generator(s) is: %.2f" % total)
    
    
    
