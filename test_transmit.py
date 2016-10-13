import serial
import re


# Open serial connection
ser = serial.Serial('/dev/cu.usbserial-DN01JC0B')

while True:
	while ser.inWaiting() > 0:
		val = ser.readline()
		non_decimal = re.compile(r'[^\d.]+')
		value = non_decimal.sub('', str(val))
		print(value)
		# if int(value) >= 400:
		# 	ser.write('1'.encode())
		# else:
		# 	ser.write('0'.encode())
	# data = input("1 or 0")

	# if data == "quit":
	# 	break

	# # Encode the data to byte form
	# ser.write(data.encode());

