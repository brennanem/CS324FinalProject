import torch
from transformers import AutoTokenizer, AutoModelForCausalLM 
import json
from PIL import UnidentifiedImageError
from transformers import pipeline
from PIL import UnidentifiedImageError




img = "grace_isaac.jpg" #TODO: figure out how to get image from user

image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")


tokenizer = AutoTokenizer.from_pretrained("xzyao/HWNWZ5B9AM9PSXV09BAF24ADGP97LMCN2LFQTZJNRQF318SMFM") 
model = AutoModelForCausalLM.from_pretrained("xzyao/HWNWZ5B9AM9PSXV09BAF24ADGP97LMCN2LFQTZJNRQF318SMFM")

print("downloaded tokenizer + model")

# try:
plain_text_caption_obj = image_to_text(img)
plain_text_caption = plain_text_caption_obj[0]['generated_text']

print("plaintext caption: ", plain_text_caption)

with open("prompt.txt") as f: 
	plain_prompt = "".join(f.readlines())

prompt = plain_prompt.replace("<ADD-PLAIN-TEXT-CAPTION>", plain_text_caption)
print("FULL PROMPT: ", prompt)

# try:
input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)

gen_tokens = model.generate(
	input_ids,
	do_sample=True,
	temperature=0.9, #can change to increase randomness for gen z
	max_length = 80, #can toggle length for shorrter gen-z captions
)

gen_text = tokenizer.batch_decode(gen_tokens)[0]
print(gen_text)

# except:
# 	print("tokenizer error")

# except:
# 	print("image error")





