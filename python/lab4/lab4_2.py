# Import time to use time specific functions
import time

epoch = time.time()
print('There have been',epoch,
      'seconds since the start of the Epoch')

ctime = time.ctime()
print('Or to put it another way, the date and time is',
      ctime)

# We can get an ISO 8601 formatted date time
# (there's an easier way in the datetime module)
isodate = time.strftime('%Y-%m-%d %H:%M:%S')
print('ISO date time is', isodate)
# See https://xkcd.com/1179/ for more details

# We can do some other interesting stuff
for x in range(0,10):
    print('.', end='')
    time.sleep(1)

