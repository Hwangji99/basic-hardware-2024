import RPi.GPIO as GPIO
import time

# 0 ~ 9 까지 1byte hex값
fndData = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]
fndSegs = [21, 22, 23, 24, 25, 26, 27] # a ~ g led pin
fndSels = [17, 18, 19, 20]    # fnd 선택 pin

# GPIO 설정
GPIO.setmode(GPIO.BCM)
for fndSeg in fndSegs:     # for 단수 in 복수 # 복수(리스트)로부터 단수(인덱스)를 뽑아낸다
   GPIO.setup(fndSeg, GPIO.OUT)
   GPIO.output(fndSeg, 0)

for fndSel in fndSels:
   GPIO.setup(fndSel, GPIO.OUT)
   GPIO.output(fndSel, 1)  # 아무것도 선택안함

def fndOut(data, sel):     # 하나의 숫자 형태를 만드는 함수
	for h in range(0, 50):
		for i in range(0, 7):
			GPIO.output(fndSegs[i], fndData[data] & (0x01 << i))
			for j in range(0, 4):   # 표시할 자리 수의 fnd만 on
				if j==sel:
					GPIO.output(fndSels[j], 0)
				else:
					GPIO.output(fndSels[j], 1)

count = 0

try:
	while True:
		count += 1
		d1000 = count / 1000
		d100 = count % 1000 / 100
		d10 = count % 100 / 10
		d1 = count % 10

		d = [d1000, d100, d10, d1]
		for i in range(3, -1, -1):
			fndOut(int(d[i]),i)  # 자리 수와 값을 전달
			time.sleep(0.1)

except KeyboardInterrupt:
	GPIO.cleanup()
