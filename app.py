from flask import Flask, render_template, request, redirect, url_for, session
import random
import string

app = Flask(__name__)
app.secret_key = "Srik@r2004"  # Needed for session

def generate_usernames(first, last):
    first = first.strip().lower()
    last = last.strip().lower()
    base = first + last
    suggestions = []

    for _ in range(5):
        number = str(random.randint(1, 9999))
        style = random.choice([
            f"{base}_{number}",
            f"{first}_{last}{number}",
            f"{first}{last}_{number}",
            f"{first}_{last}_{number}",
            f"{first}{last}{number}"
        ])
        suggestions.append(style)

    return suggestions

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first = request.form.get("first_name")
        last = request.form.get("last_name")
        if first and last:
            session["usernames"] = generate_usernames(first, last)
        return redirect(url_for("index"))  

    usernames = session.pop("usernames", [])  
    return render_template("index.html", usernames=usernames)

if __name__ == "__main__":
    app.run(debug=True)
