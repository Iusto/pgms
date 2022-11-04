def solution(quiz):
    answer = []
    for i in quiz:
        c = i.split(' = ')
        if eval(c[0]) == eval(c[1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer