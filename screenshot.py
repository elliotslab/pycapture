from PIL import ImageGrab
import datetime
import os
import time

# ask for delay between screenshots
print 'How many seconds do you want between screenshots?'
seconds = int(input())
print 'In wich extension you would like to save the screenshots?'
print '1) PNG\n2) JPEG\n' 
fileExtension = input()

if fileExtension == 1:
    extension = '.png'
else:
    extension = '.jpg'


# get date and time
currentTime = time.time()
currentDate = datetime.datetime.fromtimestamp(currentTime).strftime('%Y-%m-%d %H-%M-%S')

def screen_grab():
    im = ImageGrab.grab()
    fileName = str(currentDate) + ".png"
    im.save(fileName)

def find_oldest_file(dirname,extension):
    oldest_file, oldest_time = None, None
    for dirpath, dirs, files in os.walk(dirname):
        for filename in files:
            file_path = os.path.join(dirpath, filename)
            file_time os.stat(file_path.st_mtime
            if file_path.endswith(extension) and (file_time<oldest_time or oldest_time is None):
                oldest_file, oldest_time = file_path, file_time
    return oldest_file


