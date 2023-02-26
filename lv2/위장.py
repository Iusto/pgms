def solution(clothes):
    from collections import Counter
    answer = 1
    cnt = Counter([kind for name, kind in clothes])
    print(cnt.values())
    for i in cnt.values() :
        answer = answer * (i + 1)
    return answer - 1
    # (heargear + 1) * (eyewear + 1) - 1
    # 부위 별로 아무것도 안입는 경우가 있으니 +1을 해준다. (yellow_hat, green_turban, 안입음)
    # 모두 안입는 경우는 없으니 최종 곱한 값에서 -1을 해준다.