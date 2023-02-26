import math

def solution(n):
    i = math.sqrt(n)
    if i % 1 == 0 :
        answer = (i+1) ** 2
    else :
        answer = -1
    return answer