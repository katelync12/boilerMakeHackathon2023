import re
import sqlite3
from typing import List, Dict, Tuple
import trending
import name_check
import recent_tweets
import sentiment
import process_tweet
e = "Couldn't connect to db."
db_file = 'tweets.db'



def get_tweets() -> List[Tuple[str, float, List[str]]]:
    """Return list of tuples containing tweet info"""
    # 1) Webdriver scrape twitter
    source: str = trending.get_source_with_webdriver()
    topics: List[str] = trending.get_trending(source)

    # 1.5) Find the trending *names*
    people: List[str] = name_check.get_people(topics, debug=False)

    # 2) With names, use 2/tweets/search/recent to find 100s of tweets
    #    about each person.
    person_tweets: Dict[str, str] = {}
    # form {"Kanye":[ {'text':'ye sux','id':'1'},{'text':'ye good','id':'2'} ]}
    all_tweets_info: List[Tuple[str, float, List[str]]] = []
    for person in people:
        tweets: List[Dict[str, str]] = recent_tweets.search(person, 10)
        person_tweets[person] = tweets

    # 3) Sentiment analyze each tweet

        # still for one person
        for tweet in tweets:
            # # strip unicode
            # tweet['text'] = re.sub(pattern=r'[^\x00-\x7F]+',
            #                        repl='',
            #                        string=tweet['text'])
            content = tweet['text']
            tweet_sentiment = sentiment.get_tweet_sentiment(content)
            content = process_tweet.clean_unicode_links(content)
            handles = process_tweet.get_handles(content)
            print('Person:', person,
                  'Sentiment:', tweet_sentiment,
                  'Handles:', handles,
                  'Tweet:', content.replace('\n', ''))
            one_row: Tuple[str, float, List[str]] = (person, tweet_sentiment, handles)
            all_tweets_info.append(one_row)
    return all_tweets_info


def anushkas_code(all_tweets: List[Tuple[str, float, List[str]]]) -> None:
    """Write all_tweets to the db"""
    try:
        conn = sqlite3.connect(db_file)
    except:
        print(e)

    cur = conn.cursor()
    
    cur.execute("CREATE TABLE trending(name, count REAL, sas REAL, handles)")

    for trendTweet in all_tweets:
        # tweet is the form [("name", sas, ["@tags"]), ("name", sas, ["@tags"]), "name", sas, ["@tags"]]
        res = cur.execute("""
            SELECT name FROM trending WHERE name==?
            """, [trendTweet[0]])
    
    # print(trendTweet)
        res1 = res.fetchall()
    # print(res1)
        if len(res1)==0:
            cur.execute("""INSERT INTO trending VALUES
                (?, 1, ?, ?);
            """, [trendTweet[0], trendTweet[1], str("".join(trendTweet[2]))])
        else:
            cur.execute("""UPDATE trending
            SET count = count + 1, sas = sas + ?, handles = (handles || ?)
            WHERE name==?;
            """, [trendTweet[1], str("".join(trendTweet[2])), trendTweet[0]])
        conn.commit()
        
    cur.close()
    conn.close()

if __name__ == "__main__":
    tweet_list = get_tweets()
    anushkas_code(tweet_list)
