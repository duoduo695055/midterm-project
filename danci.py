import re

with open('vows.txt','r') as f:
    text=f.read()

words=re.findall(r'\w+\b',text)

print(len(words))
print('there are %d words'%len(words))