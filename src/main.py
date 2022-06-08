#!/usr/bin/env python3

from tweet_api import *

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
