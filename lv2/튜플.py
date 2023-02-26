import re
from collections import Counter
def solution(s):
    s = Counter(re.findall('\d+',s))
    return list(map(int, [key for key, value in (sorted (s.items(), key = lambda x: x[1], reverse = True))]))