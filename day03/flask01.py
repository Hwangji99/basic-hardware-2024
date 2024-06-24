from flask import Flask

app = Flask(__name__)    # name 이름을 통한 flask 객체 생성

@app.route("/")          # 라우팅을 위한 뷰함수 등록  # /로 요청하면
def hello():             # hello 함수가 실행되어 
  return "안녕하시렵니까!!"  # 화면에 글이 나타남

if __name__=="__main__":
  app.run(host="0.0.0.0", debug=True)
