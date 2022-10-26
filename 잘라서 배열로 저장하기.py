def solution(my_str, n):
    answer = []
    for i in range (0,len(my_str)-n+3,n) :
        answer.append(my_str[i:i+n])
    length = len("".join(answer))
    return answer