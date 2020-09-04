#!/usr/bin/env python3

import sys
import datetime

"""
Standard input:
30 1 /bin/run_me_daily
45 * /bin/run_me_hourly
* * /bin/run_me_every_minute
* 19 /bin/run_me_sixty_times

ouput:
1:30 tomorrow - /bin/run_me_daily
16:45 today - /bin/run_me_hourly
16:10 today - /bin/run_me_every_minute
19:00 today - /bin/run_me_sixty_times

Execute:
./application.py 16:10 < config
"""

time1 = sys.argv[1]


def compare_time(t1,t2):
    time1 = datetime.datetime.strptime(t1, "%H:%M")
    time2 = datetime.datetime.strptime(t2, "%H:%M")
    
    if (time1 > time2):
      return 1
    elif (time1 < time2):
      return -1
    else:
      return 0 

output = ""
for line in sys.stdin:
  strs = line.split(" ")
  time2 = time1
  if (strs[0] == "*"):
    if (strs[1] == "*"):
      time2 = time1
    else:
      time2 = strs[1] + ":" + "00"
  elif (strs[0] != "*" and strs[1] == "*"):
    time2 = time1.split(":")[0] + ":" + strs[0]
    if (compare_time(time1, time2) > 0):
      time2 = (datetime.datetime.strptime(time2, "%H:%M") + datetime.timedelta(hours=1)).strftime("%H:%M")
  else:
    time2 = strs[1] + ":" + strs[0]

  command = strs[2]
 
  if (compare_time(time1, time2) <= 0):
    output = output + time2 + " today - " + command
  else:
    output = output + time2 + " tomorrow - " + command

print(output)
