from flask import Flask, request, redirect, render_template

@app.route("/hello", methods=['POST'])
def signup_inputs():
    return render_template("inputs.html", XXXXX)
    <style>
    br {margin-bottom: 20px;}
    </style>
    <form method='POST'>
        <label>type=text
            <input name="username" type="text" />
        </label>
        <br>
        <label>type=password
            <input name="user_password" type="password" />
        </label>
        <br>
        <label>type=password
            <input name="user_password" type="password" />
        </label>
        <br>
        <label>type=email
            <input name="user-email" type="text" />
        </label>
    