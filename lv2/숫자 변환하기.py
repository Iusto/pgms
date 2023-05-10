def solution(x, y, n):
    answer = 0
    s = set([x])
    
    while s :
        if y in s :
            return answer
        nxt = set() #딕셔너리는 순회시 크기가 변경되면 오류가 나므로 추가로 선언
        for i in s :
            if i + n <= y :
                nxt.add(i+n)
            if i * 2 <= y :
                nxt.add(i*2)
            if i * 3 <= y :
                nxt.add(i*3)
        s = nxt #순회완료 시 S에 값을 넘겨주고 y가 될 때까지 반복
        answer += 1
    return -1