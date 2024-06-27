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

def fndOut(data):     # 하나의 숫자 형태를 만드는 함수
   for i in range(0, 7):
      GPIO.output(fndSegs[i], fndData[data] & (0x01 << i))
try:
   while True:
      for i in range(0, 1):
         GPIO.output(fndSels[i], 0)    # fnd 선택
         # GPIO.output(22, 1)
         # GPIO.output(23, 1)

         for j in range(0, 10):
            fndOut(j)
            time.sleep(0.5)

except KeyboardInterrupt:
   GPIO.cleanup()
