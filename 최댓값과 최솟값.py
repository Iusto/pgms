def solution(s):
    answer = []
    s = s.split(" ")
    for i in s :
        answer.append(int(i))
    
    return str(min(answer)) + " " + str(max(answer))