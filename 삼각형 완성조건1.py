def solution(sides):
    m = max(sides)
    sides.remove(max(sides))
    if sum(sides) > m :
        return 1
    else : 
        return 2