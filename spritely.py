import pygame as p
import random as r
p.init()
width = 1024
height = 768
screen = p.display.set_mode((width,height))
mar = [0] * 50
marg = p.sprite.Group()
padg = p.sprite.Group()

class mario(p.sprite.Sprite):
    def __init__(self,x,y,dx,dy):
        super().__init__()
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.image = p.surface.Surface((20,20))
        self.rect = self.image.get_rect()
        self.image.fill("GREEN")
        
        self.rect.topleft = [x,y]
    def move(self):
        self.rect.x += self.dx
        if self.rect.x <= 0:
            self.rect.x = 0
            self.dx = -self.dx    
        if self.rect.x >= width-10:
            self.rect.x = width-10
            self.dx = -self.dx    
        self.rect.y += self.dy
        if self.rect.y <= 0:
            self.rect.y = 0
            self.dy = -self.dy    
        if self.rect.y >= 760:
            self.rect.y = 760
            self.dy = -self.dy
    def collider(self):
        if p.sprite.collide_rect(self,rpad):
            self.dx = -self.dx
            rpad.image.fill("RED")

class paddle(p.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = p.surface.Surface((20,150))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]

#build the sprites
for i in range(5):
    dx = r.randint(1,10)
    dy = r.randint(-10,10)
    mar[i] = mario(0,height/2,dx,dy)
    marg.add(mar[i])

#   build the paddle duh
rpad = paddle(500,0)
padg.add(rpad)
p.display.set_caption("Mario Pong")

run = True
while run:
        for i in range (5):
            mar[i].move()
            mar[i].collider()
        screen.fill("BLUE")
        padg.draw(screen)
        marg.draw(screen)
        p.mouse.set_visible(0)
        p.event.get()
        key = p.key.get_pressed()
        if key[p.K_x] and rpad.rect.y <= 768-150:
          rpad.rect.y += 20
        elif key[p.K_w] and rpad.rect.y >=0:
            rpad.rect.y -= 20

        p.display.flip()

