from itertools import permutations, combinations
def solution(babbling):
    answer = 0
    a = ['aya','ye','woo','ma']
    ret = []
    for i in range(2,5): # i가 순차적으로 2 3 4
        for t in list(combinations(a,i)): 
        # 'aya','ye','woo','ma' 중에서 2개 3개 4개를 취한 조합
            ret+=([''.join(s) for s in list(permutations(t))]) 
        # 'ayaye', 'yeaya', 'ayawoo', 'wooaya' 식으로 조합해서 추가할 때마다 새로운 list로 생성
    for s in babbling: # babbling중에서 ret과 a 값이 같은것이 존재때마다 answer +1
        if s in ret+a :
            answer+=1
    return answer