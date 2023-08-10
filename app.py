from flask import Flask, render_template

app = Flask(__name__)

JOBS =[
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Kwun Tong, Hongkong',
    'salary': 'HKD. 100,000'
  },
  {
    'id': 2,
    'title': 'Programmer',
    'location': 'New York, USA',
    'salary': 'HKD. 200,000'
  },
  {
    'id': 3,
    'title': 'Data Analyst',
    'location': 'Bangkok, Thai',
    'salary': 'HKD. 300,000'
  },
  {
    'id': 3,
    'title': 'Backbend Engineer',
    'location': 'New York, USA',
    'salary': 'HKD. 400,000'
  }
]
@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="Sung Limited")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)