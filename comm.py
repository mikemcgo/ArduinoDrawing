import serial
import scipy
from scipy import *
import scipy.ndimage
import re

def scale(value, old, new):
	return int((value / old) * new)

# WHITE IS 255

# Open serial connection
ser = serial.Serial('/dev/cu.usbserial-DN01JC0B')
img = scipy.ndimage.imread('fountain-01.png', flatten=True)
non_decimal = re.compile(r'[^\d.]+')

while True:
	while(ser.inWaiting() > 0):
		try:
			incoming = str(ser.readline())
			incoming = incoming.split(",")
			raw_x = re.sub("[^0-9]", "", incoming[0])
			x = scale(int(raw_x), 4000, len(img[0]))
			raw_y = re.sub("[^0-9]", "", incoming[1])
			y = scale(int(raw_y), 4000, len(img))
			print(str(x) + " " + str(y))
			print(img[y][x])
			if img[y][x] == int(0.0):
				print('1')
				ser.write('1'.encode())
			else:
				print('0')
				ser.write('0'.encode())
		except IndexError:
			print('nope')
