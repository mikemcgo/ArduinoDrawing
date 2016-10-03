import serial
import scipy
from scipy import *
import scipy.ndimage


# Open serial connection
ser = serial.Serial('/dev/cu.usbserial-DN01JC0B')
img = scipy.ndimage.imread('diag.png', flatten=True)

count = 0

for y in range(len(img)):
	for x in range(len(img[0])):
		if img[y][x] == 0:
			data = str(x) + "," + str(y) + ";"

			# Encode the data to byte form
			ser.write(data.encode());

			count +=1
print(count)


