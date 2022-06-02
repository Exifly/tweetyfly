from re import I
import requests
import os
import time
import random
import datetime
from textblob import TextBlob
from dotenv import load_dotenv
from requests_oauthlib import OAuth1

load_dotenv()

# - GET GLOBAL KEYS TO MAKE REQUESTS - #
API_SECRET = os.getenv("API_SECRET")
API_KEY = os.getenv("API_KEY")
BEARER = os.getenv("BEARER")
APP_ID = os.getenv("APP_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")


def get_last_tweet_id_and_text():
    # - Get desc sorted list of tweets text and id - #
    id_list = []
    tweets = {}
    tweet = []

    header = {
        'Authorization': 'Bearer {}'.format(BEARER)
    }

    query = {
        "query": "#programming",
        "max_results": 10,
        "sort_order": "recency"
    }

    resp = requests.get(
        "https://api.twitter.com/2/tweets/search/recent", headers=header, params=query).json()

    id_list = [id['id'] for id in resp['data']]
    for el in resp['data']:
        tweet.append({"id": el['id'], "text": el['text']})

    tweets = {"tweets": tweet}

    # print(tweets)
    return id_list, tweets


def retweet(id):
    # - Retweet by id and user id - #
    payload = {
        "tweet_id": id
    }

    auth = OAuth1(
        client_key=API_KEY,
        client_secret=API_SECRET,
        resource_owner_key=ACCESS_TOKEN,
        resource_owner_secret=ACCESS_SECRET
    )

    user_id = os.getenv("MY_USER_ID")
    resp_2 = requests.post(
        f"https://api.twitter.com/2/users/{user_id}/retweets", auth=auth, json=payload).json()

    if (resp_2['data']['retweeted']):
        print(f"[{date()}] Tweet N {id} succesfully retweeted.")
    else:
        print(f"[{date()}] Tweet N {id} not retweeted")


def analyze_text(tweets):
    bad_words = ["course", "crash course", "ads",
                 "cash", "sponsor", "freelancer", "pay", "payd", "price", "USD",
                 "client:", "freelance", "freelancer", "assistance", "homework",
                 "exam", "exams", "pay", "us", "job", "free", "need", "helping",
                 "we", "do", "help", "stuck", "homework", "bot", "crypto", "finance", "budget",
                 "class", "classes", "room"]

    checked_id = 0
    counter = 0

    for text in tweets['tweets']:
        print(f"[{date()}] Checked Tweet N {counter}")
        blob = TextBlob(text=text['text'])
        print(f"[{text['id']}] {blob.words.lower()}")
        blob_words = blob.words.lower()

        count_list = 0
        blob_len = len(blob_words)
        for x in blob_words:
            if x not in bad_words:
                count_list += 1
                if count_list == blob_len:
                    print(f"[{date()}] Oh, that's a good one!")
                    checked_id = text['id']
                    print(f"[{date()}] Checked ID -->> {checked_id}")
                    return checked_id
            else:
                print(f"[{date()}] Tweet with id {text['id']} is not good..")
                counter += 1
                break


def like(id):
    body = {
        "tweet_id": id
    }

    auth = OAuth1(
        client_key=API_KEY,
        client_secret=API_SECRET,
        resource_owner_key=ACCESS_TOKEN,
        resource_owner_secret=ACCESS_SECRET
    )

    user_id = os.getenv("MY_USER_ID")
    resp = requests.post(
        f"https://api.twitter.com/2/users/{user_id}/likes", auth=auth, json=body)
    if (resp.status_code == 200):
        resp_parsed = resp.json()
        print(f"[{date()}] Oooohhh, Tweet {id} Liked!!\n", resp_parsed)
        return
    else:
        print(f"[{date()}] Error during like request API!")


def date(): return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


print(f"[{date()}] Bot Start")

while True:
    delay = random.randint(60, 180)
    print(f"[{date()}] Delay: {delay}")
    tweet_id_list = []
    tweets_list = {}
    tweet_id_list, tweets_list = get_last_tweet_id_and_text()
    checked_id = analyze_text(tweets=tweets_list)
    like(tweet_id_list[0])
    retweet(tweet_id_list[0])
    print(" ")
    time.sleep(delay)
