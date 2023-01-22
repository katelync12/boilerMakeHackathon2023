from typing import List

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from nltk.tokenize import sent_tokenize
from statistics import mean


def setup():
    nltk.download('vader_lexicon') #TODO: setup script.

# [nltk_data] Downloading package vader_lexicon to
# [nltk_data]     C:\Users\sean1\AppData\Roaming\nltk_data...
# True


def get_tweet_sentiment(tweet: str) -> int:
    """
    Averages sentences, returns composite score of tweet.
    :param tweet:
    :return: Composite score of tweet
    """
    tweet_sentences = sent_tokenize(tweet)
    sid = SentimentIntensityAnalyzer() # When this errors out, run setup()
    sentence_compound_scores: List[int] = []
    for sent in tweet_sentences:
        scores = sid.polarity_scores(sent)
        sentence_compound_scores.append(scores['compound'])
    total_tweet_score = mean(sentence_compound_scores)
    return total_tweet_score
# {'neg': 0.0, 'neu': 0.834, 'pos': 0.166, 'compound': 0.2944}


if __name__ == "__main__":
    tweet = "Roger Dodger is one of the most compelling variations on this theme. Roger Dodger is one of the most compelling variations on this theme.Roger Dodger is one of the most compelling variations on this theme."
    # setup()
    print(get_tweet_sentiment(tweet))