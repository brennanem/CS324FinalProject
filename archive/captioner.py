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
        entry = {"text": "caption: {plain_caption}\ngen-z social media caption: {gen_z_cap}".format(plain_caption = gen_caption, gen_z_cap = true_caption)}
        fine_tuning_data.append(entry)
    return fine_tuning_data    

def dump_to_file(fine_tuning_datasest):
    json_object = json.dumps(fine_tuning_datasest, indent=4)
    with open("influencerData.json", "w") as outfile:
        outfile.write(json_object)

def read_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

data_obj = read_data('./processed_celeb_data.json') #add file name here
# data_obj = {"https://instagram.fyvr2-1.fna.fbcdn.net/v/t51.2885-15/331822475_837510971426326_2068478160543791994_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=instagram.fyvr2-1.fna.fbcdn.net&_nc_cat=110&_nc_ohc=qjs1ERUfnNoAX_VXkb0&edm=AABBvjUBAAAA&ccb=7-5&oh=00_AfAT8duKiIWtIfvLZpTWod_Kl_T13a-6vkRt6LULGcnrdw&oe=63FF27CA&_nc_sid=83d603": {"true_caption": "test"}}
fine_tuning_datasest = caption(data_obj) 
dump_to_file(fine_tuning_datasest)
