import RPi.GPIO as GPIO
import time

switch = 5  # 스위치 핀 번호

# 7세그먼트 디스플레이의 각 세그먼트 핀들
segments = (21, 22, 23, 24, 25, 26, 27)

# 4자리 숫자를 표시하기 위한 디스플레이의 각 자릿수에 해당하는 공통 핀들
digits = (17, 18, 19, 20)

# 각 숫자를 7세그먼트 디스플레이로 표현하기 위한 세그먼트 설정
# (a, b, c, d, e, f, g) 순서로 세그먼트 상태를 나타냄
num = [
    (1, 1, 1, 1, 1, 1, 0),  # 0
    (0, 1, 1, 0, 0, 0, 0),  # 1
    (1, 1, 0, 1, 1, 0, 1),  # 2
    (1, 1, 1, 1, 0, 0, 1),  # 3
    (0, 1, 1, 0, 0, 1, 1),  # 4
    (1, 0, 1, 1, 0, 1, 1),  # 5
    (1, 0, 1, 1, 1, 1, 1),  # 6
    (1, 1, 1, 0, 0, 0, 0),  # 7
    (1, 1, 1, 1, 1, 1, 1),  # 8
    (1, 1, 1, 1, 0, 1, 1)   # 9
]

# GPIO 핀 번호 체계를 BCM 모드로 설정
GPIO.setmode(GPIO.BCM)

# 각 세그먼트 핀을 출력으로 설정하고 초기 상태를 LOW로 설정
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

# 각 자릿수 공통 핀을 출력으로 설정하고 초기 상태를 HIGH로 설정
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)

# 스위치 핀을 입력으로 설정하고 풀다운 저항을 사용하여 초기 상태를 LOW로 설정
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def display_number(number):
    """
    주어진 숫자를 4자리 7세그먼트 디스플레이로 표시합니다.

    number: 표시할 숫자 (0~9999)
    """
    # 각 자릿수의 숫자를 추출하여 표시
    for i in range(4):
        digit_value = number % 10  # 숫자의 가장 낮은 자릿수 추출
        number //= 10  # 추출한 자릿수 제거

        for j in range(7):
            GPIO.output(segments[j], num[digit_value][j])
        GPIO.output(digits[3 - i], GPIO.LOW)  # 현재 자릿수 활성화
        time.sleep(0.001)  # 짧은 시간 동안 활성화 유지 (다중화)
        GPIO.output(digits[3 - i], GPIO.HIGH)  # 현재 자릿수 비활성화

number = 0  # 초기 숫자 상태를 0로 설정

try:
    while True:
    	number = (number + 1) % 10000
    	for _ in range(50):
    		display_number(number)
    	  #display_number(state)  # 현재 숫자 표시
        #time.sleep(0.01)  # 0.01초 대기

except KeyboardInterrupt:
    GPIO.cleanup()  # 프로그램 종료 시 GPIO 설정 초기화
