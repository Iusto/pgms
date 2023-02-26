def solution(s):
    answer = list(s)
    n = 0
    for i in range (len(s)) :
        if answer[i] == " " :
            n = 0
            continue
        elif n % 2 == 0 :
            answer[i] = answer[i].upper()
            n+=1
        else :
            answer[i] = answer[i].lower()
            n+=1
    return "".join(answer)