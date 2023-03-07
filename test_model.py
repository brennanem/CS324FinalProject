import torch
from transformers import AutoTokenizer, AutoModelForCausalLM 
import json
from PIL import UnidentifiedImageError
from transformers import pipeline
from PIL import UnidentifiedImageError
import csv
import pandas as pd
import re



def load_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(json.loads(line))
    return data


def main():
	tokenizer = AutoTokenizer.from_pretrained("xzyao/HWNWZ5B9AM9PSXV09BAF24ADGP97LMCN2LFQTZJNRQF318SMFM") 
	model = AutoModelForCausalLM.from_pretrained("xzyao/HWNWZ5B9AM9PSXV09BAF24ADGP97LMCN2LFQTZJNRQF318SMFM")
	with open("prompt.txt") as f: 
		plain_prompt = "".join(f.readlines())
	test_data = "test_data_FINAL_2.jsonl"
	data = load_data(test_data)
	print("num test examples", len(data))
	eval_data = {"plain_text_caption": [], "true_gen_z_caption": [], "generated_caption": []}
	for i, post in enumerate(data): 
		print("example", i)
		string_text = post["text"]
		plain_text_caption = re.search(r"caption: (.*) \n", string_text).groups()[0]
		gen_z_caption = re.search(r"gen-z social media caption: (.*)", string_text).groups()[0]
		prompt = plain_prompt.replace("<ADD-PLAIN-TEXT-CAPTION>", plain_text_caption)

		input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)

		gen_tokens = model.generate(
			input_ids,
			do_sample=True,
			temperature=1.0,
			max_new_tokens=20,
			eos_token_id=198, #new line token
			pad_token_id=198,
		)
		gen_text = tokenizer.batch_decode(gen_tokens)[0]
		gen_caption = re.findall(r"gen-z social media caption: (.*)\n?", gen_text)[-1].replace("\n", "")
		eval_data["plain_text_caption"].append(plain_text_caption)
		eval_data["true_gen_z_caption"].append(gen_z_caption)
		eval_data["generated_caption"].append(gen_caption)
	
	df = pd.DataFrame.from_dict(eval_data)
	df.to_csv("evaluation_data.csv", index=False)

if __name__ == '__main__':
    main()





