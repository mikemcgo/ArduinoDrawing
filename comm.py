import serial
import time
import pyautogui

# Open serial connection
ser = serial.Serial('/dev/cu.usbserial-DN01JC0B')

while True:
	# Record cursor location every two seconds
	time.sleep(2);
	raw = pyautogui.position();

	# Convert data to a string
	data = str(raw[0]) + "," + str(raw[1]) + ";"

	# Exit if in the top left
	exit = (0,0)

	# Look for exit condition
	if data == exit:
		break;

	# Encode the data to byte form
	ser.write(data.encode());

	# Delay a bit between sending data
	time.sleep(.05)

	# Listen for returning data
	while ser.inWaiting() > 0:
		print(ser.readline());