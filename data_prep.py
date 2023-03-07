import os
import re
import json

## This file takes in the raw outputs from Apify and puts the data in a useable format (processed data). This format
## includes the image URL and the true caption. It also filters out posts that are ads or videos. 

def saveAsJSON(f, d):
    with open(f, "w") as outfile:
        json.dump(d, outfile)

def loadJSON(f):
    with open(f, 'r') as json_file:
        data = json.load(json_file)
    return data

def format_caption(text):
    #clean
    tokens = text.split()
    for i in range(len(tokens)):
        if tokens[i].startswith('@'):
            tokens[i] = '<NAME>'
    return ' '.join(tokens)

def format_data(data):
    full_data = {}
    for post in data:
        #IF CELEBS USE:
        # if (post["type"] == "Image" or post["type"] == "Sidecar") and not post["isSponsored"] and len(post["hashtags"]) == 0:
        #IF NORMAL PEOPLE USE:
        if (post["type"] == "Image" or post["type"] == "Sidecar") and not post["isSponsored"] and "#ad" not in post["hashtags"]:
            if ("paidPartnership" in post and not post["paidPartnership"]) or "paidPartnership" not in post:
                caption = format_caption(post["caption"]) if len(post["caption"]) > 0 else '<NO-CAPTION>'
                for image in post["images"]:
                    full_data[image] = {"true_caption": caption}
    return full_data

def main():
    #CHANGE INPUT FILENAME
    data = loadJSON('rawApifyOutpits/normal_ppl_posts_pt1.json')
    data = format_data(data)
    #CHANGE OUTPUT FILENAME
    saveAsJSON('processed_normal_ppl_data_pt1.json', data)

if __name__ == '__main__':
    main()
