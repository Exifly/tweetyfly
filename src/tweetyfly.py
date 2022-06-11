#!/usr/bin/env python3

from googletrans import Translator
from os import get_terminal_size
from textblob import TextBlob
from termcolor import colored
from textwrap import wrap
import datetime
import random
import time
import api


def start(min_delay, max_delay):
    print(f"[{date()}] Bot Started")
    while True:
        delay = random.randint(min_delay, max_delay)
        tweets_list = retrive_latest_tweets()
        checked_id = analyze_text(tweets=tweets_list)
        # like(checked_id)
        # retweet(checked_id)
        print("\n")
        time.sleep(delay)


def retrive_latest_tweets():
    # - Get desc sorted list of tweets text and id - #
    response = api.retrive_latest_tweet_api()

    if response.status_code == 200:
        response = response.json()
    else:
        print(f"[{date()}] Error requesting tweets api STATUS_CODE = {response.status_code}")

    # - return a list of tweet object made of: {id: <id>, tweet: <text>}, used to bind tweet ID with associated text - #
    return [{"id": tweet['id'], "text": tweet['text']} for tweet in response['data']]


def retweet(tweet_id):
    # - Retweet by id and user id - #
    response = api.retweet_api(tweet_id)

    if response.status_code == 200:
        response = response.json()
        # - if retweets api return retweeted: true - #
        if (response['data']['retweeted']):
            print(f"[{date()}] Tweet N {tweet_id} succesfully retweeted.")
        else:
            print(f"[{date()}] Tweet N {tweet_id} not retweeted")
    else:
        print(
            f"[{date()}] Error ivoking retweet api STATUS_CODE = {response.status_code}")


def analyze_text(tweets):
    bad_words = get_bad_words()
    for tweet in tweets:
        if not is_english(tweet['text']):
            break

        print('┏', colored(f"Tweed id: {tweet['id']}", 'green', attrs=['bold']), '\n┃')
        print("┃\t", colored(f"Date: ", 'cyan',
              attrs=['bold']), f"\n┃\t\t {date()}")
        tweet_text = TextBlob(text=tweet['text'])
        termsize = get_terminal_size()
        wrapped_description = wrap(tweet['text'], termsize.columns - 50)
        print('┃', colored(f"\t Text:", 'cyan', attrs=['bold']))
        for line in wrapped_description:
            print("┃\t\t" + line)

        for index, word in enumerate(tweet_text.words.lower()):
            if word not in bad_words:
                if index + 1 == len(tweet_text.words):
                    print('┃', colored(f"\t Result:", 'cyan', attrs=['bold']))
                    print('┗', colored(f"\t\tOh, that's a good one!", 'green'))
                    return tweet['id']
            else:
                print('┃', colored(f"\t Result:", 'cyan', attrs=['bold']))
                print('┗', colored(
                    f"\t\tTweet with id {tweet['id']} is not good..\n", 'red'))
                break


def like(tweet_id):
    response = api.like_api(tweet_id)

    if (response.status_code == 200):
        response = response.json()
        return print(f"[{date()}] Oooohhh, Tweet {tweet_id} Liked!!\n", response)
    else:
        return print(f"[{date()}] Error during like request API!")


# - Inline function to get sysdate date - #
def date(): return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_bad_words():
    try:
        with open("badwords.txt") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(
            f"[{date()}] File badwords.txt not found, please insert or create one in src/badwords.txt\n")
        return []


def is_english(text):
    detector = Translator()
    dec_lan = detector.detect(text)
    return dec_lan.lang == "en"
