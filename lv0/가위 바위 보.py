def solution(rsp):
    for i in range (len(rsp)) :
        if rsp[i] == 0 :
            rsp[i] = 5
        if rsp[i] == 2 :
            rsp[i] = 0
        if rsp[i] == 5 :
            rsp[i] = 2
    return rsp