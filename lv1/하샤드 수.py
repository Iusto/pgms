def solution(x):
    sum = 0
    arr = list(str(x))
    for i in range (len(arr)) :
        sum += int(arr[i])
    answer = x % sum == 0
    return answer