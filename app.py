from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("loginpage.html")


@app.route("/faculty")
def faculty():
  return render_template("faculty.html")


@app.route("/attendence")
def attendence():
  return render_template("attendence.html")


@app.route("/assignments")
def assignments():
  return render_template("assignmnts.html")


@app.route("/evaluation")
def evaluation():
  return render_template("evaluation.html")


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
