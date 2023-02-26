import numpy as np
def solution(num_list, n):
    li = np.array(num_list).reshape(-1,n) 
    # -1은 행(row)의 위치에 -1을 넣고 열의 값을 지정해주면 
    # 변환될 배열의 행의 수는 알아서 지정이 된다는 소리이다.
    return li.tolist()