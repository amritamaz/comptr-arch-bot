from bs4 import BeautifulSoup
import requests
from twython import Twython

import random

APP_KEY = 'ZManrilCBbut2rqgNnrHcPROk'
APP_SECRET = '9cTA1tKvMRoHPLrWla0VMwwNrxWRF488MbQd3ahJbaxuEtbuRU'
twitter = Twython(APP_KEY, APP_SECRET)
OAUTH_TOKEN = '2897787816-JoTwMLISEKkh87ZynvLjAa7Sn0cpMP9ExfZNVq8'
OAUTH_TOKEN_SECRET = 'ic9EassOE0XlTKZ8KPsrg9QeCOc2xQlaIg3JuBM7oGANS'

page = requests.get('https://www.udacity.com/wiki/ud233/glossary')
soup = BeautifulSoup(page.content)
words = [n.text[:-1] for n in soup.find_all('strong')]

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
        

