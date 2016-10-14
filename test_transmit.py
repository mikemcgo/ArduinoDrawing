import serial
import scipy
from scipy import *
import scipy.ndimage
import re

# Open serial connection
ser = serial.Serial('/dev/cu.usbserial-DN01JC0B')
img = scipy.ndimage.imread('half.png', flatten=True)
non_decimal = re.compile(r'[^\d.]+')

print(img[0][0])

while True:
	while(ser.inWaiting() > 0):
		try:
			incoming = str(ser.readline())
			incoming = incoming.split(",")
			x = re.sub("[^0-9]", "", incoming[0])
			y = re.sub("[^0-9]", "", incoming[1])
			z = int(x)
			print(len(x))
		except:
			print('nope')