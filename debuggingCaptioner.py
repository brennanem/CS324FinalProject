import json

def read_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data
    
data_obj = read_data('./processed_celeb_data.json')
# read_so_far = read_data('./influencerOutput.json')
print(len(data_obj))
for i, img in enumerate(data_obj):
    if i == 5865:
        print(img)
        break
# print(len(read_so_far))