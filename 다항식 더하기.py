import re
def solution(polynomial):
    a = polynomial.split('+')
    x = []
    n = []
    sumX = 0
    sumN = 0
    plus = " + "
    for i in a :
        if 'x' in i :
            x.append(i.replace("x","*1").strip())
        else :
            n.append(int(i))
    for i in range (len(x)) :
        x[i] = re.sub('^[*]', '', x[i])
    for i in x :
        sumX += int(eval(i))
    for i in n :
        sumN += i
        
    if sumX > 1 :
        sumX = "%dx" %sumX
    if sumX == 1 :
        sumX = "x"
    if sumX == 0 or sumN == 0 :
        plus = ""
    if sumX == 0 :
        sumX = ""
    if sumN == 0 :
        sumN = ""
    
    return str(sumX) + str(plus) + str(sumN)
    