# Helligkeitsmessung auf Basis des Codes von pageauc (https://www.raspberrypi.org/forums/viewtopic.php?t=112888)

import RPi.GPIO as GPIO
import picamera
import picamera.array
import numpy as np
import time


GPIO.setmode(GPIO.BCM)		# GPIO ueber GPIO-Nummer ansprechen
GPIO.setup(4, GPIO.OUT) 	# wir verwenden Pin Nummer 4

for i in range(12):
# zuerst LEDs ausschalten, um unverfaelschte Werte zu messen
	GPIO.output(4, GPIO.LOW)	# ausschalten

# dann durchschnittliche Helligkeit der Bildpunkte messen
	with picamera.PiCamera() as camera:
	    camera.resolution = (100, 75)
	    with picamera.array.PiRGBArray(camera) as stream:
	        camera.exposure_mode = 'auto'
	        camera.awb_mode = 'auto'
	        camera.capture(stream, format='rgb')
	        pixAverage = int(np.average(stream.array[...,1]))

	if pixAverage < 70:
		GPIO.output(4, GPIO.HIGH)	# anschalten
		print ("Anschalten weil: %i" % pixAverage)
	else:
		print ("aus lassen, weil %i" % pixAverage)


	time.sleep(5)