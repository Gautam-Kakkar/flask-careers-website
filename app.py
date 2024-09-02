from flask import Flask, render_template

app = Flask(__name__)

JOBS =[
    {
        'id':1,
        'title':'Data analyst',
        'location':'Bangalore, India',
        'salary':"Rs. 1000"
    },
    {
        'id':2,
        'title':'Data scientist',
        'location':'Bangalore, India',
        'salary':"Rs. 1200"
    },
    {
        'id':3,
        'title':'Frontend engineer',
        'location':'Delhi, India',
        'salary':"Rs. 900"
    },
    {
        'id':4,
        'title':'Backend engineer',
        'location':'Bangalore, India',
        'salary':"Rs. 1400"
    }
]
@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS)
print(__name__)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug="True", port='5001')