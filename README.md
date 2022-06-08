# TweetyFly

Welcome in our retweeter bot!

## Dependencies
First, you need to create a python environment:
```
python -m venv env
```

Activate it with:
> source env/bin/activate

Install Dependencies declared in **requirements.txt**:
```
pip install -r requirements.txt
```

To run this bot you will also need the NTLK_DATA, just type this command:
```
python -m textblob.download_corpora
```

## API Key
You'll need Api Keys to run this bot.
To get all api keys, just register on Twitter Developer portal and follow istrunctions.

## Configuration
Rename **.env.sample** in **.env**, then fill the content with your keys and save.

## Execution
To run the bot in MacOS and Linux terminal just type:
```
python src/main.py >> bot.log &
```

In Windows it's same:
```
python src\main.py >> bot.log
```