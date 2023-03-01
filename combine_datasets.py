import json
import os

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
    data = combine_data("data/")
    save_data("combined_data.jsonl", data)

if __name__ == '__main__':
    main()
