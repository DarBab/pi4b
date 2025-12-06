import pygame as p
import random as r
p.init()
clock = p.time.Clock()
width = 1024
height = 768
screen = p.display.set_mode((width,height))
sheet = p.image.load("/home/pi/bert/qbert_sheet.png")
swear = p.transform.scale2x(sheet.subsurface(128,83,48,25))
cube = [0] * 60
b = [0] * 60
monsters = [0] * 10
monster_x = [-32,32]
monster_y = [-48,48]
bert = [0] * 10
player = [0] * 8
banner = [0] * 8
global pl
global run,score
global monJump
pl = 0
n = 0
run = True
bert_Group = p.sprite.Group()
block_Group = p.sprite.Group()
monster_Group = p.sprite.Group()
MJ = p.USEREVENT+1
MJ2 = p.USEREVENT+2
BAN = p.USEREVENT+3
p.time.set_timer(MJ,1000)
p.time.set_timer(MJ2,1000)
p.time.set_timer(BAN,200)

class qbert(p.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = image
        self.mask = p.mask.from_surface(image)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x,y)
        pl = 0
    def bert_Move(self,x,y,char):
        self.rect.x+=x
        self.rect.y+=y
        self.image = char
        col = p.sprite.spritecollide(self,block_Group,0,p.sprite.collide_circle_ratio(.5))
        if col:
          col[0].image = cube[2]
          tunage()
        else:
          self.image = swear
          render()
        mhit = p.sprite.spritecollide(self,monster_Group,0,p.sprite.collide_mask)    
        if mhit:
          print('game over asshole')
          me.image = swear
          render()
    def mon_Move(self,x,y,char):
        self.image = char
        tx = self.rect.x
        ty = self.rect.y
        self.rect.x+=x
        self.rect.y+=y        
        col = (p.sprite.spritecollide(self,block_Group,0,p.sprite.collide_mask))
        if col:
          pass
        else:
          self.rect.x = tx
          self.rect.y = ty
          jump(self) 
          
for i in range(8):#bert
  bert[i] = p.transform.scale2x(sheet.subsurface(i*16,0,16,16))
for j in range(8):#monsters
  monsters[j] = p.transform.scale2x(sheet.subsurface(j*16,16,16,16))
for i in range(5):#blocks
  cube[i]= sheet.subsurface(0,160+(i*32),32,32)
  cube[i]= p.transform.scale2x(cube[i])
for j in range(8):#player banner
  player[j] = p.transform.scale2x(sheet.subsurface(128,j*8+112,52,8))
for i in range(10):# set up pyramid
  x=-(32*i)+500
  y=200+48*i
  for j in range(i+1):
    b[n] = qbert(cube[1],x,y)
    x+=64
    block_Group.add(b[n])
    n+=1
     
me = qbert(bert[1],518,155)
m1 = qbert(monsters[0],226,592)
m2 = qbert(monsters[2],810,592)

bert_Group.add(me)
monster_Group.add(m1,m2)
p.display.set_caption("QBERT FOR LOSERS")

def tunage():
  p.mixer.music.load("/home/pi/bert/jump.mp3")
  p.mixer.music.play()
def render():
  screen.fill("grey")
  block_Group.update()
  bert_Group.update()
  monster_Group.update()
  block_Group.draw(screen)
  bert_Group.draw(screen)
  monster_Group.draw(screen)
  screen.blit(player[pl],(32,32))            
  p.display.update()
def jump(char):
      tx = r.randint(0,1)
      ty = r.randint(0,1)
      char.mon_Move(monster_x[tx],monster_y[ty],char.image)
def scre():          
  score = 0
  for i in range(50):
    if b[i].image == cube[2]:
      score += 25
    print(score)
    if score == 1250:
      return 5
def banner_scroll():
    global pl
    pl+=1
    if pl > 5:
      pl=0

while run == True:
  clock.tick(60)
  mx,my = p.mouse.get_pos()
  
  for event in p.event.get():
    if event.type == MJ:
      jump(m1)
    if event.type == MJ2:
      jump(m2)
    if event.type == BAN:
      banner_scroll()
    if event.type == p.KEYDOWN:
      if event.key == p.K_c:
        me.bert_Move(32,48,bert[5])
      if event.key == p.K_n:
        m1.bert_Move(32,48,monsters[0])
      if event.key == p.K_z:
        me.bert_Move(-32,48,bert[7])
      if event.key == p.K_q:
        me.bert_Move(-32,-48,bert[3])
      if event.key == p.K_e:
        me.bert_Move(32,-48,bert[1])
      if event.key == p.K_y:
        if m1.mon_Move(32,-48,monsters[1]):
          tunage()
      if event.key == p.K_f:
        run = False
#  if scre():
#    me.image = swear
#    p.time.delay(3000)
#    run = False

  render()
