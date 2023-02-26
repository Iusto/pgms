def solution(num):
    answer = 0
    for i in range(1, num + 1):
        s = 0
        while s < num:
            s += i
            print(s)
            i += 1
            print(i)
        if s == num:
            answer += 1


    return answer