def solution(d, budget):
    d.sort()
    answer = 0
    for i in d :
        if budget >= i :
            answer += 1
            budget-=i
        else :
            return answer
    return answer