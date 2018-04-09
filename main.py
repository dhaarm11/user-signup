from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['POST'])
def errors():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    verify = request.form['verify']

    username_error = ""
    password_error  = ""
    verify_error  = ""
    email_error = ""

    if username == "":
        username_error = "That's not a valid username"

    elif " " in username:
        username_error = "That's not a valid username"

    elif len(username) < 3 or len(username) > 20:
        username_error = "That's not a valid username"

    elif password == "":
        password_error = "That's not a valid password"

    elif " " in password:
        password_error = "That's not a valid password"

    elif len(password) < 3 or len(password) > 20:
        password_error = "That's not a valid password"

    elif verify == "":
        verify_error = "Passwords don't match"

    elif password != verify:
        verify_error = "Passwords don't match"

    elif email != "" and len(email) < 3:
        email_error = "That's not a valid email"

    elif len(email) > 20:
        email_error = "That's not a valid email"

    elif "@" not in email:
        email_error = "That's not a valid email"

    elif "." not in email:
        email_error = "That's not a valid email"
    
    else:
        return render_template('welcome.html', username=username)

    return render_template('index.html', username_error=username_error,
    password_error=password_error, verify_error=verify_error, email_error=email_error)

@app.route("/")
def index():
    username_error = ""
    password_error  = ""
    verify_error  = ""
    email_error = ""

  
    return render_template('index.html', username_error=username_error,
    password_error=password_error, verify_error=verify_error, email_error=email_error)

app.run()