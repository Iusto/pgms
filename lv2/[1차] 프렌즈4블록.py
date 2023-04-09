def solution(m, n, board):
    for i in range (m) :
        board[i] = list(board[i])
    cnt = 0
    rm = set() # 제거해야하는 블록 좌표 기록, 중복좌표를 제거하면서 추가하도록 set()으로 선언
    while True:
        # 보드를 순회하며 4블록이 된 곳의 좌표를 집합에 기록
        for i in range(m-1):
            for j in range(n-1):
                t = board[i][j]
                if t == []:
                    continue
                if board[i+1][j] == t and board[i][j+1] == t and board[i+1][j+1] == t:
                    rm.add((i,j))
                    rm.add((i+1,j))
                    rm.add((i,j+1))
                    rm.add((i+1,j+1))
        # 좌표가 존재한다면 집합의 길이만큼 세주고 블록을 지움 
        if rm:
            cnt += len(rm)
            for i,j in rm:
                board[i][j] = []
            rm = set()
        # 없다면 함수 종료
        else:
            return cnt
        
        # 블록을 위에서 아래로 당겨줌 (반복)
        while True:
            moved = False
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j]==[]:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved = True
            if moved == False: # 더이상 아래로 당길 블럭이 없다면 루프에서 벗어남
                break

# <순서>
# 1. 보드를 순회하며 4블록이 된 곳의 좌표를 집합에 기록
# 2. 좌표가 존재한다면 집합의 길이만큼 세주고 블록을 지움
# 3. 블록을 위에서 아래로 당겨줌
# 4. 보드를 순회하며 4블록이 된 곳의 좌표를 집합에 기록
# 5. 4블록이 된 곳이 없다면 cnt값 리턴하며 함수 종료