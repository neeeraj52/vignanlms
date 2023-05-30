from flask import Flask, render_template, request, jsonify
from database import client

app = Flask(__name__)


def load_students_from_db(data):
  db = client[data["year"]]
  col = db[data["branch"] + data["section"]]
  stu = []
  for x in col.find():
    stu.append(x)
  return stu


@app.route("/")
def home():
  return render_template("loginpage.html")


@app.route("/faculty")
def faculty():
  return render_template("faculty.html")


@app.route("/attendence")
def attendence():
  return render_template("attendence.html")


@app.route("/studata", methods=["post"])
def post():
  data = request.form
  stu = load_students_from_db(data)
  return render_template("table.html", stu=stu)


@app.route("/assignments")
def assignments():
  return render_template("assignmnts.html")


@app.route("/evaluation")
def evaluation():
  return render_template("evaluation.html")


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
