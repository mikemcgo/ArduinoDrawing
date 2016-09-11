import serial
import time

# Open serial connection
ser = serial.Serial('/dev/cu.usbserial-DN01JC0B')

while True:
	# Retrieve data to send via usb (only numbers, separated by , or ;)
	data = input("Data to transmit: ");

	# Look for exit condition
	if data == 'quit':
		break;

	# Encode the data to byte form
	ser.write(data.encode());

	# Delay a bit between sending data
	time.sleep(.05)

	# Listen for returning data
	while ser.inWaiting() > 0:
		print(ser.readline());