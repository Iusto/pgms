def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] : 
            #끝말과 첫말이 같지않거나 중복일경우
            return [(i%n)+1, (i//n)+1] #번호, 차례
    else:
        return [0,0]