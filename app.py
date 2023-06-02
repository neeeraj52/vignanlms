from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from database import client

app = Flask(__name__)
app.secret_key = "super secret key"


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


@app.route("/login", methods=["GET", "POST"])
def login():
  msg = ""
  if request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]
    dbs = client["login"]
    coll = dbs["success"]
    result = coll.find_one({"username": username, "password": password})
    if result:
      session["loggedin"] = True
      session["username"] = result["username"]
      return redirect(url_for(result["role"]))
    else:
      msg = "incorrect user name/password try again!!!"
  return render_template("loginpage.html", msg=msg)


@app.route("/faculty")
def faculty():
  return render_template("faculty.html")


@app.route("/student")
def student():
  return render_template("student.html", username=session["username"])


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


@app.route("/posting", methods=['post'])
def posting():
  data = request.form
  stu = load_students_from_db(data)
  session["section"] = data["section"]
  return render_template("evaluation_table.html", stu=stu)


@app.route("/submited", methods=["post"])
def submited():
  msg = ""
  data = request.form
  db = client["marks"]
  col = db["3yeareee" + data["subject"]]
  col.delete_many({})
  a = {}
  for s in data:
    a[s] = data[s]
  col.insert_one(a)
  return msg


@app.route("/marked", methods=["post"])
def marked():
  msg = ""
  data = request.form
  db = client["attendence"]
  col = db["3yeareeea"]
  a = {}
  b = []
  for i in col.find():
    b.append(i)
  for s in data:
    if (data[s] == "p"):
      a[s] = str(int(b[0][s]) + 1)
    else:
      a[s] = str(int(b[0][s]) + 0)
  col.delete_many({})
  col.insert_one(a)
  return msg


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
