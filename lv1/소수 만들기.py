from itertools import combinations as cb
def solution(nums):
    answer = 0
    for a in cb(nums, 3):
        cbs = sum(a)
        for j in range(2, cbs):
            if cbs % j== 0: # 1부터 자기자신을 제외한 숫자들의 나머지가 모두 0이어야 소수
                break
        else:
            answer += 1
    return answer