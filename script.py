from bs4 import BeautifulSoup
import requests
from twython import Twython

import random

APP_KEY = 'xxxx'
APP_SECRET = 'xxxx'
twitter = Twython(APP_KEY, APP_SECRET)
OAUTH_TOKEN = 'xxxx'
OAUTH_TOKEN_SECRET = 'xxxx'

# boring udacity list
page = requests.get('https://www.udacity.com/wiki/ud233/glossary')
soup = BeautifulSoup(page.content)
words = [n.text[:-1] for n in soup.find_all('strong')]

#more robust patterson-hennesy list
with open('words-thin.txt') as f:
    words = words + [x.strip('\n') for x in f.readlines()]

while True:
    word = random.choice(words)
    if 'cache' in word or 'coherence' in word:
        tweet = "i love %s - @siderealed" % word
    elif 'approx' in word:
        tweet = "i love %s - @samps" % word
    else:
        tweet = "i love %s" % word

    print tweet
    do_it = raw_input('do it? y/n: ')
    if do_it == "y":
        twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        twitter.update_status(status=tweet)
        print "that's so cool"
        

