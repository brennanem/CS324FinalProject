
import json
import requests

JSON_FILE = "processed_celeb_data.json"


def saveAsJSON(filename, dict):
	with open(f, "w") as outfile: 
		json.dump(dict, outfile)

def loadJSON(f):
	with open(f) as json_file:
		data = json.load(json_file)
	return data

def loadImage(image_url, image_name):
	try:
		response = requests.get(image_url)
	except:
		print('Error')
	else:
		if response.status_code == 200:
			with open("./celeb image downloads/" + image_name + ".jpg", 'wb') as f:
				f.write(response.content)
def main():
	downloaded_dict = {}
	num = 2974
	json_dict= loadJSON(JSON_FILE)
	for i, image_url in enumerate(json_dict.keys()):
		if i > num:
			image_name = "image_" + str(num)
			loadImage(image_url, image_name)
			downloaded_dict[image_name] = json_dict[image_url]
			if (num % 100 == 0):
				print("DOWNLOADED ", num, " IMAGES")
			num += 1
	saveAsJSON("downloaded_celeb_data.json", downloaded_dict)

if __name__ == "__main__":
	main()

