class box:
  def __init__(s,x,y,dx,dy):
    s.x = x
    s.y = y
    s.dx = dx
    s.dy = dy
  def bounce(s):
    s.x += s.dx
    if s.x <= 0:
      s.x = 0
      s.dx = -s.dx
    if s.x >= 500:
      s.x = 500
      s.dx = -s.dx
    s.y += s.dy
    if s.y <= 0:
      s.y = 0
      s.dy =-s.dy
    if s.y >= 500:
      s.y = 500
      s.dy = -s.dy
      
sq = box(100,100,1,2)
while True:
  sq.bounce()
  print(sq.x,sq.y)
