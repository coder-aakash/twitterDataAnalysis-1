import time
import re
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import sys
sys.path.append(r'C:\Users\pavilion\twitter project')
import configAakash

" ## coding utf-8"

def calctime(a):
    return time.time()-a


def word_match(word,text):
    if re.search(word.lower(),text.lower()):
        return True
    else:
        return False

pos=0
neg=0
comp=0

count =0
initime=time.time()
plt.ion()

ckey=configAakash.ckey
csecret=configAakash.csecret
atoken=configAakash.atoken
asecret=configAakash.asecret

class listener(StreamListener):

    def on_data(self, data):
        global initime
        t=int(calctime(initime))
        tweet_data=json.loads(data)
        if 'text' not in tweet_data:
            print("HULLLA HOOOOO!!!!")
            coninue;
        tweet=tweet_data["text"]
        
        tweet=" ".join(re.findall("[a-zA-Z]+",tweet))
        blob=TextBlob(tweet.strip())
        global pos
        global neg
        global comp
        global count
        count=count+1
        senti=0
        for sen in blob.sentences:
            senti=senti+sen.sentiment.polarity
            if sen.sentiment.polarity >= 0:
                pos=pos+sen.sentiment.polarity
            else:
                neg=neg+sen.sentiment.polarity

        comp=comp+senti
        print("count: "+str(count))
        print("tweet:: "+str(tweet.strip()))
        print("sentiment variable::"+str(senti))
        print(t) 
        print("posituve::"+str(pos)+" negative::"+str(neg)+" Overall::"+str(comp))



        plt.axis([0,700, -50,50])
        plt.xlabel('Time')
        plt.ylabel('Sentiment')
        plt.plot([t],[pos],'go',[t],[neg],'ro',[t],[comp],'yo')
        plt.show()
        plt.pause(0.0001)
        if count==500:
            return False
        else:
            return True

    def on_error(self,status):
        print("ERROR!!!!!!!!!!!!!:::"+str(status)+" >>>>>")


auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

twitterStream= Stream(auth,listener(count))
twitterStream.filter(languages=["en"],track=["gst"])
