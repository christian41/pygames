#!/usr/bin/env python
import pygame, sys, time, random
from pygame.locals import *
pygame.init()
fpsClock=pygame.time.Clock()
playerName = raw_input("what is your name?")
screenX = int(raw_input("how wide do you want the game?  "))
screenY = int(raw_input("how tall do you want the game?  "))
initialSpeed = int(raw_input("How fast do you want to go? [1-40]  "))
print "OK ",playerName,", I'm making a game that is ", screenX,"wide and ",screenY," tall, and starting with a speed of",initialSpeed,"!"
playSurface=pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption('raspberry snake')
redColour=pygame.Color(255, 0, 0)
blackColour=pygame.Color(0, 0, 0)
whiteColour=pygame.Color(255, 255, 255)
greyColour=pygame.Color(150, 150, 150)
highScore = 0

def initialize():
    global score
    global speed
    global snakePosition
    global snakeSegments
    global raspberryPosition
    global raspberrySpawned
    global direction
    global changeDirection

    score = 0
    speed = initialSpeed
    snakePosition=[100,100]
    snakeSegments=[[100,100],[80,100],[60,100]]
    raspberryPosition=[300,300]
    raspberrySpawned=1
    direction='right'
    changeDirection=direction


def printAwesome():
    awesomeFont=pygame.font.Font('freesansbold.ttf',72)
    awesomeSurf=awesomeFont.render("Awesome "+playerName+"!  Score = "+str(score),True, redColour)
    awesomeRect=awesomeSurf.get_rect()
    awesomeRect.topleft=(10, 10)
    playSurface.blit(awesomeSurf, awesomeRect)
    pygame.display.flip()
    time.sleep(1)

def checkHighScore():
    global highScore
    if score>highScore:
        highScore = score
        print "new high score!"+str(highScore)
        highScoreFont=pygame.font.Font('freesansbold.ttf',72)
        highScoreText = 'New High Score!'
        highScoreSurf=highScoreFont.render(highScoreText,True, whiteColour)
        highScoreRect=highScoreSurf.get_rect()
        highScoreRect.topleft=(10, 100)
        playSurface.blit(highScoreSurf, highScoreRect)
        pygame.display.flip()
        time.sleep(2)
        
def printGameOver():
    gameOverFont=pygame.font.Font('freesansbold.ttf',72)
    gameOverText = 'Game Over '+playerName+"  Score = "+str(score)
    gameOverSurf=gameOverFont.render(gameOverText,True, greyColour)
    gameOverRect=gameOverSurf.get_rect()
    gameOverRect.topleft=(10, 10)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(2)
    
def gameOver():
    printGameOver()
    checkHighScore()
    wantContinue = raw_input("Do you want to play again? [y/n]")
    if wantContinue=="y":
        initialize()
    else:
        pygame.quit()
        sys.exit()

initialize()                            
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key==K_RIGHT or event.key ==ord('d'):
                changeDirection='right'
            if event.key ==K_LEFT or event.key== ord('a'):
                changeDirection='left'
            if event.key ==K_UP or event.key==ord('w'):
                changeDirection='up'
            if event.key == K_DOWN or event.key==ord('s'):
                changeDirection='down'
            if event.key== K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
    if changeDirection=='right' and not direction=='left':
        direction = changeDirection
    if changeDirection=='left' and not direction=='right':
        direction = changeDirection
    if changeDirection=='up' and not direction=='down':
        direction = changeDirection
    if changeDirection=='down' and not direction=='up':
        direction = changeDirection
    if direction == 'right':
        snakePosition[0] +=20
    if direction == 'left':
        snakePosition[0] -=20
    if direction == 'up':
        snakePosition[1] -=20
    if direction == 'down':
        snakePosition[1] +=20

    snakeSegments.insert(0,list(snakePosition))
    if snakePosition[0]==raspberryPosition[0] and snakePosition[1]==raspberryPosition[1]:
        raspberrySpawned = 0
        score+=1
        printAwesome()
        speed+=1
    else:
        snakeSegments.pop()
    if raspberrySpawned==0:
        x=random.randrange(1,int(screenX/20))
        y=random.randrange(1,int(screenY/20))
        raspberryPosition= [int(x*20),int(y*20)]
        raspberrySpawned=1

    playSurface.fill(blackColour)
    for position in snakeSegments:
        pygame.draw.rect(playSurface,whiteColour,Rect(position[0],position[1],20,20))
        pygame.draw.rect(playSurface,redColour,Rect(raspberryPosition[0],raspberryPosition[1],20,20))
    pygame.display.flip()

    if snakePosition[0] > screenX or snakePosition[0] < 0:
        gameOver()
    if snakePosition[1] > screenY or snakePosition[1] < 0:
        gameOver()

    for snakeBody in snakeSegments[1:]:
        if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
            gameOver()

    fpsClock.tick(speed)
                            
