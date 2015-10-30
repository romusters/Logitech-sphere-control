Logitech sphere control from Python<br />
<br />
Install the following:<br\>
sudo apt-get install v4l-utils<br />
sudo apt-get install guvcview<br />
sudo apt-get install uvcdynctrl<br />
<br />
Start guvcview to load control options:<br />
sudo guvcview -d /dev/video1 -g none<br />
<br />
(From commandline: uvcdynctrl -d /dev/video1 -s "Pan (relative)" 1000))<br />
<br />
Now call from Python:<br />
os.system(uvcdynctrl -d /dev/video1 -s "Pan (relative)" 1000)<br />
or tilt or other functions.
