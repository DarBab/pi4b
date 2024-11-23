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

class thang(p.sprite.Sprite):
 
   def drop():
        p.Surface.blit(screen,cool,(10,10))

       
while True:
    p.display.update()
    p.Surface.blit(screen,space,(0,0))
    q = p.image.load('/home/pi/rush.png')
    d = q.get_rect()
    gh = p.sprite.Sprite.Group.add(d)
    p.sprite.Sprite.add(d,gh)
    
