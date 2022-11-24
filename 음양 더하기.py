def solution(absolutes, signs):
    signs = list(map(str, signs))
    for i in range (len(signs)) :
        if "False" in signs[i] :
            absolutes[i] *= -1
    return sum(absolutes)