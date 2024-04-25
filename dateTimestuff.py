from datetime import datetime 
import pytz

currentDT= datetime.now()
print("Current UTC DateTime is", currentDT)
utcTime = currentDT.strftime('%H:%M:%S')
print("Current UTC time is",utcTime)
istDT= currentDT.astimezone(pytz.timezone('Asia/Kolkata'))
print("Current IST DateTime is",istDT)
istTime= istDT.strftime('%H:%M:%S')
print("Current IST DateTime is",istTime)
istHour1= int(istTime.split(':')[0])
# print(istHour1)
istHour2= int(istDT.strftime('%H'))
# print(istHour2)

if(6<=istHour2<12):
  print("Good Morning, the time is", istTime)
elif(12<istHour2<19):
  print("Good Evening, the time is", istTime)
else:
  print("Good Night, the time is", istTime)
  