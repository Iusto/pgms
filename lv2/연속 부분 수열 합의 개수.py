def solution(elements):
    l = len(elements) # 5
    answer = []

    for i in range(l): #0~4
        s = elements[i]
        answer.append(s)
        for j in range(i+1, i+l): #j = 1234 2345 3456 4567 5678
            s += elements[j%l] #elements[1234] -> 2340 3401 4012 0123
            answer.append(s)
    return len(set(answer))