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
        # if (post["type"] == "Image" or post["type"] == "Sidecar") and not post["isSponsored"] and len(post["hashtags"]) == 0:
        if (post["type"] == "Image" or post["type"] == "Sidecar") and not post["isSponsored"] and "#ad" not in post["hashtags"]:
            if ("paidPartnership" in post and not post["paidPartnership"]) or "paidPartnership" not in post:
                caption = format_caption(post["caption"]) if len(post["caption"]) > 0 else '<NO-CAPTION>'
                for image in post["images"]:
                    full_data[image] = {"true_caption": caption}
    return full_data

def main():
    data = loadJSON('normal_ppl_posts_pt1.json')
    data = format_data(data)
    saveAsJSON('processed_normal_ppl_data_pt1.json', data)

if __name__ == '__main__':
    main()

# def load_text(filename):
#     f = open(filename, "r")
#     return f.read()

# def get_text(filename):
#     text = load_text(filename).replace('\n', '')
#     #clean
#     tokens = text.split()
#     for i in range(len(tokens)):
#         if tokens[i].startswith('@'):
#             tokens[i] = '<NAME>'
#     return ' '.join(tokens)
    
# def load_data(directory):
#     data = {}
#     #get strings of filename for each img as key to data dict
#     for filename in os.listdir(directory):
#         f = os.path.join(directory, filename)
#         if f.endswith('.jpg'):
#             data[f] = {}

#     #set true caption as value for relevant key in data dict
#     for filename in os.listdir(directory):
#         f = os.path.join(directory, filename)
#         if f.endswith('.txt'):
#             #get text
#             caption = get_text(f)
#             stripped_f = f.replace('.txt', '')
#             #find images associated with caption and add to data dict
#             for img_f in data:
#                 stripped_img_f = re.search(r"(.+_UTC)", img_f).groups()[0]
#                 if stripped_f == stripped_img_f:
#                     data[img_f]['true_caption'] = caption
#     return data

# def saveAsJSON(f, d):
#     with open(f, "w") as outfile:
#         json.dump(d, outfile)

# def main():
#     data_dir = 'instaData'
#     for user_dir in os.listdir(data_dir):
#         user_path = os.path.join(data_dir, user_dir)
#         if os.path.isdir(user_path):
#             data = load_data(user_path)
#             saveAsJSON(user_path+'_og_caption_data.json', data)

# if __name__ == '__main__':
#     main()