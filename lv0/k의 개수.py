def solution(i, j, k):
    answer = ""
    for i in range(i,j+1) :
        answer += str(i)
    return answer.count(str(k))