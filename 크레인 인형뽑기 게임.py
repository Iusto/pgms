def solution(board, moves):
    answer = 0
    stack = []
    for i in moves :
        for j in range (len(board)) :
            if board[j][i-1] != 0 : #0이 아닐때
                if len(stack) > 0 and stack[-1] == board[j][i-1] : #서로 같은숫자일 시
                    stack.pop()
                    answer+=2
                    board[j][i-1] = 0
                    break
                else :
                    stack.append(board[j][i-1])
                    board[j][i-1] = 0
                    break
    return answer