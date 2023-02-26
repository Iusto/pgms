def solution(hp):
    for i in range (5,-1,-2) :
        if i == 5:
            general = hp // 5
            hp = hp % 5
        if i == 3 :
            soldier = hp // 3
            hp = hp % 3
        if i == 1 :
            worker = hp // 1
    return general+soldier+worker