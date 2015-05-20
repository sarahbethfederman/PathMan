import sys, pygame

from pattern import *
from grid import *
from player import *

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
screenRect = screen.get_rect()

backgroundImg = pygame.image.load("../assets/images/bg.png")
backgroundRect = backgroundImg.get_rect()

arcadeFont48 = pygame.font.Font("../assets/font/ARCADECLASSIC.TTF", 48)
arcadeFont24 = pygame.font.Font("../assets/font/ARCADECLASSIC.TTF", 24)
arcadeFont18 = pygame.font.Font("../assets/font/ARCADECLASSIC.TTF", 18)

title = arcadeFont48.render("PATHMAN", 1, (0, 255, 0))
subTitle = arcadeFont24.render("PATTERN RECOGNITION MAZE GAME", 1, (0, 255, 0))

running = False
playing = False

p = Pattern()
playGrid = Grid()
main_character = Player(0,0,playGrid)

running = True

print("WELCOME to PATHMAN")
print("SETTING UP AUTOMATIC LEVEL...")

def start(): 
    print("Starting.")
    
    global p
    p = Pattern()

    p.add_operation(str('+' + str(random.randrange(5, 9))))
    p.add_operation(str('-' + str(random.randrange(1, 4))))
    print(str(p.humanize()))

    global playGrid
    playGrid = Grid(10, 10, 0, int(random.randrange(0, 100)), p)
    playGrid.generate_grid()

    global main_character
    main_character = Player(0, 0, playGrid)

    global playing
    playing = True

    screen.blit(backgroundImg, (0, 0))
    screen.blit(title, (20, 20))
    screen.blit(subTitle, (215, 35))
    display_grid()
    display_pattern()
    pygame.display.flip()

def run():
    playGrid.print_grid(0, 0)

    #quiting is allowed at any time...
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            print("Quitting!")
            sys.exit()

    while running == True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                print("Quitting!")
                sys.exit()

        while playing == True:

            #handle events here! 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    print("Quitting!")
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        main_character.move("up")
                    elif event.key == pygame.K_DOWN:
                        main_character.move("down")
                    elif event.key == pygame.K_RIGHT:
                        main_character.move("right")
                    elif event.key == pygame.K_LEFT:
                        main_character.move("left")

                    playGrid.print_grid(main_character.pos_y, main_character.pos_x)
                    display_grid()

            if main_character.pos_x == playGrid.rows - 1:
                if main_character.pos_y == playGrid.cols -1:
                    print("Winner! ")

                    global playing
                    playing = False

                    start()

def display_grid():
    for x in range(0, playGrid.rows):
        for y in range(0, playGrid.cols):
            if main_character.pos_x == x and main_character.pos_y == y:
                print("drawing player")
                number = arcadeFont18.render(str(playGrid.get_tile(y, x)), 1, (0, 255, 0))
            elif x == 0 and y == 0:
                print("drawing start")
                number = arcadeFont18.render(str(playGrid.get_tile(y, x)), 1, (0, 147, 255))
            elif x == playGrid.rows -1 and y == playGrid.cols -1:
                print("drawing end")
                number = arcadeFont18.render(str(playGrid.get_tile(y, x)), 1, (0, 147, 255))
            else: 
                number = arcadeFont18.render(str(playGrid.get_tile(y, x)), 1, (147, 147, 147))

            screen.blit(number, (((x * 50) + 50), ((y * 50) +90)))
    pygame.display.flip()

def display_pattern():
    patternDisp = arcadeFont24.render(str(p.humanize()), 1, (0, 255, 0))
    screen.blit(patternDisp, (590, 270))

start()
run()
