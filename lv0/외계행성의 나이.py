def solution(age):
    age = list(map(int, str(age)))
    for i in range (len(age)) :
        age[i] += 97
    for i in range (len(age)) :
        age[i] = chr(age[i])
    return "".join(age)