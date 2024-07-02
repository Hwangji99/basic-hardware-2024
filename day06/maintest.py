from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
from PyQt5.QtCore import *
import sys
import RPi.GPIO as GPIO
import time
import threading
import adafruit_dht
import board

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

log_num = 0

leds = [26, 19]
piezoPin = 6
trigPin = 27
echoPin = 17

sensor_pin = 18

segments = (20, 21, 16, 12, 24, 13, 5)

digits = (23, 25, 4, 22)

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
GPIO.setwarnings(False)

dhtDevice = adafruit_dht.DHT11(board.D18)

# PWM(Pulse Width Modulation)을 사용하여 부저를 제어하기 위한 객체 생성
Buzz = GPIO.PWM(piezoPin, 1.0)	# piezoPin에 연결된 PWM 객체 생성, 주파수 1.0으로 초기화

# 멜로디를 위한 음계 리스트
scale = [ 262, 294, 330, 349, 392, 440, 494 ]

# 피에조 부저를 사용한 멜로디를 정의한 리스트
twinkle = [ 0, 0, 4, 4, 5, 5, 4,
			   3, 3, 2, 2, 1, 1, 0,
			   4, 4, 3, 3, 2, 2, 1,
			   4, 4, 3, 3, 2, 2, 1,
			   0, 0, 4, 4, 5, 5, 4,
			   3, 3, 2, 2, 1, 1, 0 ]

for segment in segments:
	GPIO.setup(segment, GPIO.OUT)
	GPIO.output(segment, GPIO.LOW)

for digit in digits:
	GPIO.setup(digit, GPIO.OUT)
	GPIO.output(digit, GPIO.HIGH)

form_class = uic.loadUiType("./main.ui")[0]

class WorkerThread(QThread):
	buzzingChanged = pyqtSignal(bool)	# 부저 울림 상태가 변경될 때 발생할 시그널 정의
	def __init__(self, parent=None):
		super().__init__(parent)
		self.buzzing = False	# 부저 울림 상태 초기화

	def run(self):
		self.buzzing = True	# 부저 울림 시작 상태로 설정
		Buzz.start(50)	# PWM을 50% 듀티 사이클로 시작하여 부저 울림 시작
		try:
			for i in range(0, 42):	# twinkle 리스트의 각 음표에 대해 반
				if not self.buzzing:	# self.buzzing이 False이면 멜로디 재생 중지
					break
				Buzz.ChangeFrequency(scale[twinkle[i]])	# 현재 음표의 주파수 설정
				if i in [6, 13, 20, 27, 34, 41]:	# 멜로디의 특정 위치에서는 긴 시간동안 쉼
					time.sleep(1.0)
				else:
					time.sleep(0.5)	# 그 외의 경우는 짧은 시간동안 쉼
		finally:
			Buzz.stop()	# 부저 울림 종료
			self.buzzingChanged.emit(False)	# 부저 울림 상태 변경 시그널 발생

	def stopBuzzing(self):
		self.buzzing = False	# 부저 울림 중지



class WindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		
		self.update_timer = QtCore.QTimer(self)
		self.update_timer.timeout.connect(self.update_sensor_values)
		#self.update_timer.start(2000)

		self.btnred.clicked.connect(self.btnredFunction)
		self.btnblue.clicked.connect(self.btnblueFunction)
		#self.btngreen.clicked.connect(self.btngreenFunction)_sensor_values)  # 시그널 연결 삭제
		self.led_off.clicked.connect(self.ledoffFunction)
		self.btn_ultraon.clicked.connect(self.ultraonFunction)
		#self.btn_ultraoff.clicked.connect(self.ultraoffFunction)
		self.btn_fndon.clicked.connect(self.fndonFunction)
		#self.btn_fndoff.clicked.connect(self.fndoffFunction)
		self.btn_buzzon.clicked.connect(self.buzzonFunction)
		self.btn_buzzoff.clicked.connect(self.buzzoffFunction)
		self.btn_temhuon.clicked.connect(self.temhuonFunc)
		self.btn_temhuoff.clicked.connect(self.temhuoffFunc)
		self.btnexit.clicked.connect(self.exitFunction)  # btnexit 버튼 클릭 시 exitFunction 실행

		self.worker_thread = WorkerThread()	# WorkerThread 객체 생성
		self.worker_thread.buzzingChanged.connect(self.handleBuzzingChanged)	# WorkerThread의 buzzingChanged 시그널을 handleBuzzingChanged 메서드에 연결
	

	def update_sensor_values(self):
		global log_num
		try:
			temp = dhtDevice.temperature
			humid = dhtDevice.humidity
			if temp is not None and humid is not None:
				self.lcdtemp.display(temp)  # lcdtemp는 Qt Designer에서 설정한 LCD 객체 이름
				self.lcdhum.display(humid)  # lcdhum은 Qt Designer에서 설정한 LCD 객체 이름
				print(f'{log_num} - Temp : {temp}C / Humid : {humid}%')
				log_num += 1
			else:
				self.lcdtemp.display(0)
				self.lcdhum.display(0)
		except RuntimeError as error:
			print(error.args[0])
		
	def temhuonFunc(self):
		self.update_timer.start(2000)

	def temhuoffFunc(self, event):
		self.update_timer.stop()
		#self.dhtDevice.exit()
		#event.accept()

	def buzzonFunction(self):
		if not self.worker_thread.isRunning():	# WorkerThread가 실행 중이지 않으면
			self.worker_thread.start()	# WorkerThread를 시작하여 멜로디를 재생합니다

	def buzzoffFunction(self):
		self.worker_thread.stopBuzzing()	# WorkerThread의 멜로디 재생을 멈추도록 stopBuzzing 메서드 호출
		Buzz.stop()

	def handleBuzzingChanged(self, buzzing):
		if not buzzing:	# buzzing이 False일 때 (멜로디 재생이 멈춘 상태)
			Buzz.stop()		# 부저를 멈추도록 함

	def btnredFunction(self):
		GPIO.output(leds[0], False)
		GPIO.output(leds[1], True)
		#GPIO.output(leds[2], True)

	def btnblueFunction(self):
		GPIO.output(leds[0], True)
		GPIO.output(leds[1], False)
		#GPIO.output(leds[2], True)

	#def btngreenFunction(self):
		#GPIO.output(leds[0], True)
		#GPIO.output(leds[1], True)
		#GPIO.output(leds[2], False)

	def ledoffFunction(self):
		GPIO.output(leds[0], True)
		GPIO.output(leds[1], True)
		#GPIO.output(leds[2], True)

	def ultraonFunction(self):
		try:
			while True:
				distance = measure()
				print("Distance: %2f cm" %distance)
				time.sleep(1)

		except  KeyboardInterrupt:
			GPIO.cleanup()

	def fndonFunction(self):
		def display_number(number):
			for i in range(4):
				digit_value = number % 10
				number //= 10
				for j in range(7):
					GPIO.output(segments[j], num[digit_value][j])
				GPIO.output(digits[3 - i], GPIO.LOW)
				time.sleep(0.001)
				GPIO.output(digits[3 - i], GPIO.HIGH)

		# def update_display(number):
		# 	# 7세그먼트 디스플레이 업데이트
		# 	for _ in range(50):
		# 		display_number(number)
		# 	# lcdfnd 화면 업데이트
		# 	self.lcdfnd.display(number)

		number = 0


		try:
			while True:
				number = (number + 1) % 10000
				for _ in range(50):
					display_number(number)

		except KeyboardInterrupt:
			GPIO.cleanup()

	def update_display(self):
		self.current_number = (self.current_number + 1) % 10000
		self.display_number(self.current_number)
		self.lcdfnd.display(self.current_number)

	def exitFunction(self):
		self.update_timer.stop()  # 타이머 중지
		GPIO.cleanup()  # GPIO 정리
		self.close()  # 창 닫기

	
if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()
