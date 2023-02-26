def solution(N, stages):
    result = {}
    l = len(stages)
    for i in range (1, N+1) :
        if l != 0 :
            count = stages.count(i)
            result[i] = count / l
            l -= count
        else :
            result[i] = 0
    print(result)
    return sorted(result, key=lambda x : result[x], reverse=True)