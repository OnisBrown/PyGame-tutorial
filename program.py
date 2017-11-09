# Import the modules
import sys
import random
import pygame

import math
from pygame.locals import *


pygame.init()
width = 1200
height = 1200
keys = [False,False,False,False]
position = [(width/2)-1, (height/2)-1]
speed = 5

screen = pygame.display.set_mode((width, height))
player = pygame.image.load("resources/images/dude.png")
background = pygame.image.load("resources/images/grass.png")

def FrameDeltaTime():
    global LastFrameTime
    delta = int(round(time.time()*1000)) - LastTimeframe
    LastFrame = int(round(time.time()*1000))
    return delta

#game loop
while True:
    screen.fill(0)


    for x in range(width/background.get_width()+1):
        for y in range(height/background.get_height()+1):
            screen.blit(background, (x*100, y*100))



    mposition =pygame.mouse.get_pos()
    angle = math.atan2(mposition[1]-position[1], mposition[0]-position[0])
    PlayerRot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = ((position[0]-PlayerRot.get_rect().width/2), (position[1]-PlayerRot.get_rect().height/2))
    screen.blit(PlayerRot, playerpos1)
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            if event.key == K_a:
                keys[1] = True
            if event.key == K_s:
                keys[2] = True
            if event.key == K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[0] = False
            if event.key == K_a:
                keys[1] = False
            if event.key == K_s:
                keys[2] = False
            if event.key == K_d:
                keys[3] = False


    if keys[0]:
        position[1]-= speed
    if keys[2]:
        position[1]+= speed
    if keys[1]:
        position[0]-= speed
    elif keys[3]:
        position[0]+= speed