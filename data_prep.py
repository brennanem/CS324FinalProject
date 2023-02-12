import os
import re
import json


def load_text(filename):
    f = open(filename, "r")
    return f.read()

def load_data(directory):
    data = {}
    #get strings of filename for each img as key to data dict
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if f.endswith('.jpg'):
            data[f] = {}

    #set true caption as value for relevant key in data dict
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if f.endswith('.txt'):
            #get text
            caption = load_text(f).replace('\n', '')
            stripped_f = f.replace('.txt', '')
            #find images associated with caption and add to data dict
            for img_f in data:
                stripped_img_f = re.search(r"(.+_UTC)", img_f).groups()[0]
                if stripped_f == stripped_img_f:
                    data[img_f]['true_caption'] = caption
    
    return data

def saveAsJSON(f, d):
    with open(f, "w") as outfile:
        json.dump(d, outfile)

def main():
    data = load_data('testKylie')
    saveAsJSON('kylie_data.json', data)


if __name__ == '__main__':
    main()