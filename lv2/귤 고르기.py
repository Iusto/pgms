from collections import Counter
def solution(k, tangerine):
    answer = 0
    # [1] 자료 변환 
    
    #for key, value in Counter(tangerine).items() :
        #print(key, value)

    count = sorted(Counter(tangerine).items(),reverse = True, key = lambda x : x[1])
    
    # [2] 최소 종류 계산
    for key, value in count:
        print(k)
        if k <= 0 : 
            break
        k -= value
        answer += 1
    return answer