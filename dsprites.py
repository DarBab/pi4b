import pygame as p
import random as r
import time as tm

cool = p.image.load('/home/pi/rush.png')
space = p.image.load('/home/pi/—Pngtree—star celestial body planet space_416048.JPG')
p.init()
p.display.init()
width = 800
height = 400
thing = [0] * 4
screen = p.display.set_mode([width,height])
q = p.image.load('/home/pi/rush.png')

    
while True:
    x: int = 0
    y: int = 0
    p.Surface.blit(screen,space,(0,0))
    screen.blit(q,(x,y))
    p.display.update()

