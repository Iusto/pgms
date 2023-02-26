def solution(s):
    answer = ""
    if len(s) % 2 != 0 :
        return "".join(list(s[len(s)//2]))
    else :
        for i in range(len(s)//2-1, len(s)//2+1) :
            answer += s[i]
        return answer
    