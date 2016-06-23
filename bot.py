import tweepy
import random
from secrets import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

r = lambda: random.randint(0,255)
foo = ['Hey, try this hex code: ', 'Hi, looking for a new color? Try this one: ', 'What are you up to? Want to try a new color? Try this one: ', 'Heya, try this hex code: ', 'Howdy, take this hex code for a spin: ', 'Well hello! Get some inspiration with this hex code: ', 'Yo, here\'s a color for you to try: ']
api.update_status(random.choice(foo) + '#%02X%02X%02X' % (r(),r(),r()))