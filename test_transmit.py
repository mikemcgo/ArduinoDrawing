import serial


# Open serial connection
ser = serial.Serial('/dev/cu.usbserial-DN01JC0B')

while True:
	data = input("1 or 0")

	if data == "quit":
		break

	# Encode the data to byte form
	ser.write(data.encode());

