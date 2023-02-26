def solution(n):
    result = 0
    for i in range (1,100) :
        if(6*i % n) == 0 :
            result = i
            break;
    return result