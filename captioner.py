## Run this line first 
# pip install transformers
import json
from transformers import pipeline

image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

# [{'generated_text': 'a soccer game with a player jumping to catch the ball '}]
def caption(data):
    fine_tuning_data = []
    
    for img in data:
        plain_text_caption_obj = image_to_text(img)
        gen_caption = plain_text_caption_obj[0]['generated_text']
        # is this how they want the data?
        true_caption = data[img]['true_caption']
        # print(img)
        # print(true_caption)
        # print(gen_caption)
        entry = {"text": "caption: {plain_caption}\ngen-z language caption: {gen_z_cap}".format(plain_caption = gen_caption, gen_z_cap = true_caption)}
        fine_tuning_data.append(entry)
    return fine_tuning_data    

def dump_to_file(fine_tuning_datasest):
    json_object = json.dumps(fine_tuning_datasest, indent=4)
    with open("fineTuningAttempt2.json", "w") as outfile:
        outfile.write(json_object)

def read_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

data_obj = read_data('./kylie_data.json') #add file name here
fine_tuning_datasest = caption(data_obj) 
dump_to_file(fine_tuning_datasest)
