from collections import deque
def solution(priorities, location):
    answer = 0
    d = deque([(v,i) for i,v in enumerate(priorities)])
    while len(d):
        item = d.popleft()
        if max(d)[0] > item[0]:
            d.append(item)
        else :
            answer += 1
            if item[1] == location:
                break
    return answer