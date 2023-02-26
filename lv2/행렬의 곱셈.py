def solution(arr1, arr2):                                 #arr1행의 수 * arr2열의 수
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))] #곱한 결과의 행렬 크기 0으로 초기화
    for i in range(len(arr1)): #arr1 행의 크기             
        lists = []
        for j in range(len(arr2[0])): ##arr2 열 크기
            for k in range(len(arr1[0])): #arr1 열 크기
                answer[i][j] += arr1[i][k] * arr2[k][j] #행렬 곱셈 과정을 코딩으로 나타낸 것
    return answer