from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, static_folder="css")


@app.route("/<name>")
def user(name):
    return render_template("index.html", content=["joe", "bob"])



if __name__ == "__main__":
    app.run(debug=True)
