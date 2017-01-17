# ArduinoDrawing

This project contains the python code for a project that enabled an arduino touchscreen to act as a drawing tablet.

The touchscreen is meant to sit under a piece of paper, upon which the user draws. The touchscreen then relays the coordinates of pencil to an arduino, which then relays it to a 'server' running this python code.

The server is loaded on start with an image that the user would like to draw, and if the server detects the user's pencil lies outside the black in the desired image, it will signal the arduino to light leds which vary on how long the user's pencil has been outside the allowable drawing space of the image.
