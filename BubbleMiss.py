#!/usr/bin/vipul
# coding: utf-8

# 

##importing required libraries
import pygame
import random
import numpy
import math
import time
##initialising Pygame module
pygame.init()
## Definig color codes
black = (0,0,0)
white = (255,255,255)
Red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
##defining width and height of the window
h = 600
w = 800
gameDisplay = pygame.display.set_mode((w,h))
pygame.display.set_caption('Baloon shooter')  #Title
clock = pygame.time.Clock() #clock
## Defining shapes and sizes
def cannon(cx,cy):  ##The cannon
    pygame.draw.rect(gameDisplay, black, (cx, cy, 150, 100))
    pygame.draw.rect(gameDisplay, black, (cx-25, cy+25, 100, 50))
cx= w*0.9
cy = h*0.35

def baloon(bx,by):  #The baloon 
    pygame.draw.circle(gameDisplay, green ,(int(bx),int(by)), 50)
bx= w*0.10
by = h*0.35

def bullet(bux,buy):  #the bullet
    pygame.draw.rect(gameDisplay, (100,100,100), (bux, buy, 25, 25))
    #gameDisplay.blit(bulletImg,(bux,buy))
    
def ending(x,y):   #The ending screen
    pygame.draw.rect(gameDisplay, (100,100,100), (x, y, 800, 600))
#Initializing font type and size
myfont = pygame.font.SysFont('Comic Sans MS', 30)

bux=0   #bullet x coordinate
buy = h*0.35  #bullet x coordinate
handler = 0  #cannon velocity
crash = False  ## Crash condition
bhandler = 5  ## Bubble velocity  
bullet_state = False  # state of the bullet
buh=0   #bullet velocity initially
fired=False  # condition of bullet
counter = 0   #Miss counter
gameover = False   # True When game ends 

while not crash:
    if gameover == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #when player clicks on close button
                crash=True
            if event.type == pygame.KEYDOWN:  ## Key down moves cannon down
                if event.key == pygame.K_DOWN:
                    handler=5
                if event.key == pygame.K_UP:  ##Key up moves cannon up
                    handler = -5
                if event.key == pygame.K_SPACE:   ##space shoots bullets through the cannon with 1.5 times the velocity
                    if fired == False:
                        bullet_state = True
                        buy=cy+40
                        bux = cx-50
                        buh = 7.5
                        fired = True
            if event.type == pygame.KEYUP:      ##when user leaves the key the cannon should stop moving 
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    handler=0
        ## Movement and animation calculations and logic below.
        bhandler=bhandler*numpy.random.choice([1,-1], p=[0.99, 0.01])
        if by >=h-50 or by <= 0+50:
            bhandler=bhandler*-1    
        gameDisplay.fill(white)
        if cy <=0:
            cy=cy+5
        elif cy >=h-100 :
            cy=cy-5
        cy+=handler
        cannon(cx,cy)
        by+=bhandler
        baloon(bx,by)    

        if bullet_state:
            bux=bux-buh
            bullet(bux,buy)
        if bux<=0:
            if bullet_state:
                counter +=1
            fired = False
            bullet_state=False

        ### Detecting the bullet hits the cannon by distance formula between two points.
        if math.sqrt(math.pow(bx-(bux+25/2),2) + math.pow(by - (buy+25/2),2)) <50:
            bullet_state = False
            fired=False
            gameover=True
    else:
        ending(0,0)
        textsurface1 = myfont.render("Bullets Missed: "+str(counter), False, (255, 0, 0))
        textsurface2 = myfont.render("Credits: Vipul Jad", False, (0, 0, 0))
        gameDisplay.blit(textsurface1,(w*0.4,h/2))
        gameDisplay.blit(textsurface2,(w*0.65,h*0.8))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash=True
    pygame.display.update()
    clock.tick(60)
pygame.quit()







