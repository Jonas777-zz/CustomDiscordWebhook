#!/usr/bin/env python3
import requests
import twitter
import sys
from twitter import *

def update(acc, verbose, update):
	t = Twitter(auth=OAuth('381112053-BQEtXSOpebuGnX1fa1dVNdAcWgkrYTnspp8hFVbe',
							'LxYx6DZej6cePuO6Gmovqw4eYotqEjPlOKF0QcuzIHLv1',
							'eT7B0SZQrotxuJ385joCMZ8Z6',
						   	'741wIEGOqmjTbd36eAc1wcRU9ddyqhMy4yvjvbEhw9e2t4Jpuz'
						   	))

	tl = t.search.tweets(q="from:@" + acc + " -filter:replies", result_type="recent", count="5")

	with open('recent_tweets', 'r+') as f:
		f.seek(0)
		for twit in tl['statuses']:
			if verbose == '1':
				print(twit['id_str'])
			if update == '1':
				f.write(twit['id_str'] + '\n')
		f.truncate()

if __name__ == '__main__':
	try:
		update(sys.argv[1], sys.argv[2], sys.argv[3])
	except:
		print("Usage: getlastten.py -username -verboseflag -updatefileflag")
		pass