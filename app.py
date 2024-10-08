from flask import Flask, request, render_template, redirect, url_for
import random

app = Flask(__name__)
secret_number = random.randint(1, 100)
attempts = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global secret_number, attempts
    message = ""
    if request.method == "POST":
        guess = int(request.form["guess"])
        attempts += 1
        if guess < secret_number:
            message = "Secret number is Higher than your Guess!"
        elif guess > secret_number:
            message = "Secret number is Lower than your Guess!"
        else:
            message = f"Correct! The number was {secret_number}. You guessed it in {attempts} attempts."
    return render_template("index.html", message=message)

@app.route("/restart")
def restart():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
