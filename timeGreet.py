from datetime import datetime
import pytz

# Get the current time
current_time = datetime.now()

# Choose the Indian Standard Time (IST) timezone
ist_timezone = pytz.timezone('Asia/Kolkata')

# Localize the current time to UTC
utc_time = pytz.utc.localize(current_time)

# Convert UTC time to IST
ist_time = utc_time.astimezone(ist_timezone)

# Extract and format the time part only
ist_time_str = ist_time.strftime('%H:%M:%S')

# Print the time in IST
print("Current time in IST:", ist_time_str)

Inttime = int(ist_time.strftime('%H'))

name = input('Enter your name: ')
c= name.capitalize()
if(4<=Inttime<12):
    print('Good Morning',c+',','it\'s',ist_time_str)
elif(12<=Inttime<19):
    print('Good Evening',c+',','it\'s',ist_time_str)
else:
    print('Good Night',c+',','it\'s',ist_time_str)