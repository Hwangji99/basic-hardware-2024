import RPi.GPIO as GPIO
import time

led = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

try:
  while True:
    a = input()
    if a == '0':
      GPIO.output(led, False)
      
except KeyboardInterrupt:
  GPIO.cleanup()    
