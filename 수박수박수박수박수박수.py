def solution(n):
    answer = ''
    i = 0
    #홀수는 "수" 짝수는 "박"
    while (i < n) :
        i+=1
        if i % 2 == 0 :
            answer += "박"
        else :
            answer += "수"
    return answer