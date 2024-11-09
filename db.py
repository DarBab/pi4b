import time as t

hr = (t.localtime().tm_hour)    #I hope this works
min = (t.localtime().tm_min)
sm = divmod(min,10) #            new i could find it.
sh = divmod(hr,10)
print (f"hour is {sh}")
print(f"minute is {sm}")


  
