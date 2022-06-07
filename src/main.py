from requests_oauthlib import OAuth1
from dotenv import load_dotenv
from textblob import TextBlob
from termcolor import colored
import requests
import datetime
import random
import time
import os


load_dotenv()


# - GET GLOBAL KEYS TO MAKE REQUESTS - #
API_SECRET = os.getenv("API_SECRET")
API_KEY = os.getenv("API_KEY")
BEARER = os.getenv("BEARER")
APP_ID = os.getenv("APP_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")


auth = OAuth1(
    client_key=API_KEY,
    client_secret=API_SECRET,
    resource_owner_key=ACCESS_TOKEN,
    resource_owner_secret=ACCESS_SECRET
)


def get_last_tweet_id_and_text():
    # - Get desc sorted list of tweets text and id - #
    header = {'Authorization': 'Bearer {}'.format(BEARER)}

    query = {
        "query": "#programming",
        "max_results": 10,
        "sort_order": "recency"
    }

    resp = requests.get(
        "https://api.twitter.com/2/tweets/search/recent", headers=header, params=query)

    if resp.status_code == 200:
        resp = resp.json()
    else:
        print(
            f"[{date()}] Error requesting tweets api STATUS_CODE = {resp.status_code}")

    tweets = [{"id": el['id'], "text": el['text']} for el in resp['data']]

    return tweets


def retweet(id):
    # - Retweet by id and user id - #
    payload = {"tweet_id": id}

    user_id = os.getenv("MY_USER_ID")
    resp_2 = requests.post(
        f"https://api.twitter.com/2/users/{user_id}/retweets", auth=auth, json=payload)

    if resp_2.status_code == 200:
        resp_2 = resp_2.json()
        if (resp_2['data']['retweeted']):
            print(f"[{date()}] Tweet N {id} succesfully retweeted.")
        else:
            print(f"[{date()}] Tweet N {id} not retweeted")
    else:
        print(
            f"[{date()}] Error ivoking retweet api STATUS_CODE = {resp_2.status_code}")


def analyze_text(tweets):
    bad_words = ["course", "crash course", "ads",
                 "cash", "sponsor", "freelancer", "pay", "payd", "price", "USD",
                 "client:", "freelance", "freelancer", "assistance", "homework",
                 "exam", "exams", "pay", "us", "job", "free", "need", "helping",
                 "we", "do", "help", "stuck", "homework", "bot", "crypto", "finance", "budget",
                 "class", "classes", "room"]

    checked_id = 0
    counter = 0

    for text in tweets:
        # print(f"[{date()}] Checked Tweet N {counter}")
        blob = TextBlob(text=text['text'])
        print(f"[{text['id']}] {text['text']}")
        count_list = 0
        blob_len = len(blob.words)
        for x in blob.words.lower():
            if x not in bad_words:
                count_list += 1
                if count_list == blob_len:
                    print([{date()}], colored(
                        f"Oh, that's a good one!", 'green'))
                    return checked_id
            else:
                print([{date()}], colored(
                    f"Tweet with id {text['id']} is not good..\n", 'red'))
                counter += 1
                break


def like(id):
    body = {"tweet_id": id}
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


if __name__ == "__main__":
    print(f"[{date()}] Bot Start")

    while True:
        delay = random.randint(60, 180)
        print(f"[{date()}] Delay: {delay}")
        tweet_id_list = []
        tweets_list = {}
        tweets_list = get_last_tweet_id_and_text()
        checked_id = analyze_text(tweets=tweets_list)
        # like(checked_id)
        # retweet(checked_id)
        print("\n")
        time.sleep(5)
