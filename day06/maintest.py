from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import RPi.GPIO as GPIO
import time

def measure():
	GPIO.output(trigPin, True)
	time.sleep(0.00001)
	GPIO.output(trigPin, False)
	start = time.time()

	while GPIO.input(echoPin) == False:
		start = time.time()
	while GPIO.input(echoPin) == True:
		stop = time.time()
	elapsed = stop - start
	distance = (elapsed * 19000) / 2

	return distance

leds = [26, 19, 13]
piezoPin = 6
trigPin = 27
echoPin = 17

segments = (20, 21, 16, 12, 24, 25, 5)

digits = (23, 18, 4, 22)

num = [
	(1, 1, 1, 1, 1, 1, 0),
	(0, 1, 1, 0, 0, 0, 0),
	(1, 1, 0, 1, 1, 0, 1),
	(1, 1, 1, 1, 0, 0, 1),
	(0, 1, 1, 0, 0, 1, 1),
	(1, 0, 1, 1, 0, 1, 1),
	(1, 0, 1, 1, 1, 1, 1),
	(1, 1, 1, 0, 0, 0 ,0),
	(1, 1, 1, 1, 1, 1, 1),
	(1, 1, 1, 1, 0, 1, 1)
] 

GPIO.setmode(GPIO.BCM)
for led in leds:
	GPIO.setup(led, GPIO.OUT)
	GPIO.output(led, 0)

GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

for segment in segments:
	GPIO.setup(segment, GPIO.OUT)
	GPIO.output(segment, GPIO.LOW)

for digit in digits:
	GPIO.setup(digit, GPIO.OUT)
	GPIO.output(digit, GPIO.HIGH)

form_class = uic.loadUiType("./main.ui")[0]

class WindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.btnred.clicked.connect(self.btnredFunction)
		self.btnblue.clicked.connect(self.btnblueFunction)
		self.btngreen.clicked.connect(self.btngreenFunction)
		self.led_off.clicked.connect(self.ledoffFunction)
		self.btn_ultra.clicked.connect(self.ultraFunction)
		self.btn_fnd.clicked.connect(self.fndFunction)

	def btnredFunction(self):
		GPIO.output(leds[0], False)
		GPIO.output(leds[1], True)
		GPIO.output(leds[2], True)

	def btnblueFunction(self):
		GPIO.output(leds[0], True)
		GPIO.output(leds[1], False)
		GPIO.output(leds[2], True)

	def btngreenFunction(self):
		GPIO.output(leds[0], True)
		GPIO.output(leds[1], True)
		GPIO.output(leds[2], False)

	def ledoffFunction(self):
		GPIO.output(leds[0], True)
		GPIO.output(leds[1], True)
		GPIO.output(leds[2], True)

	def ultraFunction(self):
		try:
			while True:
				distance = measure()
				print("Distance: %2f cm" %distance)
				if distance < 50 and distance >= 30:
					Buzz.start(50)
					Buzz.ChangeFrequency(220)
					time.sleep(0.3)
					Buzz.ChangeFrequency(360)
					time.sleep(0.3)
				elif distance < 30 and distance >= 10:
					Buzz.start(50)
					Buzz.ChangeFrequency(380)
					time.sleep(0.3)
					Buzz.ChangeFrequency(440)
					time.sleep(0.3)
				elif distance < 10:
					Buzz.start(50)
					Buzz.ChangeFrequency(460)
					time.sleep(0.3)
					Buzz.ChangeFrequency(530)
					time.sleep(0.3)
				else:
					Buzz.stop()
				time.sleep(1)

		except  KeyboardInterrupt:
			GPIO.cleanup()

	def fndFunction(self):
		def display_number(number):
			for i in range(4):
				digit_value = number % 10
				number //= 10
				for j in range(7):
					GPIO.output(segments[j], num[digit_value][j])
				GPIO.output(digits[3 - i], GPIO.LOW)
				time.sleep(0.001)
				GPIO.output(digits[3 - i], GPIO.HIGH)

		number = 0

		try:
			while True:
				number = (number + 1) % 10000
				for _ in range(50):
					display_number(number)

		except KeyboardInterrupt:
			GPIO.cleanup()
			
if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()
