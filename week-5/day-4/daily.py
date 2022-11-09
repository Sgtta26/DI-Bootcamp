from collections import defaultdict
from collections import Counter
import string

from nltk.corpus import stopwords

import re



class Text:
    def __init__ (self, txt):
        self.txt = txt
        


txt = "A good book would sometimes cost as much as a good house"
x = txt.count ("good")
print(x)

for _ in txt:
    if x>0:
        print(x)
    else:
        print("None")
    break

def mostFrequentWord(words):
        l = []
        for i in words:
            for j in i.split():
                l.append(j)

        freq = Counter (l)

        max = 0
        for i in freq:
            if (freq[i]>max):
                max = freq[i]
                word = i
                return word

words = ["A good book would sometimes cost as much as a good house"]         
print("Most frequent word is "+ mostFrequentWord(words))


text_file = open('sentence.txt', 'r')
text = text_file.read()

text = text.lower()
words = text.split()
words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]

unique = []
for word in words:
    if word not in unique:
        unique.append(word)

unique.sort()

print(unique)




text_file = open('stranger.txt', 'r')
text = text_file.read()

@classmethod
def from_file(cls, file_path):
    with open("stranger.txt", "r") as f:
        file_content = f.read()
    return cls(file_content)



#Text.from_file('stranger.txt')


class TextModification(Text):
    txt = txt.translate(str.maketrans('', '', string.punctuation))
print(txt)



cleanString = re.sub('\W+','', txt)
print(txt)