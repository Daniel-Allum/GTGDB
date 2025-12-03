import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


def GetDB():
    db = sqlite3.connect(".database/gtg.db")
    db.row_factory = sqlite3.Row
    return db


def GetAllGuesses():
    db = GetDB()
    guesses = db.execute("SELECT * FROM Guesses").fetchall()
    db.close()
    return guesses


def CheckLogin(username, password):
    db = GetDB()
    user = db.execute(
        "SELECT * FROM Users WHERE username=? COLLATE NOCASE", (username,)
    ).fetchone()

    if user is not None:
        if check_password_hash(user["password"], password):
            return user

    return None
