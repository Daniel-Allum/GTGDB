from flask import Flask, render_template, request, session, redirect
import db

app = Flask(__name__)
app.secret_key = "gtg"


@app.route("/")
def Home():
    guessData = db.GetAllGuesses()
    return render_template("index.html", guesses=guessData)


@app.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if db.CheckLogin(username, password):
            session["username"] = username
            return redirect("/")
    return render_template("login.html")


@app.route("/logout")
def Logout():
    session.clear()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def Register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if db.RegisterUser(username, password):
            return redirect("/")
    return render_template("register.html")


app.run(debug=True, port=5000)
