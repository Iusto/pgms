def solution(num, total):
    answer = []
    t = total // num
    while (True) :
        sum = 0
        for i in range (t,t+num,1) :
            sum += i
        if sum > total :
            t -= 1
        elif sum < total :
            t += 1
        else :
            break
    for i in range (t,t+num,1) :
        answer.append(i)
    return answer