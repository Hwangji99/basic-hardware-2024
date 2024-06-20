import RPi.GPIO as GPIO

led = 21

# GPIO를 BCM 모드로 설정
GPIO.setmode(GPIO.BCM)

# GPIO핀 설정 (입력/출력)
GPIO.setup(led, GPIO.OUT)

try:
  while True:
    GPIO.output(led, False)  # True는 5V  # 전류가 흐르려면 전압차가 있어야 한다

except KeyboardInterrupt:  # Ctrl + c
  GPIO.cleanup()
