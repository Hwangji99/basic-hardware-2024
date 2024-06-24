import RPi.GPIO as GPIO
import time

steps = [21, 22, 23, 24]
GPIO.setmode(GPIO.BCM)

for stepPin in steps:
  GPIO.setup(stepPin, GPIO.OUT)
  GPIO.output(stepPin, 0)

try:
  while 1:
    GPIO.output(stepPin[0], 0)
    GPIO.output(stepPin[1], 0)
    GPIO.output(stepPin[2], 0)
    GPIO.output(stepPin[3], 1)

    GPIO.output(stepPin[0], 0)
    GPIO.output(stepPin[1], 0)
    GPIO.output(stepPin[2], 1)
    GPIO.output(stepPin[3], 0)

    GPIO.output(stepPin[0], 0)
    GPIO.output(stepPin[1], 1)
    GPIO.output(stepPin[2], 0)
    GPIO.output(stepPin[3], 0)

    GPIO.output(stepPin[0], 1)
    GPIO.output(stepPin[1], 0)
    GPIO.output(stepPin[2], 0)
    GPIO.output(stepPin[3], 0)



except KeyboardInterrupt:
  GPIO.cleanup()
    
