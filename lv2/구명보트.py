def solution(people, limit) :
    answer = 0
    people.sort() # [50,50,70,80]

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit : # 투포인터 탐색
            a += 1                          # 80 + 50 <= 100 (F) a = 0, b = 3
            answer += 1                     # 70 + 50 <= 100 (F) a = 0, b = 2
        b -= 1                              # 50 + 50 <= 100 (T) a = 0, b = 1
    return len(people) - answer             # a = 1, b = 1 (break)