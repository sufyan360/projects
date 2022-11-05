"""
Create the towers of hanoi using recursion
Name: Sufyan Chaudhry
"""
def tower(disk, start, placeholder, finish):
    if disk == 1:
        print ("Move disk 1 from ",start,"to",finish)
        return
    else:
        tower(disk-1, start, placeholder, finish)
        print ("Move disk",disk,"from",start,"to",finish)
        tower(disk-1, placeholder, finish, start)


x = int(input("How many disks do you want? "))
tower(x,"A","B","C")
