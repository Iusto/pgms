a, b = map(int, input().strip().split(' '))
answer = ""
for i in range(b) :
    for j in range(a) :
        answer += "*"
    answer+="\n"
print(answer)