import pygame as p
import random as r
p.init()
clock = p.time.Clock()
width = 1024
height = 768
screen = p.display.set_mode((width,height))
sheet = p.image.load("/home/pi/bert/qbert_sheet.png").convert_alpha()
swear = p.transform.scale2x(sheet.subsurface(128,83,48,25))
cube = [0] * 60
b = [0] * 60
monsters = [0] * 10
monster_x = [-32,32]
monster_y = [-48,48]
bert = [0] * 10
player = [0] * 8
banner = [0] * 8
global pl,banner_Time
global run,score
pl = 0
n = 0
run = True
bert_Group = p.sprite.Group()
block_Group = p.sprite.Group()
monster_Group = p.sprite.Group()

class qbert(p.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = image
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
          render()
          tunage()
        else:
          self.image = swear
          render()
          return 1    
    def mon_Move(self,x,y,char):
        self.image = char
        tx = self.rect.x
        ty = self.rect.y
        self.rect.x+=x
        self.rect.y+=y
        col = p.sprite.spritecollide(self,block_Group,0,p.sprite.collide_circle_ratio(.5))
        if col:
          pass          
        else:
          self.rect.x = tx
          self.rect.y = ty

for i in range(8):#bert
  bert[i] = p.transform.scale2x(sheet.subsurface(i*16,0,16,16))
for j in range(8):#monsters
  monsters[j] = p.transform.scale2x(sheet.subsurface(j*16,16,16,16))
for i in range(3):#blocks
  cube[i]= sheet.subsurface(0,160+(i*32),32,32)
  cube[i]= p.transform.scale2x(cube[i])
for j in range(8):#player banner
  player[j] = p.transform.scale2x(sheet.subsurface(128,j*8+112,52,8))
for i in range(10):#set up blocks
  x=-(32*i)+500
  y=200+48*i
  for j in range(i+1):
    b[n] = qbert(cube[1],x,y)
    x+=64
    block_Group.add(b[n])
    n+=1
     
me = qbert(bert[1],518,155)
m1 = qbert(monsters[1],228,590)
m2 = qbert(monsters[1],810,590)

bert_Group.add(me)
monster_Group.add(m1,m2)
p.display.set_caption("baburt")
banner_Time = p.time.get_ticks() + 50

def tunage():
  p.mixer.music.load("/home/pi/bert/jump.mp3")
  p.mixer.music.play()
def render():
  screen.fill("black")
  block_Group.update()
  bert_Group.update()
  monster_Group.update()
  block_Group.draw(screen)
  bert_Group.draw(screen)
  monster_Group.draw(screen)
  p.draw.rect(screen,0,m1.rect,1)
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
    if score > 75:
      return 5
def banner_scroll():
    global banner_Time
    if banner_Time - p.time.get_ticks() > 0:
      pass
    else:
      global pl
      pl+=1 
      if pl > 5:
        pl = 0  
      banner_Time = p.time.get_ticks() + 50

while run == True:
  clock.tick(60)
  mx,my = p.mouse.get_pos()
#  print(mx,my)
  
  for event in p.event.get():
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
#  jump(m1,block_Group)
#  jump(m2,block_Group)
  banner_scroll()
  if scre() == 5:
    run = False
  jump(m1)
  jump(m2)
  render()
