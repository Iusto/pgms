from itertools import permutations

def solution(k, dungeons):
    dun_num = len(dungeons)
    answer = 0

    for permut in permutations(dungeons, dun_num):
        hp = k
        count = 0
        for pm in permut:
            if hp >= pm[0]:
                hp -= pm[1]
                count += 1
        if count > answer:
            answer = count
    return answer


#-----------------------------------------------------------------------


answer = 0

def dfs(k, cnt, dungeons, visited):
    global answer 
    if cnt > answer:
        answer = cnt
    
    for i in range(len(dungeons)):
        print(visited)
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], cnt + 1, dungeons, visited)
            visited[i] = False
        
def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer