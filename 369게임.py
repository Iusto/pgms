def solution(order):
    i = str(order)
    answer = i.count('3') + i.count('6') + i.count('9')
    return answer