#!/usr/bin/env python3
import requests
import twitter
from twitter import *

t = Twitter(auth=OAuth('381112053-BQEtXSOpebuGnX1fa1dVNdAcWgkrYTnspp8hFVbe',
						'LxYx6DZej6cePuO6Gmovqw4eYotqEjPlOKF0QcuzIHLv1',
						'eT7B0SZQrotxuJ385joCMZ8Z6',
					   	'741wIEGOqmjTbd36eAc1wcRU9ddyqhMy4yvjvbEhw9e2t4Jpuz'
					   	))

tl = t.search.tweets(q="from:@BetaEFT -filter:replies", result_type="recent", count="3")

print(tl.keys())

print(tl['statuses'][1]['text'])

hook_url = 'https://discordapp.com/api/webhooks/439251244008341515/9ZTzbymSZT-JjEeAGGkApYHZgxnGV6GbQEcxXqKPzjsQ-y9ajNJv6WlQT1Zves1z4Aey'

data = {
	"content": tl['statuses'][0]['text']
}

requests.post(hook_url, data=data)