import json_lines
import json

#json_lines での処理。　後でとっとく処理がめんどくさい
items = None

with open('subprocessTest.jl', 'rb') as f:
    items = json_lines.reader(f)
    for item in items:
        pass
        #print(item['title'])
        #print(item['link'])

print(items)
print("A")
for i in json_lines.reader(items):
    print(i)
    print(i['title'])
    print(i['link'])


#import json　での処理

lines = []

with open('pydocTest.jl', 'r') as f:
    for line in f:
        lines.append(json.loads(line))
for i in lines:
    print(i["title"])
    print(i["link"])
