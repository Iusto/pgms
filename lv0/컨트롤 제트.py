def solution(s):
    arr = s.split(' ')
    result =[]
    for i in arr :
        if i=='Z':
            if len(result) != 0 :
                result.pop()
        else:
            result.append(int(i))
    return sum(result)