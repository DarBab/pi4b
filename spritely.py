import pygame as p
import random as r
p.init()
clock = p.time.Clock()
width = 1024
height = 768
screen = p.display.set_mode((width,height))
sheet = p.image.load("/home/pi/Downloads/qbert_sheet.png").convert_alpha()
swear = p.transform.scale2x(sheet.subsurface(128,83,48,25))
cube = [0] * 60
b = [0] * 60
monsters = [0] * 10
monster_x = [-32,32]
monster_y = [-48,48]
bert = [0] * 10
n = 0
run = True
for i in range(8):
  monsters[i] = p.transform.scale2x(sheet.subsurface(i*16,32,16,32))
  bert[i] = p.transform.scale2x(sheet.subsurface(i*16,0,16,16))

for i in range(3):
  cube[i]= sheet.subsurface(0,160+(i*32),32,32)
  cube[i]= p.transform.scale2x(cube[i])

bert_Group = p.sprite.Group()
block_Group = p.sprite.Group()
monster_Group = p.sprite.Group()

class qbert(p.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def move(self,x,y,char):
        self.rect.x+=x
        self.rect.y+=y
        self.image = char
    def mmove(self,char):
        self.rect.x+=x
        self.rect.y+=y
        self.image = char
    def qcheck(self,gr): 
        col = p.sprite.spritecollide(self,gr,0,p.sprite.collide_circle_ratio(.5))
        if col:
           col[0].image = cube[1] 
        else:
            return 1
    def mcheck(self,gr): 
        col = p.sprite.spritecollide(self,gr,0,p.sprite.collide_circle_ratio(.5))
        if col:
           return 1
        else:
            return 2
me = qbert(bert[1],500,170)
m1 = qbert(monsters[0],214,586)
m2 = qbert(monsters[2],790,586)
bert_Group.add(me)
monster_Group.add(m1,m2)

for i in range(10):
  x=-(32*i)+500
  y=200+48*i
  for j in range(i+1):
    b[n] = qbert(cube[2],x,y)
    x+=64
    block_Group.add(b[n])
    n+=1



p.display.set_caption("Bab bert")
while run == True:
  clock.tick(60)
  for event in p.event.get():
    if event.type == p.KEYDOWN:
      if event.key == p.K_c:
        me.move(32,48,bert[5])
      if event.key == p.K_z:
        me.move(-32,48,bert[7])
      if event.key == p.K_q:
        me.move(-32,-48,bert[3])
      if event.key == p.K_e:
        me.move(32,-48,bert[1])
      if event.key == p.K_f:
        run = False
  screen.fill("cyan")
    
  block_Group.draw(screen)
  bert_Group.draw(screen)
  monster_Group.draw(screen)
  block_Group.update()
  bert_Group.update()
  monster_Group.update()
  me.qcheck(block_Group)
  p.display.update()
  if m1.mcheck(bert_Group) == 1:
    me.image = swear
    run = False
  if m2.mcheck(bert_Group) == 1:
    me.image = swear
    run = False
  if m2.mcheck(block_Group) == 2:
    print('this')
