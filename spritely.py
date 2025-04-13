import pygame as p
p.init()
clock = p.time.Clock()
width = 1024
height = 768
screen = p.display.set_mode((width,height))
sheet = p.image.load("/home/pi/Downloads/qbert_sheet.png").convert_alpha()
cube = [0] * 200
b = [0] * 60
monsters = [0] * 10
bert = [0] * 10
n = 0
#sprites from sheet
for i in range(8):
  monsters[i] = p.transform.scale2x(sheet.subsurface(i*16,32,16,32))
  bert[i] = p.transform.scale2x(sheet.subsurface(i*16,0,16,16))
#blocks from sheet
for i in range(3):
  cube[i]= sheet.subsurface(0,160+(i*32),32,32)
  cube[i]= p.transform.scale2x(cube[i])
#different groups
bert_Group = p.sprite.Group()
block_Group = p.sprite.Group()
monster_Group = p.sprite.Group()

class qbert(p.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (500,170)
    def rot(self):
#        print(c,tc)
        me.image = bert[1]
class block(p.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect() 
        self.rect.center = (x,y) 
class monster(p.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect() 
        self.rect.center = (x,y)   

me = qbert(bert[1])
m1 = monster(monsters[0],214,586)
m2 = monster(monsters[2],790,586)
bert_Group.add(me)
monster_Group.add(m1,m2)

for i in range(10):
  x=-(32*i)+500
  y=200+48*i
  for j in range(i+1):
    b[n] = block(cube[2],x,y)
    x+=64
    block_Group.add(b[n])
    n+=1
   
p.display.set_caption("Bab bert")
run = True
while run:
  for event in p.event.get():
    if event.type == p.KEYDOWN:
      if event.key == p.K_c:
        me.rect.x+=32
        me.rect.y+=48
      if event.key == p.K_z:
        me.rect.x-=32
        me.rect.y+=48
      if event.key == p.K_q:
        me.rect.x-=32
        me.rect.y-=48
      if event.key == p.K_e:
        me.rect.x+=32
        me.rect.y-=48
      if event.key == p.K_f:
        run = False

  screen.fill("BLUE")
#  qb colliding with blocks
  for i in range(55):     
    if p.sprite.spritecollide(b[i],bert_Group,0,p.sprite.collide_circle_ratio(.5)):
      b[i].image = cube[1]

  mx,my = p.mouse.get_pos()
#  print(mx,my)
#  me.rect.center = (mx,my)
  block_Group.draw(screen)
  bert_Group.draw(screen)
  monster_Group.draw(screen)
  block_Group.update()
  bert_Group.update()
  monster_Group.update()
  p.display.update()


