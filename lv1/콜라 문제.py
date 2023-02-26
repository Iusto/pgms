def solution(a, b, n):
    answer = 0
    while (n // a != 0) :
        answer += n//a*b
        c = int(n%a)
        n = n//a*b + c
    return answer