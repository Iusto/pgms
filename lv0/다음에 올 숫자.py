def solution(common):
    answer = 0
    a,b,c = common[:3] #1번째부터 3번째 값까지 차례대로 할당
    if (b-a == c-b): #1번째와 2번째 차가 3,4차가 같다면 등차수열
        answer = common[-1]+(b-a) #맨끝의 값에 차를 더함
    elif (b/a == c/b): #1번째와 2번째 비가 3,4차가 같다면 등차수열
        answer = common[-1]*(b/a) #맨끝의 값에 비를 더함
    return answer