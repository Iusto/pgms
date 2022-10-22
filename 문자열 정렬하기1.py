import re
def solution(my_string):
    return list(map(int, sorted(re.findall(r'\d', my_string))))