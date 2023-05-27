from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
  return render_template("projectlogin.html")


@app.route('/faculty')
def faculty():
  return render_template("faculty.html")

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
