from itertools import islice
from math import ceil
import instaloader
from datetime import datetime
from itertools import dropwhile, takewhile
from instaloader import Instaloader, Profile

PROFILE = [‘alix_earle’, ‘kyliejenner’, ‘charliedamelio’, ‘laurenwolfe’, ‘maddieziegler’, ‘sommerray’, ‘livvydunne’, ‘bellapoarch’, ‘oliviarodrigo’, ‘staskaranikolaou’, ‘dualipa’, ‘zendaya’, ‘amandasteele’, ‘lilychee’, ‘khaby00’, ‘milliebobbybrown’, ‘daisykeech’, ‘noahcyrus’, ‘addisonraee’, ‘dixiedamelio’, ‘luckybsmith’, ‘bradypotter’, ‘zackbia’, ‘lukasabbat’, ‘kevinbororquez’, ‘alexparsa’, ‘bretmanrock’, ‘emmachamberlain’, ‘siennamaegomez’, ‘madelineargy’, ‘kendalljenner’, ‘justinliv’, ‘tanamongeau’, ‘jackmorris’, ‘lilyrose_depp’, ‘emmaroberts’, ‘lirisaw’, ‘ivygetty’, ‘leniklum’, ‘reneerapp’, ‘maudeapatow’, ‘katybellotte’, ‘sydney_sweeney’, ‘fatherkels’, ‘serena_pitt’, ‘barbieferreira’, ‘kitkeenan’, ‘acquired.style’, ‘tchalamet’, ‘aadamharrison’, ‘harryjowsey’, ‘drumaq’, ‘clix’, ‘haileybieber’, ‘boyinquestion’, ‘oliviajade’, ‘bretmanrock’, ‘noahbeck’, ‘suedebrooks’, ‘stevenfingar’, ‘conangray’, ‘alabamaluellabarker’, ‘landonasherbarker’, ‘brycehall’, ‘realbarbarapalvin’, ‘perfect_angelgirl’]
 #list of profiles 
SINCE = datetime(2023, 1, 16)
UNTIL = datetime(2023, 2, 11)
L = instaloader.Instaloader()

for profile in PROFILE: 
	posts = instaloader.Profile.from_username(L.context, profile).get_posts()
	for post in posts:
		if not (post.date_utc >= SINCE and post.date_utc <= UNTIL):
			continue
		if len(post.caption_hashtags)!= 0:
			continue
		if post.is_video: #only exclude if the first slide in the post is a video, otherwise include
			continue
		if post.is_sponsored:
			continue
		L.download_post(post, profile)