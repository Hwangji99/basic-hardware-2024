import RPi.GPIO as GPIO
import time

relayPin = 25      # Spin에 연결
GPIO.setmode(BCM)
GPIO.setup(relayPin, GPIO.OUT)

try:
  GPIO.output (relayPin, 1)

except KeyboardInterrupt:
  GPIO.cleanup()
