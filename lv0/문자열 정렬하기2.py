def solution(my_string):
    a = my_string.lower()
    a = list(a)
    a.sort()
    answer = ''.join(a)
    return answer