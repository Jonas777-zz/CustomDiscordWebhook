#!/usr/bin/env python3
import requests
import twitter
import getlatest
from twitter import *

def twitter_stuff():
	t = Twitter(auth=OAuth('381112053-BQEtXSOpebuGnX1fa1dVNdAcWgkrYTnspp8hFVbe',
							'LxYx6DZej6cePuO6Gmovqw4eYotqEjPlOKF0QcuzIHLv1',
							'eT7B0SZQrotxuJ385joCMZ8Z6',
						   	'741wIEGOqmjTbd36eAc1wcRU9ddyqhMy4yvjvbEhw9e2t4Jpuz'
						   	))

	tl = t.search.tweets(q="from:@metaphorminute -filter:replies", result_type="recent", count="5")

	# print(tl.keys())
	# print(tl['statuses'][1]['text'])

	#last 5 tweets from last time we checked
	with open('recent_tweets', 'r') as f:
		old_tweets = f.read().splitlines()

	#check the newest 5 recent tweets
	new_tweets = [tl['statuses'][x]['id_str'] for x in range(5)]

	#if the old newest tweet (line 0) isn't still the newest, update recent_tweets
	#need to find how many new tweets as well
	if old_tweets[0] != new_tweets[0]:
		print("new tweet!!!!!")
		if new_tweets.count(old_tweets[0]) == 0:
			print("more than 5 tweets have happened since the last check. only the 5 most recent tweets will be posted.")
			num_tweets = 5
		else:
			num_tweets = new_tweets.index(old_tweets[0])
		getlatest.update('metaphorminute', '0', '1')
		print("beginning num_tweets: " + str(num_tweets))
		for i in range(num_tweets):
			print("getting tweet: " + str(num_tweets - i - 1))
			push_to_discord(tl['statuses'][num_tweets - i - 1]['text'])	#push the first x new tweets where x = how many lines the old newest tweet got pushed back
	else:
		print("no updates!")

def push_to_discord(content):
	hook_url = 'https://discordapp.com/api/webhooks/439251244008341515/9ZTzbymSZT-JjEeAGGkApYHZgxnGV6GbQEcxXqKPzjsQ-y9ajNJv6WlQT1Zves1z4Aey'

	print(content)

	data = {
		"content": "" + content
	}

	requests.post(hook_url, data=data)

if __name__ == '__main__':
	twitter_stuff()