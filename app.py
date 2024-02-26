import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql
from sqlalchemy.sql import func


conn = sql.connect("database.db")

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

companys=[
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
# app.secret_key = 'your secret key'
 
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '12345'
# app.config['MYSQL_DB'] = 'mydb'
 
# mysql = MySQL(app)

# Creating Models
class company(db.Model):
    __tablename__ = "companys"
 
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(500), nullable=False, unique=True)
    status = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(500), nullable=False)
    
    def __repr__(self) -> str:
        return f"{self.id} -{self.project} - {self.status} - {self.location}"



def create_db():
    with app.app_context():
        db.create_all()

@app.route("/")
def hello_world():
    return render_template('index.html', companys = companys)

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/add_record")
def add_record():
    return render_template('add.html')

@app.route("/register", methods=['GET','POST'])
def register():
    # msg = ''
    # if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
    #     username = request.form['username']
    #     password = request.form['password']
    #     email = request.form['email']
    #     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    #     cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
    #     account = cursor.fetchone()
    #     if account:
    #         msg = 'Account already exists !'
    #     elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
    #         msg = 'Invalid email address !'
    #     elif not re.match(r'[A-Za-z0-9]+', username):
    #         msg = 'Username must contain only characters and numbers !'
    #     elif not username or not password or not email:
    #         msg = 'Please fill out the form !'
    #     else:
    #         cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
    #         mysql.connection.commit()
    #         msg = 'You have successfully registered !'
    # elif request.method == 'POST':
    #     msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

@app.route("/login", methods=['GET','POST'])
def login():
    # msg = ''
    # if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
    #     username = request.form['username']
    #     password = request.form['password']
    #     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    #     cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
    #     account = cursor.fetchone()
    #     if account:
    #         session['loggedin'] = True
    #         session['id'] = account['id']
    #         session['username'] = account['username']
    #         msg = 'Logged in successfully !'
    #         return render_template('index.html', msg = msg)
    #     else:
    #         msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

# Add data route
@app.route("/add", methods=['GET', 'POST'])
def add_company():
    if request.method == 'POST':
        company_project = request.form.get('project')
        company_status = request.form.get('status')
        company_location = request.form.get('location')
 
        add_detail = company(
           project=company_project,
           status =company_status,
           location = company_location
        )
        # c = conn.cursor()
        # c.execute('''insert into company("project","status","location") values ("?", "?",  "?")''')
        # conn.commit()
        # c.close()
        app.app_context().push()
        db.session.add(add_detail)
        db.session.commit()
        
        return redirect(url_for('home1'))
 
    return render_template("index1.html")

# Home route
@app.route("/home1")
def home1():
    details = company.query.all()
    return render_template("index1.html", details=details)
 
 

 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7002, debug=True)