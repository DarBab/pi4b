import pygame as p
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
  bert[i] = p.transform.scale2x(sheet.subsurface(i*16,0,16,16))
for j in range(8):
  monsters[j] = p.transform.scale2x(sheet.subsurface(j*16,128,16,16))
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
        self.rect.bottomleft = (x,y)
    def move(self,x,y,char,gr):
        tx = self.rect.x
        ty = self.rect.y
        print(tx,ty)
        self.rect.x+=x
        self.rect.y+=y
        self.image = char
        col = p.sprite.spritecollide(self,gr,0,p.sprite.collide_circle_ratio(.5))
        if col:
          col[0].image = cube[1]
        else:
          self.rect.x = tx
          self.rect.y = ty
          return 5

        
me = qbert(bert[1],516,162)
m1 = qbert(monsters[4],228,590)
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
        me.move(32,48,bert[5],block_Group)
      if event.key == p.K_n:
        m1.move(32,48,monsters[0],block_Group)
      if event.key == p.K_z:
        me.move(-32,48,bert[7],block_Group)
      if event.key == p.K_q:
        me.move(-32,-48,bert[3],block_Group)
      if event.key == p.K_e:
        me.move(32,-48,bert[1],block_Group)
      if event.key == p.K_y:
        m1.move(32,-48,monsters[0],bert_Group)
      if event.key == p.K_f:
        run = False

  mx,my = p.mouse.get_pos()
#  print(mx,my)
  screen.fill("cyan")
  block_Group.draw(screen)
  bert_Group.draw(screen)
  monster_Group.draw(screen)
  block_Group.update()
  bert_Group.update()
  monster_Group.update()

  p.display.update()
