from itertools import islice
from math import ceil
import instaloader
from datetime import datetime
from itertools import dropwhile, takewhile
from instaloader import Instaloader, Profile
import time

	

def runScraper(since, until, profiles):
	L = instaloader.Instaloader()
	for profile in profiles: 
		posts = instaloader.Profile.from_username(L.context, profile).get_posts()
		counter = 0
		for post in posts:
			if counter == 12: 
				sleep(20)
			if not (post.date_utc >= since and post.date_utc <= until):
				continue
			if len(post.caption_hashtags)!= 0:
				continue
			if post.is_video: #only exclude if the first slide in the post is a video, otherwise include
				continue
			if post.is_sponsored:
				continue
			L.download_post(post, profile)
			counter += 1

def main():
	profiles = ["alix_earle"]

	#jan 2023
	since = datetime(2022, 1, 1)
	until = datetime(2023, 1, 15)
	runScraper(since, until, profiles)

	# time.sleep(45)
	# #feb 2023
	# since = datetime(2023, 2, 1)
	# until = datetime(2023, 2, 15)
	# runScraper(since, until, profiles)

	# time.sleep(45)
	# #last year 
	# for month in range(1, 12, 1):
	# 	time.sleep(45)
	# 	since = datetime(2022, month, 1)
	# 	until = datetime(2022, month + 1, 1)
	# 	runScraper(since, until, profiles)


if __name__ == "__main__":
	main()


