import json
import os
import random

## This file divided our dataset into the data we would use for testing, and the data we would use for evaluating 
## It was also used to combine files when we had to run in multiple batches 

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

def combine_data(dir_path):
    data = []
    for filename in os.listdir(dir_path):
        f = os.path.join(dir_path, filename)
        if os.path.isfile(f): 
            data += load_data(f)
    return data

def main():
    # data = combine_data("data/")
    # save_data("combined_data.jsonl", data)

    data = load_data("combined_and_cut_data.jsonl")
    total = len(data)
    test_indices = random.sample(range(total), 100)
    train_data, test_data = [], []
    for i, entry in enumerate(data):
        if i in test_indices:
            test_data.append(entry)
        else:
            train_data.append(entry)
    save_data("finetuning_data_FINAL.jsonl", train_data)
    save_data("testing_data_FINAL.jsonl", test_data)

if __name__ == '__main__':
    main()
