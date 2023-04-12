from collections import deque

def solution(maps):
    answer = 0

    # 상하좌우
    move = [
        [0, 1],
        [0, -1],
        [-1, 0],
        [1, 0]
    ]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        # queue가 빌 때까지 반복
        while queue:
            x, y = queue.popleft()
            #x,y는 현재 좌표

            # 상하좌우 칸 확인하기
            for mx, my in move: # move x, move y
                nx = x + mx
                ny = y + my
                #nx, ny는 이동할 다음 좌표

                # 맵을 벗어나면 무시하기
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): 
                    continue

                # 벽이면 무시하기
                if maps[nx][ny] == 0: 
                    continue

                # 처음 지나가는 길이면 거리계산하고 다시 상하좌우 확인하기
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))    # 재귀
                    # 현재 좌표 (x,y)에서 이동할 다음 좌표(nx, ny)에 +1을 해서 거리 계산

        # 상대 팀 진영(제일 오른쪽 아래 칸)까지의 거리 반환
        return maps[len(maps)-1][len(maps[0])-1]

    answer = bfs(0, 0) # 0,0부터 시작
    
    # 상대 팀 진영에 도착할 수 없을 때 -1
    if answer == 1 :
        return -1 
    else :
        return answer    
           