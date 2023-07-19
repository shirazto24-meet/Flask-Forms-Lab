from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "cherrybear"
password = "123"
facebook_friends=["Leshem","Oded","Adam", "Yanay", "Sasha", "Gabby"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		username2= request.form['username']
		password2= request.form['password']

		if username2 == username and password2==password:
			return redirect(url_for('home'))
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')
  
@app.route("/home")
def home():
	return render_template('home.html', facebook_friends= facebook_friends)

@app.route("/friend_exists/<string:name>",methods=['GET','POST'])
def friend_exists(name):
	if name in facebook_friends:
		exist = True
	else:
		exist = False

	return render_template('friend_exists.html', name=name, exist = exist)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)