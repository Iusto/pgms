def solution(k, m, score):
    answer = 0
    score.sort(reverse=True) #내림차순으로 정렬
    apple_box = []
    for i in range(0, len(score), m): #m만큼 apple_box를 담음, 나머지도 담음
        apple_box.append(score[i:i+m])
    for apple in apple_box:
        if len(apple) == m: #m만큼의 길이만 answer에 합치기
            answer += min(apple) * m #(최저 사과 점수) x (한 상자에 담긴 사과 개수) x (상자의 개수)
    return answer