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

## 2일차(2024-06-21)
- 라즈베리 파이 파이썬
    - 가상환경
        - python -V : 파이썬 버전 확인
        - python -m venv env(가상환경명) : 가상환경 env 생성
        - source ./env/bin/activate : 가상환경 실행
        - python -m venv --system-site-packages env
        - pip install '라이브러리 명'
        - deactivate : 가상환경 실행 중지(빠져나오기)

    - Wiring
        - 라즈베리파이에서 GPIO에 접근하는 방법
        - https://github.com/Wiring/Wiring
        - Wiring 폴더 안에서 ./bulid 실행
        - gpio readall : 라즈베리파이의 gpio에 대한 핀 정보가 출력
## 3일차(2024-06-24)
- 릴레이 모듈
    - 사용 모듈 : 1채널 5V 미니 릴레이 모듈
    - 용도 : 신호를 만들어내어 자동으로 ON/OFF를 조정하는 스위치 역할의 모듈
    - NC(Normally Close) : 평상시에 닫혀있다는 뜻으로, 릴레이에 전류가 흐르면 Open 되므로 평상시에 전원을 on 상태로 유지하다가 신호를 주어 off 할 때 사용
    - NO(Normally Open) : 평상시에 열려있다는 뜻으로, 릴레이에 전류가 흐르면 Close 되므로 평상시에 전원을 off 상태로 유지하다가 신호를 주어 on 할 때 사용
    - COM(Common) : 공통 단자로 전력 또는 외부기기의 한쪽 선을 항상 연결해야 하는 단자
    - 예시(LED모듈 스위치)
        - 릴레이 모듈 S : GPIO 연결
        - 릴레이 모듈 + : 5V 연결
        - 릴레이 모듈 - : GND 연결
        - 릴레이 모듈 COM : 5V 연결
        - 릴레이 모듈 NO or NC : LED 모듈의 VCC와 연결
        - LED 모듈 RGB : GND 연결

- 스텝 모터와 모터 드라이버

    - 스텝 모터 : 한 바퀴의 회전을 많은 수의 스텝 들로 나눌 수 있는 앙페르의 오른손 법칙을 활용한 브러쉬리스 직류 전기 모터

    - 앙페르의 오른손 법칙 :

    - 모터 드라이버 : 스텝 모터를 원활하게 제어하기 위한 장치

    - 모터를 라즈베리 파이에 직접 연결하지 말것(모터의 전원이 종료될 때 연기전력이 발생되기 때문)

    - 스텝 모터 작동 방식

        - 1상 여자 방식 : 차례로 1개으 상에 전기 신호를 줌
        - 2상 여자 방식 : 동시에 2개의 상에 전기 신호를 줌
        - 1-2상 여자 방식 : 1상과 2상 방식을 반복

    - 예시

        - 모터 드라이버 + : 5V 연결
        - 모터 드라이버 - : GND 연결
        - 모터 드라이버 IN1 ~ IN4 : 각각의 GPIO에 연결

- Flask

    - 웹 애플리케이션 개발을 위한 파이썬 프레임워크
    ```C
    from flask import Flask # name 이름을 통한 flask 객체 생성
    app = Flask(__name__)

    @app.route("/") # 라우팅을 위한 뷰 함수
    def hello():    # 등록 사이트에 접속을 성공한다면 hello 함수 실행
    return "Hello World!"

    if __name__ == "__main__":  # 터미널에서 직접 실행시키면 실행 파일이 main으로 바뀜
        app.run(host="0.0.0.0", port="10111", debug=True)
    ```
    
    ```C
    GET 방식 데이터 전달 방법
    # 주소전달 방법 : 주소/?이름=James&주소=Busan

    from flask import Flask, request

    app = Flask(__name__)

    @app.route("/")
    def get():
        value1 = request.args.get("이름","user")
        value2 = request.args.get("주소","부산")
        return value1+ ":" + value2

    if __name__ == "__main__":
        app.run(host = "0.0.0.0", port="18080", debug = True)
    ```
- 스텝 모터

- IP주소 + 포트번호/?이름=황지환&주소=미국

## 4일차(2024-06-25)
- 카메라 모듈 

- FND 모듈

    - 4-digit 규격의 공통 음극(Common Cathod)방식
        - a ~ dp : VCC(HIGH)
        - COM1 ~ COM4 : GND(LOW)
    - 4-digit 규격의 공통 양극(Common Anode)방식
        - a ~ dp : GND(LOW)
        - COM1 ~ COM4 : VCC(HIGH)

    <img src="https://raw.githubusercontent.com/Hwangji99/basic-rasberrypi-2024/main/images/ri001.png" width="600">

## 5일차(2024-06-26)
