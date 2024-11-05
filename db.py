import RPi.GPIO as g
import time

dp   = 18      
lp  = 16      
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

if __name__ == '__main__':
        setup()
        for n in num:                                   #get the digit
            for i in range(8):
                b = ((n<<i&128) and g.HIGH)
                g.output(dp,b)
                g.output(cp,g.HIGH)
                time.sleep(1)
                g.output(cp,g.LOW)
            g.output(lp,g.LOW)
        g.output(lp,g.HIGH)
        g.output(11,g.LOW)
                






