Logitech sphere control from Python
Install the following:
```sh
sudo apt-get install v4l-utils
sudo apt-get install guvcview
sudo apt-get install uvcdynctrl
```

Start guvcview to load control options:
```sh
sudo guvcview -d /dev/video1 -g none
```

(From commandline: `uvcdynctrl -d /dev/video1 -s "Pan (relative)" 1000`)

Now call from Python:
```python
os.system(uvcdynctrl -d /dev/video1 -s "Pan (relative)" 1000)
```
or tilt or other functions.
