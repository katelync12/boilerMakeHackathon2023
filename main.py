from flask import Flask, redirect, url_for, render_template
from sampledstream import create_url, connect_to_endpoint
from dotenv import load_dotenv

app = Flask(__name__, static_folder="css")

data = [
    {
        'rank':'1',
        'username': '@Donuts',
        'cancels': '7736'
    },
    {
        'rank':'2',
        'username': '@TreasureChest',
        'cancels': '6032'
    },
    {
        'rank':'3',
        'username': '@JimmyJohns',
        'cancels': '5132'
    },
    {
        'rank':'4',
        'username': '@Duolingo',
        'cancels': '4211'
    },
    {
        'rank':'5',
        'username': '@SlimJim',
        'cancels': '5131'
    }
]

# @app.route("/<name>")

@app.route("/")
def user(name=''):
    print(name)
    url = create_url()
    try:
        global tweets
        tweets = []
        tweets = connect_to_endpoint(url)
    except Exception as err:
        print(f"Error retrieving tweets: {err}")
    print('Num tweets:', len(tweets))
    return render_template("index.html", content=tweets)#data)

@app.route("/aboutUs")
def about():
    return render_template("aboutUs.html")


# When the route (url) is the same as an html file in the templates folder, 
# flask gives a 404. Maybe because it thinks we're trying to read the html file
# directly?
@app.route("/x.html")
def x():
    return render_template("index.html", content=[])


if __name__ == "__main__":
    load_dotenv()


    app.run(debug=True)
