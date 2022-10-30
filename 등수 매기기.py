def solution(score):
    dict = {}
    temp = []
    for i in score:
        temp.append(sum(i)/2)
    for i, value in enumerate(sorted(temp,reverse=True), start=1): 
        #평균값을 기준으로 내림차순 정렬하여 인덱스 차례대로 1부터 추가
        if value not in dict: #해당 평균값이 dict에 없다면 value값과 인덱스를 추가
            dict[value] = i  #dict[200] = 10이면 200 key값과 10 value값 추가
    return [dict[i] for i in temp] #평균값대로 인덱스 리턴