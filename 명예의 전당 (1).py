def solution(k, score):
    hof = []
    answer = []
    for i in score:
        hof.append(i)
        if (len(hof) > k):
            hof.remove(min(hof))
        answer.append(min(hof))

    return answer