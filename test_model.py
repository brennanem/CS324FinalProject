import torch
from transformers import AutoTokenizer, AutoModelForCausalLM 
import json
from PIL import UnidentifiedImageError
from transformers import pipeline
from PIL import UnidentifiedImageError
import csv



def load_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(json.loads(line))
    return data


if __name__ == '__main__':
    main()


def main():
	tokenizer = AutoTokenizer.from_pretrained("xzyao/HWNWZ5B9AM9PSXV09BAF24ADGP97LMCN2LFQTZJNRQF318SMFM") 
	model = AutoModelForCausalLM.from_pretrained("xzyao/HWNWZ5B9AM9PSXV09BAF24ADGP97LMCN2LFQTZJNRQF318SMFM")
	with open("prompt.txt") as f: 
		plain_prompt = "".join(f.readlines())
	test_data = "test_data_FINAL_2.jsonl"
	data = load_data(test_data)
	final_captions = []
	for post in data: 
		string_text = post["text"]
		end = string_text.find("\n") - 1
		plain_text_caption = string_text[:end]
		colon = string_text.find(":")
		gen_z_caption = string_text[colon + 2:]
		prompt = plain_prompt.replace("<ADD-PLAIN-TEXT-CAPTION>", plain_text_caption)

		input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)

		gen_tokens = model.generate(
			input_ids,
			do_sample=True,
			temperature=0.9, #can change to increase randomness for gen z
			max_length = 80, #can toggle length for shorrter gen-z captions
		)

		gen_text = tokenizer.batch_decode(gen_tokens)[0]
		post_dict = {}
		post_dict["plain_text_caption"] = plain_text_caption
		post_dict["gen_z_caption"] = gen_z_caption
		post_dict["generated_caption"] = gen_text
		final_captions.append(post_dict)

	final_file = open('evaluation_data.csv', 'w')
	writer = csv.writer(final_file)
	writer.writerow(['plain_text_caption', 'gen_z_caption', 'generated_caption'])
	for dictionary in final_captions: 
		writer.writerow(dictionary.values())







