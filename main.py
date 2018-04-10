from flask import Flask, request, redirect, render_template
import os
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True
    
@app.route("/")
def index():
    return render_template('user.html')

@app.route("/", methods=['POST'])
def sign_in():
    
    username = request.form['username']
    password = request.form['psw']
    reenter = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    reenter_error = ""
    email_error = ""

    if len(username) <3 or len(username) >20:
        username_error = "Invalid username. Must be between 3 & 20 characters (no spaces)."
        
    if len(password) == 0 or len(password) <3 or len(password) >20:
        password_error = "Please enter a valid password (between 3 & 20 characters, no spaces)."
        password = ""
        reenter = ""

    if password != reenter:
        reenter_error = "Passwords do not match. Please re-enter."
        password = ""
        reenter = ""

    if email != "" and "@" not in email or "." not in email:
        email_error = "Please enter a valid e-mail."

    if not username_error and not password_error and not reenter_error and not email_error:
        return redirect("/user_welcome?username={0}".format(username))

    else:
        return render_template('user.html', username_error=username_error, password_error=password_error, 
        reenter_error= reenter_error, email_error=email_error, username=username, email=email)


@app.route("/user_welcome")
def user_welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()