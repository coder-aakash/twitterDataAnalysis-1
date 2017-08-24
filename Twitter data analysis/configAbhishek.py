import tweepy

consumer_key = 'TkqbhnsKDab4Y4gyi4p5xsydb'
consumer_secret = 'tpqe0Dr0aCwxOEFZBbs0vi6CPs8um2UeZ38xOZvkuk8baTSwMX'
access_token = '734128691001872384-GdrUdbHeI6fHUiXIymRWSlHlxdYvvYI'
access_token_secret = 'nRtr4RR2ABSlRu8yq4CmpOlLY6h2NNcWVJrJIwH27WnWM'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
