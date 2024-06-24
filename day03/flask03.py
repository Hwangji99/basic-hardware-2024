# URL 접속을 /led/on, /let/off로 접속하면 led를 on, off하는 웹페이지를 만들기
import RPi.GPIO as GPIO
import time

from flask import Flask

led = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

@app.route("/led/on")
def hello():
  return "LED ON"
    
@app.route("/led/off")
def hello():
  return "LED OFF"
    
if __name__ == "__main__":
  app.run(host="0.0.0.0", port="10012", debug=True)
  GPIO.output(led, False)
else:
  GPIO.output(led, True)

except KeyboardInterrupt:  # Ctrl + c
  GPIO.cleanup()
