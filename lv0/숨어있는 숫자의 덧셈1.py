import re

def solution(my_string):
    numbers = re.findall(r'\d', my_string)
    answer = sum(list(map(int, numbers)))
    return answer