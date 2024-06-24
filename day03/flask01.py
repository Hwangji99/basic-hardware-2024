from flask import Flask

app = Flask(_name_)

@app.route("/")
def hello():
  return "Hello World"

if _name_=="_name_":
  app.run(host="0.0.0.0", debub=True)
