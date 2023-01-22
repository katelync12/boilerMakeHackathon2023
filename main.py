from collections import Counter

from flask import Flask, redirect, url_for, render_template
from sampledstream import create_url, connect_to_endpoint
from dotenv import load_dotenv
import get_users_with_bearer_token
import json
import sqlite3
from typing import Dict, List
db_file = 'tweets.db'
e = "Couldn't connect to db."


app = Flask(__name__, static_folder="css")


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

    # # Retrieve tweets
    # url = create_url()
    # try:
    #     global tweets
    #     tweets = [] #: List[Dict[str,str]]
    #     tweets = connect_to_endpoint(url)
    # except Exception as err:
    #     print(f"Error retrieving tweets: {err}")

    # Save to db:
    # for tweet in tweets:
    #     insert("")

    # try:
    #     conn = sqlite3.connect(db_file)
    #     print(sqlite3.version)
    # except:
    #     print(e)
    #
    # cur = conn.cursor()
    #
    # # cur.execute("CREATE TABLE tweets(id, text)")
    # for tweet in tweets:
    #     # tweet is the form {"id":"12312", "text":"Hello!"} tweet["id"] tweet["text"]
    #     cur.execute("""
    #     INSERT INTO tweets VALUES
    #         (?, ?)
    #     """, [tweet["id"], tweet["text"]])
    #
    # conn.commit()
    # retrieve = cur.execute("SELECT id, text FROM tweets")
    # retrieveList = retrieve.fetchall()
    #
    # # TODO: retrieve again
    # print('Num tweets:', len(tweets))
    # conn.close()
    #
    # username = "taylorswift13"
    #
    # for word in retrieveList:
    #     if "@" in word[1]:
    #         tweetList = word[1].split()
    #         for word in tweetList:
    #             if word.startswith("@"):
    #                 username = word
    #                 username = username.replace("@", "")
    #                 username = username.replace(":", "")
    #                 username = username.replace("-", "")
    #                 break


    conn = sqlite3.connect(db_file)

    try:
        cur = conn.cursor()

        res = cur.execute("""
                SELECT name, count, sas, handles FROM trending
                """)
        res1 = res.fetchall()

        rankTable = []
        for i in range(len(res1)):
            print("res1: ", res1[i])
            sublist = list()
            sublist.append(res1[i][0])  # name
            ats = filter(None, res1[i][3].split('@'))
            counter = Counter(ats)  # hash map for hashtags
            print("counter", counter)
            sublist.append('@' + counter.most_common(1)[0][0])  # most common hashtag
            print(counter.most_common(1))
            sublist.append(res1[i][2] / res1[i][1])
            rankTable.append(sublist)
        rankTable = sorted(rankTable, key=lambda x: x[2], reverse=True)
    finally:
        cur.close()
        conn.close()

    username = rankTable[0][1][1:]
    image_url = get_users_with_bearer_token.create_url(username)
    get_image = get_users_with_bearer_token.connect_to_endpoint(image_url)
    # image = json.dumps(get_image, indent=4, sort_keys=True)
    image = get_image['data'][0]['profile_image_url']

    return render_template("index.html", content=rankTable, image=image, username=username)#data)


@app.route("/random")
def random():
    """
    Workflow:
    1) retrieve a certain number of recent tweets
    2) save those tweets to the db and their sentiment
    3) retrieve a certain number of recent tweets from db.
    3)
    :param name:
    :return:
    """

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
    
    # cur.execute("CREATE TABLE tweets(id, text)")
    for tweet in tweets:
        # tweet is the form {"id":"12312", "text":"Hello!"} tweet["id"] tweet["text"]
        cur.execute("""
        INSERT INTO tweets VALUES
            (?, ?)
        """, [tweet["id"], tweet["text"]])

    conn.commit()
    retrieve = cur.execute("SELECT id, text FROM tweets")
    retrieveList = retrieve.fetchall()

    # TODO: retrieve again
    print('Num tweets:', len(tweets))
    conn.close()

    username = "taylorswift13"

    for word in retrieveList:
        if "@" in word[1]:
            tweetList = word[1].split()
            for word in tweetList:
                if word.startswith("@"):
                    username = word
                    username = username.replace("@", "")
                    username = username.replace(":", "")
                    username = username.replace("-", "")
                    break

    image_url = get_users_with_bearer_token.create_url(username)
    get_image = get_users_with_bearer_token.connect_to_endpoint(image_url)
    # image = json.dumps(get_image, indent=4, sort_keys=True)
    image = get_image['data'][0]['profile_image_url']

    return render_template("random.html", content=retrieveList, image=image, username=username)



@app.route("/aboutUs")
def about():
    return render_template("aboutUs.html")


if __name__ == "__main__":
    load_dotenv()


    app.run(host='0.0.0.0',debug=False)
