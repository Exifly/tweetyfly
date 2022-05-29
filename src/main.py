import requests
import os
import time
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


def get_last_tweet_id():
    # - Get desc sorted list of tweet id - #
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

    return [id['id'] for id in resp['data']]


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
        print(f"Tweet N {id} succesfully retweeted.")
    else:
        print(f"Tweet N {id} not retweeted")


print("Bot Start")
while True:
    tweet_id_list = []
    tweet_id_list = get_last_tweet_id()
    retweet(tweet_id_list[0])
    time.sleep(5)
