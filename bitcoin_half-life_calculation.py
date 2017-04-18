from datetime import datetime
from datetime import timedelta

start = datetime(2009, 1, 3, 18, 15, 5)

totalcoin = 21000000*100000000

miningspeed = 50*100000000

halfing = 0


remainingtotal = totalcoin

while not miningspeed < 2:

    if remainingtotal >= 0.5 * totalcoin:
        remainingtotal = remainingtotal - miningspeed
        start += timedelta(minutes = 10) 
    else:
        totalcoin = 0.5* totalcoin
        miningspeed = miningspeed * 0.5
        halfing += 1
        
        
  
print("number of halfing: "+ str(halfing))
print("total coin mined: "+ str((21000000*100000000 - remainingtotal)/100000000))
print("ending time: " + str(start))
