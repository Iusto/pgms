def solution(name, yearning, photo):
    answer = []
    for i in photo :
        result = 0
        for j in name :
            if j in i :
                result += yearning[name.index(j)]
        answer.append(result)
    return answer