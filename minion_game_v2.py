
from itertools import count
from operator import index
import string
word = 'BANANA'
consonants = list(string.ascii_uppercase)
vowels = ['A', 'E', 'I', 'O', 'U']
stuart = 0
kevin = 0
for i in range(len(vowels)):
    if vowels[i] in consonants:
        consonants.remove(vowels[i])

for i in range(len(word)):
    if word[i] in consonants:
        stuart += (len(word[i:]))
    if word[i] in vowels:
        kevin += (len(word[i:]))

if kevin > stuart:
    print("Kevin", kevin)

elif stuart > kevin:
    print("Stuart", stuart)

elif kevin == stuart:
    print('Draw')
