import nltk
import ujson
import fnmatch
from bz2 import BZ2File as bzopen
import os

data = [os.path.join(dirpath, f)
        for dirpath, dirnames, files in os.walk(path)
        for f in fnmatch.filter(files, '*.bz2')]

    
def parse_tweet(t):
        row = {}
        try:
                lang = t['lang']
        except:
                lang = t['user']['lang']
        text = t['text'].replace('\n', ' ').replace(",", ' ').encode('utf-8')
        try:
                hasht = t['entities']['hashtags'][0]['text']
        except:
                hasht = ''
        try:
                followers = t['user']['followers_count']
                utc = t['user']['utc_offset']
        except:
                followers = None
                utc = ''
        try:
                retw = t['retweeted']
        except:
                retw = False
        row = {'id_str': t['id_str'], 'created_at': t['created_at'], 'utc_offset': utc,
                'favorited': t['favorited'], 'retweeted': retw, 'retweet_count': t['retweet_count'],
                'hashtags': hasht, 'lang': lang, 'followers_count': followers,  'text': text}
        return(row)

def clean_tweets(filelist, docfilepath, encode_html=True):
        for f1 in filelist:
            with open(docfilepath, 'a') as fp:
                with bzopen(f1, "r") as f:
                    try:
                            for line in f:
                                    try:
                                            row=parse_tweet(ujson.loads(line))
                                            ujson.dump(row, fp, encode_html_chars=encode_html)
                                            fp.write('\n')
                                    except:
                                            continue
                                       
                    except:
                            print("failed file")
    


numfiles = 10
dt = len(data)
nfilesin = dt/numfiles
for i in range(numfiles)[:]:
        start = int(nfilesin*i)
        end = int(nfilesin*(i+1))
        print("start: ", str(start), "end: ", str(end))
        outfilename = pathout  + str(i)+ ".json"
        clean_tweets(data[start:end], outfilename, encode_html=True)

print("Done.")
