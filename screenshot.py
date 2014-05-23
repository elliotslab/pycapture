from PIL import ImageGrab
import datetime
import time

# ask for delay between screenshots
print 'How many seconds do you want between screenshots?'
seconds = int(input())

# get date and time
currentTime = time.time()
currentDate = datetime.datetime.fromtimestamp(currentTime).strftime('%Y-%m-%d %H-%M-%S')

