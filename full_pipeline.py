import torch
from transformers import AutoTokenizer, AutoModelForCausalLM 
import json
from PIL import UnidentifiedImageError
from transformers import pipeline
from PIL import UnidentifiedImageError
import re



#get image
img = "grace_isaac.jpg" #TODO: figure out how to get image from user

#download image captioner
image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

#download tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("xzyao/HWNWZ5B9AM9PSXV09BAF24ADGP97LMCN2LFQTZJNRQF318SMFM") 
model = AutoModelForCausalLM.from_pretrained("xzyao/HWNWZ5B9AM9PSXV09BAF24ADGP97LMCN2LFQTZJNRQF318SMFM")
print("downloaded tokenizer + model")

#get descriptive caption
plain_text_caption_obj = image_to_text(img)
plain_text_caption = plain_text_caption_obj[0]['generated_text']
print("plaintext caption: ", plain_text_caption)

#set prompt
with open("prompt.txt") as f: 
	plain_prompt = "".join(f.readlines())
prompt = plain_prompt.replace("<ADD-PLAIN-TEXT-CAPTION>", plain_text_caption)

#tokenize
input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)
#generate from model
gen_tokens = model.generate(
	input_ids,
	do_sample=True,
	temperature=1.0,
	max_new_tokens=20,
	eos_token_id=198, #new line token
	pad_token_id=198,
	num_return_sequences=5,
)
gen_text = tokenizer.batch_decode(gen_tokens)

#extract captions
captions = [re.findall(r"gen-z social media caption: (.*)\n?", text)[-1].replace("\n", "") for text in gen_text]
print(captions)






