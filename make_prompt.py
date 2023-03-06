import json
import random

def load_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(json.loads(line))
    return data

def save_data(filename, data):
    with open(filename, 'w') as f:
        for entry in data:
            json.dump(entry, f)
            f.write('\n')

def make_prompt(data):
    total = len(data)
    prompt_indices = random.sample(range(total), 5)
    test_data = []
    prompts = []
    for i, entry in enumerate(data):
        if i in prompt_indices:
            prompts.append(entry["text"])
        else:
            test_data.append(entry)
    prompts.append("caption: <ADD-PLAIN-TEXT-CAPTION>\ngen-z social media caption:")
    prompt = "\n\n".join(prompts)
    return prompt, test_data

def main():
    data = load_data("testing_data_FINAL.jsonl")
    prompt, data = make_prompt(data)
    print(prompt)
    save_data("test_data_FINAL_2.jsonl", data)

if __name__ == "__main__":
    main()