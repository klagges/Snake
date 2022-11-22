import pygame
import random

clock = pygame.time.Clock()
# setdir = "r"                        # Startdirection
food = False  # Essen beim ersten durchlauf nicht geöffnet
pos_listx = []
pos_listy = []
## Color################
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
##### Hitbox für essen
add_hitBox = 10

# bildschirmauflösung
high = 800
widh = 600
pos_x = high // 2  # Schlangen start Position
pos_y = widh // 2  # Schlangen start Position

pos2_x = 0
pos2_y = 0
pos2_x_min = pos2_x - 1
pos2_x_max = pos2_x + 1
pos2_y_min = pos2_y - 1
pos2_y_max = pos2_y + 1
textRect1 = 0
spd = 2  # Bewegungsgeschwindigkeit
points = 0
game_over = False
overmenu = False
running = True


def stars():
    global pos_x, pos_y
    global setdir
    global food
    global pos2_y
    global pos2_x
    global pos2_y_min
    global pos2_y_max
    global pos2_x_max
    global pos2_x_min
    global pos_listx
    global pos_listy
    global screen, textRect1, points
    global spd
    global game_over
    global overmenu
    print(" Setze zurück")
    pos_x = high // 2  # Schlangen start Position
    pos_y = widh // 2  # Schlangen start Position

    pos2_x = 0
    pos2_y = 0
    pos2_x_min = pos2_x - 1
    pos2_x_max = pos2_x + 1
    pos2_y_min = pos2_y - 1
    pos2_y_max = pos2_y + 1
    textRect1 = 0
    spd = 2  # Bewegungsgeschwindigkeit
    points = 0
    game_over = False
    overmenu = False


def buildscreen():
    global screen
    pygame.display.set_caption("Snake . . . .")
    screen = pygame.display.set_mode((high, widh))
    # initializing pygame
    pygame.font.init()
    pygame.font.get_init()


def collisionWall():
    if pos_x <= high:
        return True
    elif pos_x >= 1:
        return True
    elif pos_y <= 1:
        return True
    elif pos_y >= widh:
        return True
    else:
        print("no clollision")


def foodpos():
    global pos2_y
    global pos2_x
    global pos2_y_min
    global pos2_y_max
    global pos2_x_max
    global pos2_x_min

    pos2_y = random.randint(10, widh - 10)
    pos2_x = random.randint(10, high - 10)
    pos2_x_min = pos2_x - add_hitBox
    pos2_x_max = pos2_x + add_hitBox
    pos2_y_min = pos2_y - add_hitBox
    pos2_y_max = pos2_y + add_hitBox


