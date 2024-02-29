from flask import Flask, render_template, request, Response, send_file,redirect, url_for
import csv

app = Flask(__name__)


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

# Creating Models
# class company(db.Model):
#     __tablename__ = "companys"
 
#     id = db.Column(db.Integer, primary_key=True)
#     project = db.Column(db.String(500), nullable=False, unique=True)
#     status = db.Column(db.String(500), nullable=False)
#     location = db.Column(db.String(500), nullable=False)
    
#     def __repr__(self) -> str:
#         return f"{self.id} -{self.project} - {self.status} - {self.location}"

# class Registrants(db.Model):
#     __tablename__ = "account"
 
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(500), nullable=False, unique=True)
#     email = db.Column(db.String(500), nullable=False)
#     password = db.Column(db.String(500), nullable=False)
    
#     def __repr__(self) -> str:
#         return f"{self.id} -{self.username} - {self.email} - {self.password}"


# def create_db():
#     with app.app_context():
#         db.create_all()


@app.route("/")
def hello_world():
    return render_template('index.html', companys = companys)

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/csv")
def csv():
    return render_template('csv.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/add_record")
def add_record():
    return render_template('add.html')

# Sample data for demonstration
users = []

@app.route("/registers", methods=["GET", "POST"])
def registers():
	if request.method == "POST":
		name = request.form.get("name")
		email = request.form.get("email")
		users.append({"name": name, "email": email})
	
	return render_template("register.html", csv_data=users)

@app.route("/generate_csv")
def generate_csv():
	if len(users) == 0:
		return "No data to generate CSV."

	# Create a CSV string from the user data
	csv_data = "Name,Email\n"
	for user in users:
		csv_data += f"{user['name']},{user['email']}\n"

	return render_template("csv.html", csv_data=csv_data)

@app.route("/download_csv")
def download_csv():
	if len(users) == 0:
		return "No data to download."

	# Create a CSV string from the user data
	csv_data = "Name,Email\n"
	for user in users:
		csv_data += f"{user['name']},{user['email']}\n"

	# Create a temporary CSV file and serve it for download
	with open("users.csv", "w") as csv_file:
		csv_file.write(csv_data)

	return send_file("users.csv", as_attachment=True, download_name="users.csv")
@app.route("/download_csv_direct")
def download_csv_direct():
	if len(users) == 0:
		return "No data to download."

	# Create a CSV string from the user data
	csv_data = "Name,Email\n"
	for user in users:
		csv_data += f"{user['name']},{user['email']}\n"

	# Create a direct download response with the CSV data and appropriate headers
	response = Response(csv_data, content_type="text/csv")
	response.headers["Content-Disposition"] = "attachment; filename=users.csv"

	return response

@app.route("/register", methods=['GET','POST'])
def register():
   
    # if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     email = request.form.get('email')
    #     db.execute('INSERT INTO account (username, password, email) VALUES (?,?,?)',username, password, email)

        
    return render_template('register.html')

@app.route("/login", methods=['GET','POST'])
def login():
    # msg = ''
    # if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
    #     username = request.form['username']
    #     password = request.form['password']
    #     db.execute('SELECT * FROM account WHERE username = % s AND password = % s', (username, password, ))
    #     if account:
    #         session['loggedin'] = True
    #         session['id'] = account['id']
    #         session['username'] = account['username']
    #         msg = 'Logged in successfully !'
    #         return render_template('index.html', msg = msg)
    #     else:
    #         msg = 'Incorrect username / password !'
    return redirect('/home1')

# Add data route
@app.route("/add", methods=['GET', 'POST'])
def add_company():
    # if request.method == 'POST':
    #     company_project = request.form.get('project')
    #     company_status = request.form.get('status')
    #     company_location = request.form.get('location')
 
    #     add_detail = company(
    #        project=company_project,
    #        status =company_status,
    #        location = company_location
    #     )
       
    #     db.execute('''insert into companys("project","status","location") values ("?", "?",  "?")''')
    #     app.app_context().push()
    #     db.session.add(add_detail)
    #     db.session.commit()
        
        return redirect(url_for('home1'))
 
        return render_template("index1.html")

# Home route
@app.route("/home1")
def home1():
    # details = company.query.all()
    return render_template("index1.html")
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7002, debug=True)