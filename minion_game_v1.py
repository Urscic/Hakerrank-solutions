'''
this verions is working fine with small strings, but it needs optimalizatoin for longer ones
what needs a lot of memo:
- lists (worked)
- nested loops (better but not enough)
PS. The problem occurs to be using index
'''
def minion_game(word):
    from itertools import count
    from operator import index
    import string
    consonants = list(string.ascii_uppercase)
    vowels = ['A', 'E', 'I', 'O', 'U']
    stuart = []
    kevin = []
    for i in range(len(vowels)):
        if vowels[i] in consonants:
            consonants.remove(vowels[i])
    
    for i in range(len(word)):
        if word[i] in consonants:
            index = i
            stuart.append(word[index:])
            for j in range(len(word[index:])-1):
                new_word = word[index:(-1-j)]
                stuart.append(new_word)

    
    for i in range(len(word)):
        if word[i] in vowels:
            index = i
            kevin.append(word[index:])
            for j in range(len(word[index:])-1):
                new_word = word[index:(-1-j)]
                kevin.append(new_word)
    if len(kevin) > len(stuart):
        print("Kevin", len(kevin))

    elif len(stuart)> len(kevin):
        print("Stuart", len(stuart))

    elif len(kevin)==len(stuart): 
        print('Draw')
      
if __name__ == '__main__':
    s = input()
    minion_game(s)
