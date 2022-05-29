## TODO Retweeter and references

API Endpoint:
https://api.twitter.com/2/tweets/search/recent


Query parameter:
#python3, #programming, 


## TODO

* [+] Ottenere code verifier
* [+] Ottenere client id
* [+] Ottenere acces_token (id user tweeter) da API
* [+] Filtrare Response Json dal tweet piu recente
* [+] Ottenere l'id del tweet piu recente
* [] Invocare API per mettere like al tweet piu recente tramite id
* [+] Invocare API per retweettare il tweet piu recente tramite id

## Machine Learning TODO
### Using TextBlob to reconyze some words in tweets to avoid spam retweets

* [] Importare Textblob
* [] Associare ad ogni testo(tweet) il proprio ID
* [] Parsare il testo per ottenere le singole parole
* [] Retweet solo se il testo non contiene determinate parole
    * [] Retweet anche se il sentiment analysis è positivo (opzionale)