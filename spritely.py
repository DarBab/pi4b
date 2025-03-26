import pygame as p
import time as t
p.init()
tick = p.time.Clock()
width = 1024
height = 768
screen = p.display.set_mode((width,height))
sheet = p.image.load("/home/pi/Downloads/qbert_sheet.png").convert_alpha()
monster = sheet.subsurface(17,32,16,31)
monster = p.transform.scale2x(monster)
bert = sheet.subsurface(0,0,16,16)
bert = p.transform.scale2x(bert)
cube =[0] * 10
b = [0] * 10
cube[0]= sheet.subsurface(0,160,32,32)
cube[0]= p.transform.scale2x(cube[0])
cube[1]= sheet.subsurface(0,192,32,32)
cube[1]= p.transform.scale2x(cube[1])
bert_Group = p.sprite.Group()
block_Group = p.sprite.Group()
monster_Group = p.sprite.Group()

class qbert(p.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (0,0)

class block(p.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect() 
        self.rect.center = (x,y)   

me = qbert(bert)
bert_Group.add(me)
x = 500
y = 200
b[0] = block(cube[0],x,y)
b[1] = block(cube[0],x-32,y+48)
b[2] = block(cube[0],x+32,y+48)
b[3] = block(cube[0],x-64,y+96)
b[4] = block(cube[0],x,y+96)
b[5] = block(cube[0],x+64,y+96)

block_Group.add(b[0],b[1],b[2],b[3],b[4],b[5])

p.display.set_caption("qbert asshole!")
run = True

while run:
        for event  in p.event.get():
            if event.type == p.QUIT:
                run = False
        if p.sprite.collide_mask(b[0],me):
            me.image = monster
            b[4].image = cube[1]
        screen.fill("BLUE")
        mx,my = p.mouse.get_pos()
        me.rect.center = (mx,my)
        block_Group.clear(screen,screen)
        block_Group.draw(screen)
        bert_Group.draw(screen)
        block_Group.update()
        bert_Group.update()
        p.display.update()


