from requests_oauthlib import OAuth1
from dotenv import load_dotenv
import requests
import os


load_dotenv()


# - GET GLOBAL KEYS TO MAKE REQUESTS - #
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
API_SECRET = os.getenv("API_SECRET")
CLIENT_ID = os.getenv("CLIENT_ID")
USER_ID = os.getenv("MY_USER_ID")
API_KEY = os.getenv("API_KEY")
BEARER = os.getenv("BEARER")
APP_ID = os.getenv("APP_ID")


auth = OAuth1(
    # - This object is required to call like and retweet api - #
    client_key=API_KEY,
    client_secret=API_SECRET,
    resource_owner_key=ACCESS_TOKEN,
    resource_owner_secret=ACCESS_SECRET
)


def retrive_latest_tweet_api():
   # - Get desc sorted list of tweets text and id - #
   response = requests.get(
      "https://api.twitter.com/2/tweets/search/recent",

      headers={'Authorization': 'Bearer {}'.format(BEARER)},

      params={
         "query": "#coding",  # arguments to find in tweet texts
         "max_results": 10,
         "sort_order": "recency"
      }
   )
   return response


def retweet_api(tweet_id):
    # - Retweet by tweet id- #
   response = requests.post(
      f"https://api.twitter.com/2/users/{USER_ID}/retweets",

      auth=auth,

      json={"tweet_id": tweet_id}
   )
   return response


def like_api(tweet_id):
    # - Like by tweet id- #
   response = requests.post(
      f"https://api.twitter.com/2/users/{USER_ID}/likes",

      auth=auth,

      json={"tweet_id": tweet_id}
   )
   return response
   
def get_profile(profile_id):
   response = requests.get(
      f"https://api.twitter.com/2/users/{profile_id}/tweets",

      headers={'Authorization': 'Bearer {}'.format(BEARER)},
   )
   return response