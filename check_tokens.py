from transformers import GPT2Tokenizer

import json
import matplotlib.pyplot as plt

## This file was used to find the length of our longest input in tokens and visualize the distribution of token length 

with open('./combined_data.jsonl', 'r') as json_file:
    json_list = list(json_file)

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

longestString = ''
longestLength = 0
listOfLengths = []
newList = []
for json_str in json_list:
    result = json.loads(json_str)
    string = result['text']
    listOfIds = tokenizer(string)['input_ids']
    tokens = len(listOfIds)
    if tokens <= 70:
        newList.append(result)
    listOfLengths.append(tokens)
    # if (length > longestLength):
    #     longestLength = length
    #     longestString = string

plt.hist(listOfLengths)
plt.show()
# print(len(newList))
# with open('combined_and_cut_data.jsonl', 'w') as f:
#     for entry in newList:
#         json.dump(entry, f)
#         f.write('\n')

