from itertools import product
def solution(word):
    vowel = ['A','E','I','O','U']
    words = []
    for i in range (1,6) :
        for j in list(product(vowel, repeat=i)) :
            words.append(''.join(j))
    words.sort()
    return words.index(word) + 1