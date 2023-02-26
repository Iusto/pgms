def solution(a, b):
    answer = 0
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for i in range(a-1):
        answer += months[i] #5월이면 1~5까지 일수로 전부 합침
    
    answer += b-1 #인덱스가 0부터 시작이므로 -1
    answer = answer%7 #7로 나누어 나머지가 4이라면 토일월화이므로 화요일이 됨
    
    return days[answer]