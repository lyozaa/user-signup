from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/welcome")
def welcome_new():
    welcome_user = request.args.get("username")
    return render_template("welcome.html", username = welcome_user)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    #initialize empty errors
    username_error_msg = ""
    password_error_msg = ""
    verify_password_error_msg = ""
    email_error_msg = ""

    username = request.form["username"]
    user_password = request.form["user_password"]
    password_confirm = request.form["password_confirm"]
    user_email = request.form["user_email"]

    if username == "":
        username_error_msg = "Please enter a username."
    if len(username) < 3:
        username_error_msg = "Username must be 3-20 characters."
    if len(username) > 20:
        username_error_msg = "Username must be 3-20 characters."
    if " " in username:
        username_error_msg = "Username cannot contain a space."
    if user_password == "":
        password_error_msg = "Please enter a password."
    if password_confirm == "":
        verify_password_error_msg = "Please confirm your password."
    if user_password != password_confirm:
        password_error_msg = "Passwords do not match."
        verify_password_error_msg = "Passwords do not match."
    if "@" not in user_email:
        email_error_msg = "Please enter a valid email address."
    if "." not in user_email:
        email_error_msg = "Please enter a valid email address."
    if " " in user_email:
        email_error_msg = "Please enter a valid email address."

    if username_error_msg == "" and password_error_msg == "" and verify_password_error_msg == "" and email_error_msg == "":
         return redirect("/welcome?username=" + username)
    else:
        return render_template("index.html", 
        #username = username,
        #user_password = user_password,
        #verify_password = verify_password,
        #user_email = user_email,
        username_error = username_error_msg,
        password_error = password_error_msg,
        verify_password_error = verify_password_error_msg,
        email_error = email_error_msg
    )

app.run()