import itertools
def solution(number):
    result = []
    r = itertools.combinations(number, 3)
    for i in list(r) :
        if sum(i) == 0 :
            result.append(i)
    return len(result)