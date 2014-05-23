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

directory = os.getenv('APPDATA') + '//screencaptures'

try:
    os.chdir(directory)
except:
    os.mkdir(directory)
    os.chdir(directory)


# get date and time
currentTime = time.time()
currentDate = datetime.datetime.fromtimestamp(currentTime).strftime('%Y-%m-%d %H-%M-%S')

def screen_grab():
    im = ImageGrab.grab()
    fileName = str(currentDate) + extension 
    im.save(fileName)

def find_oldest_file(dirname,ext):
    oldest_file, oldest_time = None, None
    for dirpath, dirs, files in os.walk(dirname):
        for filename in files:
            file_path = os.path.join(dirpath, filename)
            file_time = os.stat(file_path).st_mtime
            if file_path.endswith(extension) and (file_time<oldest_time or oldest_time is None):
                oldest_file, oldest_time = file_path, file_time
    return oldest_file

def count_files(path,ext):
    list_dir = []
    list_dir = os.listdir(path)
    count = 0
    for file in list_dir:
        if file.endswith(ext):
            count += 1
    return count

def delete_files():
        files = count_files(directory, extension)
        if files >= 40:
            os.unlink(str(find_oldest_file(directory,extension)))

while True:
    currentTime = time.time()
    currentDate = datetime.datetime.fromtimestamp(currentTime).strftime('%Y-%m-%d %H-%M-%S')
    screen_grab()
    time.sleep(seconds)
    delete_files()
