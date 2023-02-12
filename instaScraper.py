from itertools import islice
from math import ceil
import instaloader
from datetime import datetime
from itertools import dropwhile, takewhile
from instaloader import Instaloader, Profile

PROFILE = ["sydney_sweeney"]
SINCE = datetime(2023, 1, 16)
UNTIL = datetime(2023, 2, 11)
L = instaloader.Instaloader()

for profile in PROFILE: 
	posts = instaloader.Profile.from_username(L.context, profile).get_posts()
	# for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
	for post in posts:
		if not (post.date_utc >= SINCE and post.date_utc <= UNTIL):
			continue
		if len(post.caption_hashtags)!= 0:
			continue
		if post.is_video: #only exclude if the first slide in the post is a video, otherwise include
			continue
		if post.is_sponsored:
			continue
		print(post.caption)
		L.download_post(post, profile)
   		

