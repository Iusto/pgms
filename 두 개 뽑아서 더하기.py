import itertools
def solution(numbers):
    result = []
    p = itertools.permutations(numbers,2)
    for i in p :
        result.append(sum(i))
    return sorted(list(set(result)))