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
        user = db.CheckLogin(username, password)
        if user:
            session["id"] = user["id"]
            session["username"] = user["username"]
            return redirect("/")
    return render_template("login.html")


@app.route("/logout")
def Logout():
    session.clear()
    return redirect("/")


app.run(debug=True, port=5000)
