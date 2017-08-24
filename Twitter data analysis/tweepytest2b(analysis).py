#%matplotlib notebook
import json
import pandas as pd
import matplotlib.pyplot as plt
from csv import DictWriter
tweets_data=[]
tweets_data_path='C:\\Users\\pavilion\\AppData\\Local\\Programs\\Python\\Python36-32\\twitter project\\testdata2.txt'

tweets_file=open(tweets_data_path,'r')
database=open("tweetsforlang1.csv",'w')
tweets_file.seek(0)
tweet=dict()
for line in tweets_file:
    try:
        tweet=json.loads(line)
        tweets_data.append(tweet)
    
        # print(str(i)+". "+t['text'])
        #print("lang:"+t['lang'])
        # print("countrty:"+tweet["place"]["country"])
    except:
       # print("try fail")
        continue
writer = DictWriter(database, tweet.keys())
writer.writeheader()
#writer.writerows(tweet)
tweets_file.close()
database.close()

print("There are "+ str(len(tweets_data))+" tweets collected in the file")

#next we will structure the tweers data into a pandas DataFrame to simplify
#the manipulation
tweets=pd.DataFrame()
#empty data frame

#add 3 columns to the tweets DataFrame called text,lang and country.
#Text: column contains the tweet
#lang:language in which te tweet was written
#country:country from where the tweet was sent

tweets["text"]=list(map(lambda tweet: tweet["text"],tweets_data))
tweets["lang"]=list(map(lambda tweet: tweet["lang"],tweets_data))
tweets["country"]=list(map(lambda tweet: tweet["place"]["country"] if tweet["place"]!=None else None,tweets_data))

#create 2 charts
#one for top 5 languages in which the tweets were written
#second, the top 5 countries from which the tweets were sent

tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
