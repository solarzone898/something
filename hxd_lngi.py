import time as tea


def hxd(start,end,sp):
  for i in range(start,end):
    print(hex(i))
    tea.sleep(0.01)
    
    

hxd(0,1000001,0.00001)
