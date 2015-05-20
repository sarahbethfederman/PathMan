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
title = arcadeFont48.render("PATHMAN", 1, (0, 255, 0))
subTitle = arcadeFont24.render("PATTERN RECOGNITION MAZE GAME", 1, (0, 255, 0))
titleRect = title.get_rect()
subTitleRect = subTitle.get_rect()

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
    #p.add_operation('+1')
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

            if main_character.pos_x == playGrid.rows - 1:
                if main_character.pos_y == playGrid.cols -1:
                    print("Winner! ")

                    global playing
                    playing = False

start()
run()
