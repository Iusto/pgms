from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers] # [(4, -4), (1, -1), (2, -2), (1, -1)]
    s = list(map(sum, product(*l)))
    return s.count(target)