import pygame as p
from dataclasses import dataclass
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

@dataclass
class thang(p.sprite.Sprite):
    x: float
    y: float
    dx: float
    dy: float


    def bounce(s):
        p.Surface.blit(screen,cool,(s.x,s.y))
        s.x+=s.dx
        s.y+=s.dy
        if (s.x>=800):
           s.x=800
           s.dx=-s.dx
        if (s.y>=400):
           s.y=400
           s.dy=-s.dy
        if (s.x<=0):
           s.x<=0
           s.dx=-s.dx
        if (s.y<=0):
           s.y<=0
           s.dy=-s.dy
           

    def drop(s):
        p.Surface.blit(screen,cool,(s.x,s.y))
        s.v+=s.g
        s.a+=s.v
        s.y+=s.a
        if (s.y>=400):
         s.y=400
         s.a=-s.a
        if (s.x > 800):
         s.x=0

       
thing[0] = thang(400,200,1,1)
thing[1] = thang(400,200,1,-1)
thing[2] = thang(400,200,-1,1)
thing[3] = thang(400,200,-1,-1)

while True:
    p.display.update()
    p.Surface.blit(screen,space,(0,0))
    thing[0].bounce()
    thing[1].bounce()
    thing[2].bounce()
    thing[3].bounce()
