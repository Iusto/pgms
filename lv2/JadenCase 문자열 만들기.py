def solution(s):
    answer = []
    words = s.split(' ')
    for i in words :
        answer.append(i.capitalize()) #문자열의 첫글자는 대문자로, 나머지는 소문자로 변환
    return ' '.join(answer)

# capitalize() 문자열의 첫글자는 대문자로, 나머지는 소문자로 변환
# print ( 'HELLO WORLD!'.capitalize() ) # Hello world!

# [추가지식]
# title() 문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자로, 나머지는 소문자로 변환한다.
# print( 'FooBar'.title() ) # Foobar

# [한줄컷]
# return ' '.join([word.capitalize() for word in s.split(" ")])