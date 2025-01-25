import pygame as p
import random as r
import time as t
p.init()
screen = p.display.set_mode((1280, 720))
block = p.Rect(200,200,100,100)
block.topleft = (100,100)
pic = p.image.load('/home/pi/Downloads/Mario - Climb2.gif')
mar = [0] * 50
marg = p.sprite.Group()

class mario(p.sprite.Sprite):
    def __init__(self,x,y,dx,dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        super().__init__()
    def move(self):
        self.rect.x += self.dx
        if self.rect.x <= 0:
            self.rect.x = 0
            self.dx = -self.dx    
        if self.rect.x >= 1260:
            self.rect.x = 1260
            self.dx = -self.dx    
        self.rect.y += self.dy
        if self.rect.y <= 0:
            self.rect.y = 0
            self.dy = -self.dy    
        if self.rect.y >= 700:
            self.rect.y = 700
            self.dy = -self.dy    

for i in range(5):
    dx = r.randint(-10,10)
    dy = r.randint(-10,10)
    mar[i] = mario(r.randint(0,1260),r.randint(0,700),dx,dy)
    marg.add(mar[i])
screen.fill("BLACK")
p.display.set_caption("lick me")

while True:
    for go in range (50):
        for i in range (5):
            screen.fill("BLACK")
            marg.draw(screen)
            p.display.flip()
            mar[i].move()
    quit()

