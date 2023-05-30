from flask import Flask, render_template

app = Flask(__name__)
stu = [{
  "SNAME": "ARNIPALLI VISHAL",
  "ROLL NO": "20891A0201"
}, {
  "SNAME": "BODDULA ALOUKIKA",
  "ROLL NO": "20891A0205"
}, {
  "SNAME": "BOLAGANI SAI VENKATESWARARAO",
  "ROLL NO": "20891A0206"
}, {
  "SNAME": "CHINTHIRALA SUNANDITHA",
  "ROLL NO": "20891A0207"
}, {
  "SNAME": "CHINTAPALLI SRIKANTH",
  "ROLL NO": "20891A0208"
}, {
  "SNAME": "CHOWKALA BHARATH",
  "ROLL NO": "20891A0209"
}, {
  "SNAME": "DACHEPALLY LAXMI PRASANNA",
  "ROLL NO": "20891A0210"
}, {
  "SNAME": "JUNJU THIRUMALESH",
  "ROLL NO": "20891A0213"
}, {
  "SNAME": "KAKANI SAI NEERAJ",
  "ROLL NO": "20891A0214"
}, {
  "SNAME": "KANDULA SINDHUJA",
  "ROLL NO": "20891A0215"
}, {
  "SNAME": "KASPARAJU PRAVEEN KUMAR",
  "ROLL NO": "20891A0216"
}, {
  "SNAME": "KETHAVATH ANIL",
  "ROLL NO": "20891A0217"
}, {
  "SNAME": "KOPPULA PAVAN REDDY",
  "ROLL NO": "20891A0218"
}, {
  "SNAME": "KYASTHU GANGA PRASAD",
  "ROLL NO": "20891A0219"
}, {
  "SNAME": "LAKAVATH PAVAN",
  "ROLL NO": "20891A0220"
}, {
  "SNAME": "MALOTH RAMESH",
  "ROLL NO": "20891A0221"
}, {
  "SNAME": "MD RIYAZ",
  "ROLL NO": "20891A0222"
}, {
  "SNAME": "N.MANIKANTA REDDY",
  "ROLL NO": "20891A0223"
}, {
  "SNAME": "NARRA RAVITEJA",
  "ROLL NO": "20891A0224"
}, {
  "SNAME": "PALLE VINAY",
  "ROLL NO": "20891A0225"
}, {
  "SNAME": "PATHI CHANDU",
  "ROLL NO": "20891A0226"
}, {
  "SNAME": "PESARU GAYATHRI",
  "ROLL NO": "20891A0227"
}, {
  "SNAME": "SULTHAN PRANEETH GIRI",
  "ROLL NO": "20891A0228"
}, {
  "SNAME": "TADI SURYA PRAKASH REDDY",
  "ROLL NO": "20891A0229"
}, {
  "SNAME": "TANGELLA YASHWANTH REDDY",
  "ROLL NO": "20891A0230"
}, {
  "SNAME": "AKASH UPPULA",
  "ROLL NO": "20891A0233"
}, {
  "SNAME": "VONTEDDU MANI PRASAD REDDY",
  "ROLL NO": "20891A0234"
}, {
  "SNAME": "KOPPU SHYAMAUNDER LIKITHA",
  "ROLL NO": "20891A0235"
}]


@app.route("/")
def home():
  return render_template("loginpage.html")


@app.route("/faculty")
def faculty():
  return render_template("faculty.html")


@app.route("/attendence")
def attendence():
  return render_template("attendence.html")


@app.route("/studata")
def sheet():
  return render_template("table.html", stu=stu)


@app.route("/assignments")
def assignments():
  return render_template("assignmnts.html")


@app.route("/evaluation")
def evaluation():
  return render_template("evaluation.html")


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
