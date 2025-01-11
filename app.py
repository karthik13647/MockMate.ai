from flask import Flask, render_templates

app=Flask(__name__)

@app.route("/")

def func():
  return render_templates("index.html")

if __name__=="__main__":
  app.run(port="0.0.0.0",dubug=True)
