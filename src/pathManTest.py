from pattern import *
from grid import *
from player import *

adding_Operations = True
adding_Seed = False
playing = False

p = Pattern()

print("")
print("----WELCOME to PATHMAN-------")
print("----SETUP: Add Operations----")

print("Please add operations. When done, type 'finished' or type 'standard' for a standard grid")

while adding_Operations == True:
    user_input = raw_input("Add an operation: ")

    if user_input == "finished":
        adding_Operations = False
        adding_Seed = True
    elif user_input == "standard":
        p = Pattern()
        p.add_operation('+5')
        p.add_operation('+1')
        p.add_operation('+4')
        g = Grid(10, 10, 0, 2, p)
        adding_Operations = False

    if adding_Operations != False:
        print("Attempting to add: " + user_input)
        p.add_operation(user_input)

while adding_Seed == True:
    print("----SETUP: Select Seed----")
    user_input = raw_input("Select a seed (any number): ")
    g = Grid(10, 10, 0, user_input, p)
    adding_Seed = False

g.generate_grid()

playing = True
main_character = Player(0, 0, g.rows, g.cols, g.path)

print("------GAME BEGIN------")
print("-----Turn: " + str(main_character.move_counter) + " ---------------------------")
print("-----Mistakes: " + str(main_character.mistakes_counter) + " -----------------------")
print("-----Current player location: " + str(main_character.pos_y) + ", " + str(main_character.pos_x) + " -----")
print("-----Pattern: " + str(p.humanize()) + " ------")
g.print_grid()

print(p.humanize())

print("Now Playing. Use commands 'up' 'down' 'right' and 'left' to move")

while playing == True:
    user_input = raw_input("Which way would you like to move: ")

    if user_input == "quit":
        playing = False
        print("Quiting...")

    if playing == True:
        main_character.move(user_input)
        print("-----Turn: " + str(main_character.move_counter) + " ---------------------------")
        print("-----Mistakes: " + str(main_character.mistakes_counter) + " -----------------------")
        posOutput = "-----Current player location: " + str(main_character.pos_y) + ", " + str(main_character.pos_x) + " -----"
        print(posOutput)
        print("-----Pattern: " + str(p.humanize()) + " ------")
        g.print_grid()

        if main_character.pos_x == main_character.rows - 1:
            if main_character.pos_y == main_character.cols -1:
                print("Winner! ")
                playing = False