import os
import re
import json

# count = 0 
# with open("normal_people_pt2_output.json") as json_file:
#     data = json.load(json_file)
#     for key in data: 
#         count += 1
# print(count)

count = 0
with open("normal_people_pt2_output.json") as f:
    for line in f:
        count += line.count("{")
print(count)
