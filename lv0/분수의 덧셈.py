import math
def solution(denum1, num1, denum2, num2):
    gcd = math.gcd(num1,num2) #최대공약수
    lcm = int((num1*num2) / gcd) #최소공배수

    denum1 = (lcm/num1) * denum1
    denum2 = (lcm/num2) * denum2
    result = int(denum1+denum2)

    if math.gcd(result,lcm) != 1: #약분되는 경우 6/20 => 3/10
        a = int(result/int(math.gcd(result,lcm)))
        b = int(lcm/int(math.gcd(result,lcm)))
        return [a,b]
    return [result,lcm]