def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []
    for i in range(len(numbers)-1):
        stack.append([i, numbers[i]])
        while stack:
            if stack[-1][1] < numbers[i+1]:
                f_idx, f_num = stack.pop()
                answer[f_idx] = numbers[i+1]
            else:
                break
    return answer

# 현재 숫자보다 다음 숫자가 크지 않다면 break해서 인덱스만 스택에 저장
# 뒤에 큰 수가 크다면 스택에 저장되어있는 인덱스중 뒤에 큰수보다 작은 인덱스들만 입력
# 뒤에 오는 숫자보다 큰 숫자는 break되고 작은 숫자들은 입력되며 입력된 숫자들은 삭제처리

# 과정

# stack = [0,9] 저장됨, [0,9]가 [1,1]보다 크므로 break됨
# stack =[[0,9],[1,1]] 저장됨, [1,1]이 [2,5]보다 작음, 입력된 인덱스 [2,5]는 삭제
# 하지만 [0,9]는 [2,5]보다 크므로 break가 된다. stack = [0,9] 유지