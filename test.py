from phue import Bridge
import time as t
b=Bridge('192.168.50.123')
lights=('Left','Center','Right')
col = [255,65535,0]

b.connect()
for p in range(3):
    for l in lights:
        b.set_light(l,'on',True)
        b.set_light(l,'hue',col[p])
        print(p,col[p])
        t.sleep(2)
        b.set_light(l,'on',False)




