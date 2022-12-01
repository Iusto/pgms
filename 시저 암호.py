import re

def solution(s, n):
    answer = ""
    for i in s :
        if 90 >= ord(i) >= 65 : #대문자
            if ord(i) + n > 90 :
                answer+=(chr(ord(i) + n - 26))
            else :
                answer+=(chr(ord(i) + n))
        else : #소문자
            if ord(i) + n > 122 :
                answer+=(chr(ord(i) + n - 26))
            else :
                answer+=(chr(ord(i) + n))
    return re.sub(r"[^a-zA-Z]", " ", answer)
