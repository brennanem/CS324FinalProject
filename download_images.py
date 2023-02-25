
import json
import requests

JSON_FILE = processed_celeb_data.json


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
        	with open('.jpg', 'wb') as f:
            	f.write(response.content)
def main():
	downloaded_dict = {}
	num = 0
	json_dict= loadJSON(JSON_FILE)
	for image_url in json_dict:
		image_name = "image_" + num
		loadImage(image_url, image_num)
		downloaded_dict[image_name] = json_dict[image_url]
		num += 1
		if (num % 100 = 0):
			print("DOWNLOADED ", num, " IMAGES")
	saveAsJSON("downloaded_celeb_data.json", downloaded_dict)


