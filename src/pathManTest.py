from pattern import *
from grid import *
from player import *

adding_Operations = True
adding_Seed = False
p = Pattern()

print("Please add operations. When done, type 'finished'")

while adding_Operations == True:
    user_input = raw_input("Add an operation: ")

    if user_input == "finished":
        adding_Operations = False
        adding_Seed = True
    if adding_Operations != False:
        print("Attempting to add: " + user_input)
        p.add_operation(user_input)

while adding_Seed == True:
    user_input = raw_input("Select a seed (any number): ")
    g = Grid(10, 10, 0, user_input, p)
    adding_Seed = False


g.generate_grid()
g.print_grid()

print(p.humanize())