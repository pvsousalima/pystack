#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time
from myconfig import *
from tweepy.error import TweepError
from funny import get_funny_phrase_pt, get_funny_phrase_en
from collect import collect_rates
from random import choice

# OAuth process, using the keys and tokens (add you own keys to a 'myconfig.py file')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def update_status(status):
    u''' Update user's status on twitter'''
    #api.update_status(status=status)
    print('Status updated: {}]\n{} char\n'.format( status, len(status)))


rates = [x/10 for x in range(39, 40, 45)]

def main():
    u''' Main function '''

    while True: 
        
        # get rates
        #rate = collect_rates()
        rate = choice(rates)

        # random pickups of phrases in english and pt
        mychoice = choice(['pt', 'en'])

        # choose between pt and eng and updates it
        if mychoice == 'en':
            update_status('1 USD = {} BRL. {}'.format(rate, get_funny_phrase_en()))        
        elif mychoice == 'pt':
            update_status('1 USD = {} BRL. {}'.format(rate, get_funny_phrase_pt()))

        # Waits for five minute
        time.sleep(0.2)


if __name__ == '__main__':
    main()
