## ###############################################################################
##
## history_wa.py
## ngitung distribusi chattingan el 2003
## by: bibirkubiasasaja
##
###############################################################################

import csv, sys, os
from datetime import datetime
from datetime import date
import matplotlib.pyplot as plt
import numpy as np

      
def openFile(fileName,minDate, maxDate):

  timestamp = []
  daycounter = {}

  #open each data
  f = open(fileName)
  for line in f:
    line = line.strip()
    tokenCount = -1
    for tokens in line.split(" "):
      tokenCount+=1
      if tokenCount == 0: 
        tok1 = tokens
      elif tokenCount == 1:
        tok2 = tokens
      elif tokenCount == 2:
        tok3 = tokens
      elif tokenCount == 3:
        tok4 = tokens      
      else :
        break

    timePerLine= tok1+" "+tok2+" "+tok3+" "+tok4

    try:
      timestamp.append(datetime.strptime(timePerLine,"%b %d, %I:%M %p"))
    except:
      pass


  for date in timestamp:
    dayId = date.weekday()
    #compare and find min and max date
    minDate = min(minDate, date)
    maxDate = max(maxDate, date)
    if dayId in daycounter :
      daycounter[dayId] += 1 
    else:
      daycounter[dayId] = 1 
  
  frequency = []
  for k,v in daycounter.iteritems():
    frequency.append(v)

  #bar plot variable
  wid = .9
  alp = 0.3
  ali = "center"
  title = "Chattingan WA EL 2003 %s - %s" % (minDate.strftime("%b %d"),
                                            maxDate.strftime("%b %d"))
  xlim0 = -0.5
  xlim1 = 4.5

  nameofday = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  ind = np.arange(7)
  bar_width = 0.5
  opacity = 0.7


  #plot
  #"""
  plt.figure()
  waplot = plt.bar(ind, frequency, bar_width,
                   alpha=opacity,
                   color='b')
  plt.xticks(ind,nameofday)
  plt.title(title)
  plt.xlabel('day')
  plt.ylabel('jumlah chat')
  plt.show()
  #"""


def main():
  #put initial value as max value->min and the opposite
  minDate = datetime.strptime(date.max.isoformat(),"%Y-%m-%d")
  maxDate = datetime.strptime(date.min.isoformat(),"%Y-%m-%d")
  fileName = "history_wa.txt"
  openFile(fileName, minDate, maxDate)
      
if __name__ == '__main__':
  main()
