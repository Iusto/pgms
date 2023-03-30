def solution(record):
    answer = []
    result = []
    dict = {}
    for i in record :
        temp = i.split()
        if temp[0] == "Enter" :
            dict[temp[1]] = temp[2]
            answer.append([temp[0],temp[1]])
        if temp[0] == "Leave" :
            answer.append([temp[0],temp[1]])
        if temp[0] == "Change" :
            dict[temp[1]] = temp[2]
    for i in answer :
        if i[0] == 'Enter' :
            result.append(dict[i[1]] + "님이 들어왔습니다.")
        if i[0] == 'Leave' :
            result.append(dict[i[1]] + "님이 나갔습니다.")
    return result