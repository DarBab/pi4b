x=500
y=200
for i in range(10):
  dx=-(32*i)
  dy=48*i
  tx=dx+x
  y=200+dy
  print()
  for j in range(i+1):
    print(tx,y)
    tx+=64
  
  