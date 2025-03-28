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
cube =[0] * 20
b = [0] * 20
cube[2]= sheet.subsurface(0,160,32,32)
cube[2]= p.transform.scale2x(cube[2])
cube[1]= sheet.subsurface(0,192,32,32)
cube[1]= p.transform.scale2x(cube[1])
cube[0]= sheet.subsurface(0,224,32,32)
cube[0]= p.transform.scale2x(cube[0])
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

b[1] = block(cube[0],x-32,200+48)
b[2] = block(cube[0],x+32,200+48)

b[3] = block(cube[0],x-64,200+96)
b[4] = block(cube[0],x,200+96)
b[5] = block(cube[0],x+64,200+96)

b[6] = block(cube[0],x-96,200+144)
b[7] = block(cube[0],x-32,200+144)
b[8] = block(cube[0],x+32,200+144)
b[9] = block(cube[0],x+96,200+144)

b[10] = block(cube[0],x-128,200+192)
b[11] = block(cube[0],x-64,200+192)
b[12] = block(cube[0],x,200+192)
b[13] = block(cube[0],x+64,200+192)
b[14] = block(cube[0],x+128,200+192)
for i in range(15):
    block_Group.add(b[i])

p.display.set_caption("Bab bert")
run = True
while run:
        for event  in p.event.get():
            if event.type == p.QUIT:
                run = False
        if p.sprite.collide_mask(b[0],me):
            b[9].image = cube[2]
        screen.fill("BLUE")
        mx,my = p.mouse.get_pos()
        print(mx,my)
        me.rect.center = (500,170)
        block_Group.clear(screen,screen)
        block_Group.draw(screen)
        bert_Group.draw(screen)
        block_Group.update()
        bert_Group.update()
        p.display.update()


