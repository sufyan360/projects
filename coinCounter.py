"""
This program uses Gui to get user input on how many of each type of coin they have.
The total is then calculated from that input
Name: Sufyan
"""
from tkinter import *
window = Tk()

#class Coin():
  #  def __init__(self, window):
#self.window = window
window.title("Change Counter")
window.geometry("725x300")

intructions = Label(window, text = "Enter the number of each coin, then click compute.(If you have none enter 0)")
intructions.grid(column=1, row=0)


penny = Label(window, text="Pennies($.01) :").grid(column=0, row=1)
nickel = Label(window, text="Nickels($.05) :").grid(column=0, row=2)
dime = Label(window, text="Dimes($.10) :").grid(column=0, row=3)
quarter = Label(window, text="Quarters($.25) :").grid(column=0, row=4)
halfdollar = Label(window, text="Half-dollars($.50) :").grid(column=0, row=5)
dollarcoin = Label(window, text="Dollar coins($1.00) :").grid(column=0, row=6)


penny1 = Entry(window, width=10)
penny1.grid(column = 1, row = 1)
        
nickel1 = Entry(window, width=10)
nickel1.grid(column = 1, row = 2)
        
dime1 = Entry(window, width=10)
dime1.grid(column = 1, row = 3)
        
quarter1 = Entry(window, width=10)
quarter1.grid(column = 1, row = 4)
        
halfdollar1 = Entry(window, width=10)
halfdollar1.grid(column = 1, row = 5)
        
dollarcoin1 = Entry(window, width=10)
dollarcoin1.grid(column = 1, row = 6)

totalL = Label(window, text="Total: ").grid(column=1, row=7)


penny2 = Label(window, text="$0.00")
penny2.grid(column=2, row=1)
        
nickel2 = Label(window, text="$0.00")
nickel2.grid(column=2, row=2)
        
dime2 = Label(window, text="$0.00")
dime2.grid(column=2, row=3)
        
quarter2 = Label(window, text="$0.00")
quarter2.grid(column=2, row=4)
        
halfdollar2 = Label(window, text="$0.00")
halfdollar2.grid(column=2, row=5)
        
dollarcoin2 = Label(window, text="$0.00")
dollarcoin2.grid(column=2, row=6)

total =Label(window, text="$0.00")
total.grid(column=2, row=7)


        
def calculate():
    if int(penny1.get())>0:
        int_penny = int(penny1.get())
        pennyMoney = int_penny * 0.01
        penny2.config(text="$"+str(pennyMoney))
    else:
        pennyMoney = 0.0
        penny2.config(text="Invalid")
        
        
    if int(nickel1.get())>0:
        int_nickel = int(nickel1.get())
        nickelMoney = int_nickel * 0.05
        nickel2.config(text="$"+str(nickelMoney))
    else:
        nickelMoney = 0.0
        nickel2.config(text="Invalid")
        
    if int(dime1.get())>0:
        int_dime = int(dime1.get())
        dimeMoney = int_dime * 0.10
        dime2.config(text="$"+str(dimeMoney))
    else:
        dimeMoney = 0.0
        dime2.config(text="Invalid")
        
    if int(quarter1.get())>0:
        int_quarter = int(quarter1.get())
        quarterMoney = int_quarter * 0.25
        quarter2.config(text="$"+str(quarterMoney))
    else:
        quarterMoney = 0.0
        quarter2.config(text="Invalid")
        
    if int(halfdollar1.get())>0:
        int_halfdollar = int(halfdollar1.get())
        halfdollarMoney = int_halfdollar * 0.50
        halfdollar2.config(text="$"+str(halfdollarMoney))
    else:
        halfdollarMoney =0.0
        halfdollar2.config(text="Invalid")
        
    if int(dollarcoin1.get())>0:
        int_dollarcoin = int(dollarcoin1.get())
        dollarcoinMoney = int_dollarcoin * 1.00
        dollarcoin2.config(text="$"+str(dollarcoinMoney))
    else:
        dollarcoinMoney = 0.0
        dollarcoin2.config(text="Invalid")

    totalMoney = pennyMoney + nickelMoney + dimeMoney + quarterMoney + halfdollarMoney + dollarcoinMoney
    totalMoney = round(totalMoney,2)
    
    total.config(text="$" + str(totalMoney))
        
                       
#gui = Coin(window)

compute = Button(window, text="Compute", command=calculate).grid(column=1, row=10)

window.mainloop()
                


        
        




        
        
        

        
        

        
    
