from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World"

if _name_=="__name__":
  app.run(host="0.0.0.0", debub=True)
