import re
from typing import List, Dict
import trending
import name_check
import recent_tweets
import sentiment

if __name__ == "__main__":
    # 1) Webdriver scrape twitter
    source: str = trending.get_source_with_webdriver()
    topics: List[str] = trending.get_trending(source)

    # 1.5) Find the trending *names*
    people: List[str] = name_check.get_people(topics, debug=False)

    # 2) With names, use 2/tweets/search/recent to find 100s of tweets
    #    about each person.
    person_tweets: Dict[str, str] = {}
    # form {"Kanye":[ {'text':'ye sux','id':'1'},{'text':'ye good','id':'2'} ]}
    for person in people:
        tweets: List[Dict[str, str]] = recent_tweets.search(person, 10)
        person_tweets[person] = tweets

    # 3) Sentiment analyze each tweet

        # still for one person
        for tweet in tweets:
            # strip unicode
            tweet['text'] = re.sub(pattern=r'[^\x00-\x7F]+',
                                   repl='',
                                   string=tweet['text'])
            tweet_sentiment = sentiment.get_tweet_sentiment(tweet['text'])
            print('Person:', person, 'Sentiment:', tweet_sentiment, 'Tweet:', tweet['text'].replace('\n'))
