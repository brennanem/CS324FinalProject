from transformers import GPT2Tokenizer

import json
import matplotlib.pyplot as plt
# Opening JSON file
with open('./combined_data.jsonl', 'r') as json_file:
    json_list = list(json_file)
# returns JSON object as 
# a dictionary
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

longestString = ''
longestLength = 0
listOfLengths = []
newList = []
for json_str in json_list:
    result = json.loads(json_str)
    string = result['text']
    # length = len(string)
    listOfIds = tokenizer(string)['input_ids']
    tokens = len(listOfIds)
    if tokens <= 70:
        newList.append(result)
    listOfLengths.append(tokens)
    # if (length > longestLength):
    #     longestLength = length
    #     longestString = string

# plt.hist(listOfLengths)
# plt.show()
print(len(newList))
with open('combined_and_cut_data.jsonl', 'w') as f:
    for entry in newList:
        json.dump(entry, f)
        f.write('\n')

# print("longestLength: " + str(longestLength))
# print(longestString)

    
# Iterating through the json
# list
# for i in data['emp_details']:
#     print(i)
  
# Closing file
