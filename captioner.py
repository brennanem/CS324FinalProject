## Run this line first 
# pip install transformers
import json
from transformers import pipeline

image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

# [{'generated_text': 'a soccer game with a player jumping to catch the ball '}]
def caption(data):
    fine_tuning_data = {}
    for img in data:
        plain_text_caption_obj = image_to_text(img)
        gen_caption = plain_text_caption_obj['generated_text']
        # is this how they want the data?
        fine_tuning_data[img['true caption']] = gen_caption

def dump_to_file(fine_tuning_datasest):
    json_object = json.dumps(fine_tuning_datasest, indent=4)
    with open("fine_tuning_data.json", "w") as outfile:
        outfile.write(json_object)

def read_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

data_obj = read_data() #add file name here
fine_tuning_datasest = caption(data_obj) 
dump_to_file(fine_tuning_datasest)
