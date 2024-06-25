# 동일한 폴더 위치에 templates 폴더를 만들고 거기에 html 파일을 저장한다

import RPi.GPIO as GPIO
from flask import Flask, request, render_template
# from gpiozero import LED

led = LED(21)

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/data', methods = ['POST'])
def data():
  data = request.form['led']

  if(data == 'on'):
    GPIO.output(led, False)
    return home()

  elif(data == 'off'):
    GPIO.output(led, True)
    return home()

if __name__ == '__main__':
  try:
    app.run(host = '0.0.0.0', port = '10101', debug=True)
  except KeyboardInterrupt:
    GPIO.cleanup()
