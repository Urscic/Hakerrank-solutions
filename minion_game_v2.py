def minion_game(word):
    from itertools import count
    from operator import index
    import string
    alph = list(string.ascii_uppercase)
    vowels = ['A', 'E', 'I', 'O', 'U']
    stuart, kevin = 0, 0
    consonants = [i for i in alph if i not in vowels]

    for i in range(len(word)):
        if word[i] in consonants:
            stuart += (len(word)-i) #len(word)-i WAY MUCH FASTER THEN (len(word[index:])-1)
        
        if word[i] in vowels:
            kevin += (len(word)-i)

    if kevin > stuart:
        print("Kevin", kevin)

    elif stuart > kevin:
        print("Stuart", stuart)

    elif kevin == stuart:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)