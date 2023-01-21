import sqlite3
from typing import Dict, List
db_file = 'tweets.db'
e = "Couldn't connect to db."

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
    """
    Workflow:
    1) retrieve a certain number of recent tweets
    2) save those tweets to the db and their sentiment
    3) retrieve a certain number of recent tweets from db.
    3)
    :param name:
    :return:
    """
    print(name)

    # Retrieve tweets
    url = create_url()
    try:
        global tweets
        tweets = [] #: List[Dict[str,str]]
        tweets = connect_to_endpoint(url)
    except Exception as err:
        print(f"Error retrieving tweets: {err}")

    # Save to db:
    # for tweet in tweets:
    #     insert("")
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except:
        print(e)

    cur = conn.cursor()
    cur.execute("CREATE TABLE tweets(id, text)")
    for tweet in tweets:
        # tweet is the form {"id":"12312", "text":"Hello!"} tweet["id"] tweet["text"]
        cur.execute("""
        INSERT INTO tweets VALUES
            (?, ?)
        """, [tweet["id"], tweet["text"]])

    # TODO: retrieve again
    print('Num tweets:', len(tweets))

    return render_template("index.html", content=tweets)#data)

@app.route("/aboutUs")
def about():
    return render_template("aboutUs.html")


if __name__ == "__main__":
    load_dotenv()


    app.run(debug=True)
