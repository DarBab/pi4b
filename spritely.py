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

for i in range(8):
  monsters[i] = p.transform.scale2x(sheet.subsurface(i*16,32,16,32))
  bert[i] = p.transform.scale2x(sheet.subsurface(i*16,0,16,16))

for cl in range(3):
  tc = 160+(cl*32)   
  cube[cl]= sheet.subsurface(0,tc,32,32)
  cube[cl]= p.transform.scale2x(cube[cl])

bert_Group = p.sprite.Group()
block_Group = p.sprite.Group()
monster_Group = p.sprite.Group()

class qbert(p.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (50,17)
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

me = qbert(bert[0])
m1 = monster(monsters[0],214,586)
m2 = monster(monsters[2],790,586)
bert_Group.add(me)
monster_Group.add(m1,m2)
n = 0

for i in range(10):
  dx=-(32*i)
  dy=48*i
  x=dx+500
  y=200+dy
  for j in range(i+1):
    b[n] = block(cube[0],x,y)
    x+=64
    block_Group.add(b[n])
    n+=1
   
p.display.set_caption("Bab bert")
run = True
while run:
  for event  in p.event.get():
    if event.type == p.QUIT:
      run = False
  screen.fill("BLUE")
  for ty in range(55):     
    if p.sprite.spritecollide(b[ty],bert_Group,0,p.sprite.collide_rect_ratio(.5)):
      b[ty].image = cube[1]

  mx,my = p.mouse.get_pos()
#  print(mx,my)
  me.rect.center = (mx,my)
  block_Group.draw(screen)
  bert_Group.draw(screen)
  monster_Group.draw(screen)
  block_Group.update()
  bert_Group.update()
  monster_Group.update()
  p.display.update()
  c = clock.tick(60)
  tc = c+10
  me.rot()


