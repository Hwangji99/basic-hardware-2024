# basic-rasberrypy-2024
IoT 개발자 과정  라즈베리파이 리포지토리

## 1일차(2024-06-20)
- 옴의 법칙
    - 회로를 통과해 흐르는 전류는 회로의 양단에 가해진 전압에 비례한다는 규칙 V = IR
    - 전류(C) : 전하의 흐름
        - 전자의 이동 방향과 반대
        - 전자의 이동 방향: 전지의 (-)극 -> (+)극
        - 전류의 이동 방향: 전지의 (+)극 -> (-)극
    - 전압(V) : 전기회로에서 전류를 흐르게 하는 능력
        - 물의 흐름과 전기회로의 비유 : 펌프로 물을 끌어올리면 물의 높이 차이 때문에 생긴 수압에 물이 흐르듯이 전기 회로에서는 전지의 전압에 의해 전류가 흐름
    - 저항(R) : 전류를 방해하는 요소
    - GRD : 모든 전류는 그라운드로 흐른다(모인다)

- 키르히호프 법칙
    - 전류가 흐르는 즉 전기가 통과하는 분기점(선의 연결지점, 만나는 지점)에서, 전류의 합 즉 들어온 전류의 양과 나간 전류의 양의 합은 같다.

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

        <img src="https://raw.githubusercontent.com/Hwangji99/basic-rasberrypi-2024/main/images/풀업 저항.png" width="600">


    - 풀다운 저항
        - 전원부에 스위치를 연결한 경우에 Floating 현상을 제거하기 위한 방법

        <img src="https://raw.githubusercontent.com/Hwangji99/basic-rasberrypi-2024/main/images/풀다운 저항.png" width="600">

