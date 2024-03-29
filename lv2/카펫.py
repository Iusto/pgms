def solution(brown, yellow):
    answer = []
    for col in range(3, brown//2): # 갈색 최소길이가 3임
        if (brown//2-col+2-2) * (col-2) == yellow:
            return [brown//2-col+2, col]
    # 노란색(가운데)의 격자 수(넓이)는 (갈색 가로 길이-2)*(갈색 세로 길이-2)
    # 갈색 가로 길이는 (총 갈색 격자 수//2 - 갈색 세로 길이 + 2)
    # 반복문을 수행하다가 (갈색 가로 길이-2)*(갈색 세로 길이-2) == 노란색의 넓이(격자 수) 인 경우
    # 갈색의 가로 길이, 갈색의 세로 길이 배열을 반환
    
    # +2가 필요한 이유는 양 끝의 세로 격자 1개씩 추가해야 하기 때문
    # 가로4개에서 양쪽 세로를 빼면 2개가 빠짐