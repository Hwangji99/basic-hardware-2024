# basic-rasberrypy-2024
IoT 개발자 과정  라즈베리파이 리포지토리

## 1일차(2024-06-20)
- 옴의 법칙
    - 
    - 전류(C) :
    - 전압(V) :
    - 저항(R) :
    - GRD : 모든 전류는 그라운드로 흐른다(모인다)

- 키르히호프 법칙
    - 

- Python 함수
    - GPIO 설정 함수
        - GPIO.setmode(GPIO.BOARD) - wPi
        - GPIO.setmode(GPIO.BCM) - BCM
        - GPIO.setup(channel, GPIO.mode)
            - channel: 핀번호, mode : IN/OUT
        - GPIO.cleanup()
    - GPIO 출력 함수
        - GPIO.output(channel, state)
            - channel: 핀번호, state: HIGH(1)/LOW(0) or 1/0 or True/False
    - GPIO 입력 함수
        - GPIO.input(channel)
            - channel: 핀번호, 반환값: HIGH/LOW or 1/0 or True/False
    - 시간 지연 함수
        - time.sleep(secs)

- 스위치
    - 플로팅 현상
        - 신호가 뜨게 되어 HIGH 인지 LOW 인지 인식하지 못한다는 것을 의미
    - 풀업 저항
        - 접지부에 스위치를 연결한 경우에 Floating 현상을 제거하기 위한 방법

        <img src="https://raw.githubusercontent.com/Hwangji99/basic-rasberrypi-2024/main/images/풀업 저항.png" width="730">


    - 풀다운 저항
        - 전원부에 스위치를 연결한 경우에 Floating 현상을 제거하기 위한 방법

        <img src="https://raw.githubusercontent.com/Hwangji99/basic-rasberrypi-2024/main/images/풀다운 저항.png" width="730">

        