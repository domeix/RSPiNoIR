import picamera
import picamera.array
import numpy as np
with picamera.PiCamera() as camera:
    camera.resolution = (100, 75)
    with picamera.array.PiRGBArray(camera) as stream:
        camera.exposure_mode = 'auto'
        camera.awb_mode = 'auto'
        camera.capture(stream, format='rgb')
        pixAverage = int(np.average(stream.array[...,1]))
print ("Light Meter pixAverage=%i" % pixAverage)