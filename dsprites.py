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
class thang(p.sprite.Sprite):
    def __init__(self,x,y):
        p.sprite.Sprite.__init__()
        one = p.sprite.Group()
        p.sprite.Sprite.add(one,d)
        print(d,one)

    def drop():
        p.Surface.blit(screen,cool,(10,10))
        print('gh')
       
while True:
    p.display.update()
    p.Surface.blit(screen,space,(0,0))
    q = p.image.load('/home/pi/rush.png')
    d = q.get_rect()
