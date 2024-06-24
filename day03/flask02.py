# 정적라우팅
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "안녕하세요 안녕하세요 동쪽의 마~을에서~"

@app.route("/name")
def name():
  return "<h1>my name is Hwang Ji-hwan</h1>"

@app.route("/age")
def age():
  return "<h1> 30 year's old</h1>"

if __name__ == "__name__":
  app.run(host="0.0.0.0", port="10012", debug=True)
