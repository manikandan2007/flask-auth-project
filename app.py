from flask import Flask, request, redirect, session, render_template, flash

app = Flask(__name__)
app.secret_key = "key"


@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        u = request.form["u"]
        p = request.form["p"]

        open("users.txt", "a").write(u + "<==UserId  :  Password==>" + p + "\n")
        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form["u"]
        p = request.form["p"]

        for line in open("users.txt"):
            if "<==UserId  :  Password==>" in line:
                user, pwd = line.strip().split("<==UserId  :  Password==>")
                if u == user and p == pwd:
                    session["u"] = u
                    return redirect("/home")

        flash("Wrong login credentials. Please try again.")
        return redirect("/login")

    return render_template("login.html")


@app.route("/home")
def home():
    if "u" not in session:
        return redirect("/login")

    return render_template("home.html", username=session["u"])


@app.route("/logout")
def logout():
    session.pop("u", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)