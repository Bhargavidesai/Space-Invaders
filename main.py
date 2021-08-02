import pygame
import random
import math
# this class will help in adding music to our game
from pygame import mixer

# initializing the pygame
pygame.init()

# to run main game loop
run = False

# creating the screen (width and height) --> top most left corner (0,0) topmost right(700,0) downmost left(0,750) downmost right(700,750)
screen = pygame.display.set_mode((700, 750))

status='over'

# caption of the window
pygame.display.set_caption("Space Invaders")

# adding logo to the window
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# background image
background = pygame.image.load('bg.jpg')
bg = pygame.image.load('title.jpg')
l2=pygame.image.load('level2.jpg')
l3=pygame.image.load('level3.jpg')

# title
titleimg = pygame.image.load('name.png')

# message font
msg_font = pygame.font.SysFont('Stencil', 70)

# clock
clock = pygame.time.Clock()

# button
buttonimg = pygame.image.load('button.png')
msg = pygame.font.SysFont('Stencil', 50)

def title():
    screen.blit(bg, (0, 0))
    screen.blit(titleimg, (100, 250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()


# backgroung music
# mixer.music is used bcz it is played continuesly
mixer.music.load('background.wav')
# -1 makes the music to play continuesly in the background form a loop
mixer.music.play(-1)


# title
title()
clock.tick(0.4)


def button():
    #display menu on the screen
    m_text = msg_font.render('MENU', True, (250, 250, 250))
    m_line = msg_font.render('-----------', True, (250, 250, 250))
    screen.blit(m_text, (260, 150))
    screen.blit(m_line, (250, 185))
    # display play text on the button image
    screen.blit(buttonimg, (250, 300))
    play_text = msg.render('PLAY', True, (0, 0, 0))
    screen.blit(play_text, (295, 325))
    # display quit text on the button image
    screen.blit(buttonimg, (250, 400))
    quit_text = msg.render('QUIT', True, (0, 0, 0))
    screen.blit(quit_text, (295, 425))
    #detectes the mouse movements on the screen
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #if the mouse cursor is with in the range of play button then this will be true
    if 276 < mouse[0] < 421 and 310 < mouse[1] < 379:
        #if we left click on the mouse this will be true
        if click == (True, False, False):
            return 1
    # if the mouse cursor is with in the range of quit button then this will be true
    if 276 < mouse[0] < 421 and 416 < mouse[1] < 479:
        # if we left click on the mouse this will be true , exits the game
        if click == (True, False, False):
            pygame.quit()
            quit()


# countdown
def message(i):
    n = ['    3  ', '    2  ', '    1  ', 'START']
    text = n[i]
    msg_text = msg_font.render(text, True, (250, 250, 250))
    # display start at the center of the screen
    screen.blit(msg_text, (250, 350))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()

# menu
def menu():
    intro=False
    while intro == False:
        screen.blit(bg, (0, 0))
        ret=button()
        if ret==1:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

# menu
menu()

# countdown
count = 4
run = True
for i in range(count):
    screen.blit(bg, (0, 0))
    clock.tick(1)
    message(i)
    clock.tick(10)

# score
score_value = 0
level=1
# font style of the score and size
# SysFont use the system font to style the text
font = pygame.font.SysFont('Castellar', 29)
textX = 10
textY = 10
#level position
levelX = 550
levelY = 10


# score fuction display score on the screen
def showscore(x, y,lx,ly):
    score = font.render('Score : ' + str(score_value), True, (250, 250, 250))
    screen.blit(score, (x, y))
    levelfont = font.render('LEVEL : '+ str(level), True, (250, 250, 250))
    screen.blit(levelfont, (lx, ly))


# gameover function
def game_over_text():
    over_text = msg_font.render('GAME OVER', True, (250, 250, 250))
    # display game over at the center of the screen
    screen.blit(over_text, (150, 350))


# player
playerimg = pygame.image.load('player.png')
# setting the position of the player image on the screen
# as image is 64x64 setting the x any y should not be exactly like 700 or 750
playerX = 330  # sets the image to center of x axis
playerY = 640  # set the image to just above the end of y axis
playerX_change = 0  # for the movement of player in x axis


# player function
def player(x, y):
    # this blit method will display player on the screen
    screen.blit(playerimg, (x, y))


# for creating multiple enemy we are creating a list
speed_e=0.35
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 6

# creates the specified number of enemies
for i in range(num_of_enemy):
    enemyimg.append(pygame.image.load('en.png'))
    # setting the random position of the enemy image on the screen
    # as image is 64x64 setting the x any y should not be exactly like 700 or 750
    enemyX.append(random.randint(0, 636))  # random position in x axis
    enemyY.append(random.randint(50, 150))  # random position in y axis
    enemyX_change.append(0.35)  # for the movement of enemy in x axis
    enemyY_change.append(40)  # for the movement of enemy in y axis


# enemy function
def enemy(x, y, i):
    # this blit method will display enemy on the screen
    screen.blit(enemyimg[i], (x, y))


# bullet
# bullet image loading
bulletimg = pygame.image.load('bullet.png')
# y axis is constant as player is shooting the bullet standing in constant y axis its only changing the x axis
bulletX = 0
bulletY = 640
bulletY_change = 2  # this will set the velocity of the bullet
# ready state--> we cannot see the bullet on the screen
# fire state --> we will see the moving bullet on the screen
bullet_state = 'ready'


# bullet function
# display the bullet on the screen
def shoot(x, y):
    global bullet_state
    bullet_state = 'fire'
    # this adding 16 makes the bullet to appear on the center of the spaceship
    # and adding 10 makes the bullet to apper on the little bit above the spaceship
    screen.blit(bulletimg, (x + 16, y + 10))


# collision fuction
# calculates the distance b/w bullet and enemy
def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(((enemyX - bulletX) ** 2) + ((enemyY - bulletY) ** 2))
    # if the distance b/w bullet and enemy is less than 27 then returns True
    if distance < 27:
        return True
    else:
        return False

def win():
    winimg=pygame.image.load('win.png')
    screen.blit(winimg,(300,345))
    win_text = msg_font.render('WON!!', True, (250, 250, 250))
    # display game over at the center of the screen
    screen.blit(win_text, (250, 420))


# Game loop
while run:
    # screen should be on the top than player function.
    # bcz player is drawen on the screen not below the screen soo screen will be set 1st and then player will be drawen
    # RGB(red,green,blue) colour to the display window makes the window black
    # screen.fill((0, 0, 0))
    # to make the background image to remain persistant on the screen we are writing it inside the while loop
    if level==1:
        screen.blit(background, (0, 0))
    elif level==2:
        screen.blit(l2,(0,0))
    else:
        screen.blit(l3,(0,0))


    # decreasing the value of x player moves left ,increasing the values of x palyer moves right
    # playerX-=0.1
    # playerX+=0.1

    # decreasing te value of y player moves upwards ,increasing the value of y player moves down
    # playerY-=0.1
    # playerY+=0.1

    # while loop will run on every click on the keyboard [left,right,up,down,space]
    # this while loop will terminate only when close(x) is clicked event will be quit
    # events and written inside the for loop
    for event in pygame.event.get():

        # closes the gaming window
        if event.type == pygame.QUIT:
            run = False

        # this is true when a we click any button in the keyboard
        if event.type == pygame.KEYDOWN:

            # this will be true only when left button is clicked
            if event.key == pygame.K_LEFT:
                playerX_change = -0.9  # negative value to move left
            # this will be true only when right button is clicked
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.9  # positive value to move right
            # this will be true when space bar is pressed and this will call the shoot fuction to shoot the bullet
            if event.key == pygame.K_SPACE:
                # if the bullet state ready then only we can shoot the bullet
                if bullet_state == 'ready':
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX  # by this bullet will not follow the player once the bullet is shooted and x axis of the bullet will be set to  axis of the player as player is shooting the bullet
                    shoot(bulletX, bulletY)  # shoot fuction call

        # this is true when any clicked button is released
        if event.type == pygame.KEYUP:

            # this is true if left or right pressed key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0  # zero value for no movement as the key is released

    # altering the major x axis for the movement of the player
    # examaple: 5 = 5 + -0.3 --> 5 - 0.3 , 5 = 5 + 0.3 --> 5 + 0.3 [ where 5 being major x axis]
    playerX += playerX_change

    # setting the boundaries to the player so that ot should not go beyond the screen
    # for left
    if playerX <= 0:
        playerX = 0
    # for right --> as player image is 64x64 700-64=636 will be the boundary for the player
    elif playerX >= 636:
        playerX = 636

    # enemy movement
    # altering the major x axis for the movement of the enemy
    # examaple: 5 = 5 + -0.3 --> 5 - 0.3 , 5 = 5 + 0.3 --> 5 + 0.3 [ where 5 being major x axis]
    # i specifies the compiler which enemy is x and y axis are being considered
    # as we have created multiple enemies the for loop help in applying condition to all the enemies
    for i in range(num_of_enemy):
        # game over if enemy reaches this y axis
        if enemyY[i] > 575 and status=='over':
            for j in range(num_of_enemy):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        # setting the boundaries to the enemy so that ot should not go beyond the screen
        # for left
        if enemyX[i] <= 0:
            # movement towards right when it hits the left boundary
            enemyX_change[i] = speed_e
            # moving down when it hits the boundary left boundary
            enemyY[i] += enemyY_change[i]
        # for right --> as enemy image is 64x64 700-64=636 will be the boundary for the enemy
        elif enemyX[i] >= 636:
            # movement to left when it hits the right boundary
            enemyX_change[i] = -speed_e
            # moves down when it hits the right boundary
            enemyY[i] += enemyY_change[i]

        # collision
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound('explosion.wav')
            collision_sound.play()
            bulletY = 640  # if the collision occurs the bullet is set to its orignal place
            bullet_state = 'ready'
            score_value += 5
            # once the collsion occurs the enemy destroyes and appears again in different position
            enemyX[i] = random.randint(0, 636)  # random position in x axis
            enemyY[i] = random.randint(50, 150)  # random position in y axis

        # calling enemy function
        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 640  # when the bullet reaches the end of the screen we can shoot the new bullet from the spaceship
        bullet_state = 'ready'
    if bullet_state == 'fire':
        shoot(bulletX, bulletY)  # shoot function call
        bulletY -= bulletY_change  # moves the y toward upwards by decresing the value of y axis

    # calling player function
    player(playerX, playerY)

    # calling showscore function
    showscore(textX, textY,levelX,levelY)

    #levels according to score and increasing the speed of enemy
    if score_value >=50 and score_value <= 100:
        level=2
        speed_e=0.5
    elif score_value >100 and score_value<=150:
        level=3
        speed_e=0.7
    elif score_value==200:
        status='win'
        for i in range(num_of_enemy):
            for j in range(num_of_enemy):
                enemyY[j] = 2000
            win()
            break


    # for updating the display
    pygame.display.update()
