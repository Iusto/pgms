def solution(chicken):
    answer = 0
    while chicken >= 10:
        chicken, mod = divmod(chicken, 10)
        # divmod(10, 3), 10을 3으로 나누면 몫이 3과 나머지 1을 튜플 형식으로
        # (3, 1)로 반환 하는 함수
        answer += chicken
        chicken += mod
    return answer