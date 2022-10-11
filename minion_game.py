# Stuart B
from itertools import count
from operator import index
import string
word = 'banana'
consonants = list(string.ascii_lowercase)
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(len(vowels)):
    if vowels[i] in consonants:
        consonants.remove(vowels[i])
stuart = []
for i in range(len(word)):
    if word[i] in consonants:
        index = i
        stuart.append(word[index:])
        # bez -1 ostanie słowo będzie puste
        for j in range(len(word[index:])-1):
            new_word = word[index:(-1-j)]
            stuart.append(new_word)

print(stuart)
kevin = []
# Kewvin A
for i in range(len(word)):
    if word[i] in vowels:
        index = i
        kevin.append(word[index:])
        for j in range(len(word[index:])-1):
            new_word = word[index:(-1-j)]
            kevin.append(new_word)
print(kevin)
if len(kevin) > len(stuart):
    print("Kevin", len(kevin))

elif len(stuart)> len(kevin):
    print("Stuart", len(stuart))

else: print('draw')


