import math
def solution(a, b):
    gcd = math.gcd(a, b)
    s = [] # 소인수분해
    N = b // gcd  # 나누어지는 수
    d = 2  # 나누는 수
    while N != 1:
        if N % d != 0:
            d += 1
        else:
            N //= d
            s.append(d)
    s = list(set(s))
    if a%b == 0 or (len(s) <= 2 and 2 in s) or (len(s) <= 2 and 5 in s) :
        return 1
    else : 
        return 2