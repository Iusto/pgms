import math
def solution(arr):
    answer = 1
    for n in arr:
        answer *= int(n / math.gcd(n, answer))

    return answer