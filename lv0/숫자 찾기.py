def solution(num, k):
    num = list(map(int, str(num)))
    if k not in num :
        return -1
    else :
        return num.index(k) + 1