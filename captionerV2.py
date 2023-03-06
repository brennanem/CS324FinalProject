import json
from PIL import UnidentifiedImageError
from transformers import pipeline
from PIL import UnidentifiedImageError

image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

def read_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data
    
# insert whichever raw data we're doing a run on 
data_obj = read_data('./processed_normal_people_data_pt2.json')

# use a different file name for each run
with open("normal_people_pt2_2_output.json", "w") as outfile:
    for i, img in enumerate(data_obj):
        try:
            plain_text_caption_obj = image_to_text(img)
            gen_caption = plain_text_caption_obj[0]['generated_text']                
            true_caption = data_obj[img]['true_caption']
            if (i % 50 == 0):
                print(i)
            entry = {"text": "caption: {plain_caption}\ngen-z social media caption: {gen_z_cap}".format(plain_caption = gen_caption, gen_z_cap = true_caption)}
            json_object = json.dumps(entry, indent=4)
            outfile.write(json_object)
        except UnidentifiedImageError:
            print("skipped image at i = " + str(i))
        except:
            print("skipped for another reason, ", i)