def start():
    global running
    font2 = pygame.font.SysFont('freesanbold.ttf', 60)
    font3 = pygame.font.SysFont('freesanbold.ttf', 30)
    overmenu = True
    while overmenu:

        # print("overmenu")
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                overmenu = False
                running = False
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                overmenu = False
                running = False
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_s:
                main()

        screen.fill(black)
        pygame.draw.rect(screen, white, [180, 200, 400, 400], 0)
        ## Zeiger Menu
        if game_over:
            text_go = font2.render('Game Over', True, (black))


        else:
            text_go = font2.render('Snake', True, (black))
            text_inf = font3.render(' Drücke "s" zum Starten '
                                    '  oder Esc zum Beenden', True, (red))

        text_goRect1 = text_go.get_rect()
        text_infRect1 = text_inf.get_rect()

        text_goRect1.center = (300, widh // 2)
        text_infRect1.center = (200, 100)

        screen.blit(text_go, text_goRect1)
        screen.blit(text_inf, text_infRect1.center)
        # pygame.draw.rect(screen, red, [0, 0, high, widh], 5)
        pygame.display.flip()
        clock.tick(30)


def end():
    global running
    global overmenu
    overmenu = False
    running = False


def gover():
    print(" Game Is Ofver bildschirm")


def main():
    # Clear screen
    global pos_x, pos_y
    setdir = "r"
    global spd
    global food
    global pos2_y
    global pos2_x
    global pos2_y_min
    global pos2_y_max
    global pos2_x_max
    global pos2_x_min
    global pos_listx
    global pos_listy
    global screen, textRect1, points
    snake_lang = 65
    global game_over
    global running
    font1 = pygame.font.SysFont('freesanbold.ttf', 30)
    font2 = pygame.font.SysFont('freesanbold.ttf', 60)

    while running:
        ###############################

        ##############

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
        # print(pos_x, pos_y, Setze richtung in die die Schlange geht)

        if setdir == "r":  # right
            pos_x += 1 * spd
        elif setdir == "l":  # left
            pos_x -= 1 * spd
        elif setdir == "u":  # up
            pos_y -= 1 * spd
        elif setdir == "d":  # down
            pos_y += 1 * spd
        ## Prüfe Wand collision Oben unten, recht und links
        if pos_x >= high:
            # print("col1",pos_x, high)
            game_over = True
            running = False
        elif pos_x <= 1:
            # print("col2")
            game_over = True
            running = False
        elif pos_y <= 1:
            # print("col3")
            game_over = True
            running = False
        elif pos_y >= widh:
            # print("col4")
            game_over = True
            running = False

        ### Collision kopf mit körper
        if len(pos_listx) > 15:
            for c in range(5, len(pos_listx)):
                if pos_listx[c] <= pos_x <= pos_listx[c]:
                    if pos_listy[c] <= pos_y <= pos_listy[c]:
                        print(pos_listx[c], pos_listy[c], pos_y, pos_x)
                        game_over = True
                        running = False

        ## Prüfe Food Collision
        # collisionWall()
        if pos2_x_min <= pos_x <= pos2_x_max:
            if pos2_y_min <= pos_y <= pos2_y_max:
                print("col1", pos_x, pos2_x)
                snake_lang += 5
                points += 10
                if points % 100 == 0: spd += 1
                food = False

        # print("Y",pos2_y_min,pos2_y_max)
        # print("x", pos2_x_min, pos2_x_max)

        #### Prüfe Tasteneingaben
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and setdir != "r":
            setdir = "l"
        if key[pygame.K_RIGHT] and setdir != "l":
            setdir = "r"
        if key[pygame.K_UP] and setdir != "d":
            setdir = "u"
        if key[pygame.K_DOWN] and setdir != "u":
            setdir = "d"
        if key[pygame.K_s]:
            game_over = False
        ## Spielfeld lleren
        screen.fill(black)

        if not food:
            foodpos()

            food = True
        # print(snake_lang)

        ## Snake
        pygame.draw.rect(screen, red, [pos_x, pos_y, 10, 10], 0)
        # aktuell_pos = pos_x, pos_y
        pos_listx.append(pos_x)
        pos_listy.append(pos_y)
        if len(pos_listx) >= snake_lang:
            pos_listx.pop(0)
            pos_listy.pop(0)

        pygame.draw.circle(screen, green, [pos2_x, pos2_y], 5, 0)
        # print(pos_listx)
        # print(len(pos_listx))
        if len(pos_listx) >= 5:
            pos_listx.reverse()
            pos_listy.reverse()
            for i in range(0, len(pos_listx)):
                # print("test")
                pygame.draw.rect(screen, red, [pos_listx[i], pos_listy[i], 10, 10], 0)
            pos_listx.reverse()
            pos_listy.reverse()

            # for i in range(0, len(pos_list):
            #    pygame.draw.rect(screen, red, [aktuell_pos, 10, 10], 0)
        # print(snake_lang)
        text1 = font1.render(f'Punkte = {points}', True, white)
        textRect1 = text1.get_rect()
        # setting center for the first text
        textRect1.center = (700, 20)
        screen.blit(text1, textRect1)
        pygame.draw.rect(screen, red, [0, 0, high, widh], 5)
        pygame.display.flip()
        clock.tick(60)


buildscreen()
start()
main()
if game_over: gover()
end()
