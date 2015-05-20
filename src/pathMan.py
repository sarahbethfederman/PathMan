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

game_clock = pygame.time.Clock()
clock_seconds = 60
clock_millisec = 0

running = False
playing = False

p = Pattern()
playGrid = Grid()
main_character = Player(0,0,playGrid)

levels_won = 0
levels_lost = 0

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

    global game_clock
    global clock_seconds
    global clock_millisec
    game_clock = pygame.time.Clock()
    clock_seconds = 60
    clock_millisec = 0

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
            screen.blit(backgroundImg, (0, 0))
            screen.blit(title, (20, 20))
            screen.blit(subTitle, (215, 35))
            display_grid()
            display_pattern()
            display_levels()

            update_clock()

            #handle events here! 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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

                    global levels_won
                    levels_won += 1

                    global playing
                    playing = False

                    start()
            pygame.display.flip()

def display_grid():
    for x in range(0, playGrid.rows):
        for y in range(0, playGrid.cols):
            if main_character.pos_x == x and main_character.pos_y == y:
                number = arcadeFont18.render(str(playGrid.get_tile(y, x)), 1, (0, 255, 0))
            elif str(str(y) + ", " + str(x)) in main_character.visitedPath:
                number = arcadeFont18.render(str(playGrid.get_tile(y, x)), 1, (0, 147, 0))
            elif str(str(y) + ", " + str(x)) in main_character.mistakesTracker:
                number = arcadeFont18.render(str(playGrid.get_tile(y, x)), 1, (147, 0, 0))
            elif x == 0 and y == 0:
                number = arcadeFont18.render(str(playGrid.get_tile(y, x)), 1, (0, 147, 255))
            elif x == playGrid.rows -1 and y == playGrid.cols -1:
                number = arcadeFont18.render(str(playGrid.get_tile(y, x)), 1, (0, 147, 255))
            else: 
                number = arcadeFont18.render(str(playGrid.get_tile(y, x)), 1, (147, 147, 147))

            screen.blit(number, (((x * 50) + 50), ((y * 50) +90)))

def display_pattern():
    patternDisp = arcadeFont24.render(str(p.humanize()), 1, (0, 255, 0))
    screen.blit(patternDisp, (590, 270))

def display_levels():
    global levels_won
    global levels_lost

    won_text = arcadeFont24.render("Levels Won: " + str(levels_won), 1, (0, 255, 0))
    lost_text = arcadeFont24.render("Levels Lost: " + str(levels_lost), 1, (255, 0, 0))  
    
    screen.blit(won_text, (590, 370))
    screen.blit(lost_text, (590, 400))  

def update_clock():
    global game_clock
    global clock_millisec
    global clock_seconds

    if clock_millisec > 1000:
        clock_seconds -= 1
        clock_millisec -= 1000

    timerText = arcadeFont48.render(str(clock_seconds), 1, (255, 0, 0))
    timerTextRect = timerText.get_rect()

    screen.blit(timerText, (650, 170))
    pygame.display.flip()

    clock_millisec += game_clock.tick_busy_loop(60)

    if clock_seconds <= 0:
        print("GAME OVER")

        global levels_lost
        levels_lost += 1

        global start
        start()

start()
run()
