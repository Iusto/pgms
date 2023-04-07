import re

def solution(files):
    a = sorted(files, key=lambda x : int(re.findall('\d{1,5}', x)[0])) 
    # 한 글자에서 최대 다섯 글자 사이 짝대기 뒤에 숫자패턴으로 정렬
    b = sorted(a, key=lambda x : re.split('\d{1,5}', x.lower())[0])
    # 짝대기 앞에 알파벳 패턴 분리 후 정렬, 문자열 비교 대소문자 구분 안함
    return b