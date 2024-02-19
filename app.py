from flask import Flask,render_template,url_for


app = Flask(__name__)
company=[
    {
        'id':1,'project':'web development','status':'available', "location":'Ghana'
    },
     {
        'id':2,'project':' Registration form development','status':'available',"location":'Ghana'
    },
     {
        'id':3,'project':'Database Management','status':'available',"location":'Ghana'
    }
]

@app.route("/")
def hello_world():
    return render_template('index.html', company=company)

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET','POST'])
def register():
    return render_template('register.html')

@app.route("/login", methods=['GET','POST'])
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7002, debug=True)