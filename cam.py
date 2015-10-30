import os

#os.system('sudo guvcview -d /dev/video1 -g none')
while True:
	os.system('uvcdynctrl -d /dev/video1 -s "Pan (relative)" 20')


