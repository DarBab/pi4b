import RPi.GPIO as g
from datetime import time as t
import time as t

dp = 18      
lp = 16      
cp = 12       
num = (0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90)
common = (11,13,15,19)    
counter = 0         
            
def setup():
    g.setmode(g.BOARD)     
    g.setup(dp, g.OUT)       
    g.setup(lp, g.OUT)
    g.setup(cp, g.OUT)

    for pin in common:
        g.setup(pin,g.OUT)
        g.output(pin,g.HIGH)

def digit (d):
    g.output(lp,g.HIGH)
    for i in range(8):
        b = (num[d]<<i&128) and g.HIGH
        g.output(dp,b)
        g.output(cp,g.HIGH)
        t.sleep(1)
        g.output(cp,g.LOW)       
    g.output(lp,g.LOW)

if __name__ == '__main__':
    setup()
    while True:
        clk = t.localtime()
        h = divmod(clk.tm_hour,10)
        m = divmod(clk.tm_min,10)
        digit(h[0])
        g.output(common[0],0)
        t.sleep(1)
        g.output(common[1],0)
        digit(h[1])
        g.output(common[1],0)
        t.sleep(1)
        digit(m[0])
        g.output(common[2],0)
        t.sleep(1)
        digit(m[1])
        g.output(common[3],0)
        t.sleep(1)