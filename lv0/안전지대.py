def solution(board):
    n = len(board)
    center = []
    sum = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                center.append([i,j])
    
    for i,j in center :
        if i-1 < 0 :
            i = 1
        if j-1 < 0 :
            j = 1
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                try:
                    board[x][y] = 1
                except :
                    pass
        
    for i in range (n) :
        for j in range (n) :
            if board[i][j] == 0 :
                sum += 1
    return sum