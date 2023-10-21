from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':"Data Analyst",
        'location':"Bengaluru,Bharat",
        'salary':"Rs.10,00,000"
    },
    {
        'id':2,
        'title':"Data Mining",
        'location':"Bengaluru,Bharat",
        'salary':"Rs.20,00,000"
    },
    {
        'id':3,
        'title':"Java",
        'location':"Pune,Bharat",
        'salary':"Rs.30,00,000"
    },
    {
        'id':4,
        'title':"PHP Devloper",
        'location':"Pune,Bharat",
        'salary':"Rs.5,00,000"
    },
    {
        'id':5,
        'title':"Django",
        'location':"Kerala,Bharat",
    },
    {
        'id':6,
        'title':"Spring Boot",
        'location':"Bengaluru,Bharat",
        'salary':"Rs.20,00,000"
    }
]

@app.route("/")
def hello_World():
    return render_template("home.html",jobs=JOBS,about="About")

@app.route("/api/json")
def jsonapp():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)