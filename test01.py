import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
import os
import glob

GPIO.setwarnings(True)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(7, GPIO.HIGH)
GPIO.output(5, GPIO.HIGH)

#for cam in glob.glob('/dev/video*') :
for cam in ['/dev/video0', '/dev/video2'] :
    #print(cam)
    nom_cam = cam.split('/')[2]
    commande = f'ffmpeg -f video4linux2 -i {cam} -vframes 1  -video_size 640x480 /var/www/html/test_{nom_cam}.jpeg'
    print(commande)
    os.system(commande)

GPIO.output(7, GPIO.LOW)
GPIO.output(5, GPIO.LOW)
