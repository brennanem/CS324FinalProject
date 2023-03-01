import os
import re
import json

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
<<<<<<< HEAD
        #IF CELEBS USE:
        # if (post["type"] == "Image" or post["type"] == "Sidecar") and not post["isSponsored"] and len(post["hashtags"]) == 0:
        #IF NORMAL PEOPLE USE:
        if (post["type"] == "Image" or post["type"] == "Sidecar") and not post["isSponsored"] and "#ad" not in post["hashtags"]:
            if ("paidPartnership" in post and not post["paidPartnership"]) or "paidPartnership" not in post:
                caption = format_caption(post["caption"]) if len(post["caption"]) > 0 else '<NO-CAPTION>'
=======
        # if i == 0:
        #     print('post type', post["type"])
        #     print('post sponsored', post["isSponsored"])
        #     print('len hashtags', len(post["hashtags"]))
        # if (post["type"] == "Image" or post["type"] == "Sidecar") and not post["isSponsored"] and not post["paidPartnership"] and "#ad" not in post["hashtags"]:

        if (post["type"] == "Image" or post["type"] == "Sidecar") and not post["isSponsored"] and "#ad" not in post["hashtags"]:
            if ("paidPartnership" in post and not post["paidPartnership"]) or "paidPartnership" not in post:
                caption = format_caption(post["caption"]) if len(post["caption"]) > 0 else '<NO_CAPTION>'
>>>>>>> 5e49fc6 (created normal people output data folders)
                for image in post["images"]:
                    full_data[image] = {"true_caption": caption}
    return full_data

def main():
<<<<<<< HEAD
    #CHANGE INPUT FILENAME
    data = loadJSON('rawApifyOutpits/normal_ppl_posts_pt1.json')
    data = format_data(data)
    #CHANGE OUTPUT FILENAME
    saveAsJSON('processed_normal_ppl_data_pt1.json', data)
=======
    data = loadJSON('normal_people_pt2_raw_data.json')
    data = format_data(data)
    saveAsJSON('processed_normal_people_data_pt2.json', data)
>>>>>>> 5e49fc6 (created normal people output data folders)

if __name__ == '__main__':
    main()
