def solution(keymap, targets):
    answer = []
    hs = {}
    #인덱스 사전
    for k in keymap:
        for i, ch in enumerate(k):
            if ch in hs :
                hs[ch] = min(i + 1, hs[ch]) 
            else : 
                hs[ch] = i + 1

    for i, t in enumerate(targets):
        ret = 0
        for ch in t:
            if ch not in hs: #사전에 없을 시 -1
                ret = - 1
                break
            ret += hs[ch]
        answer.append(ret)

    return answer