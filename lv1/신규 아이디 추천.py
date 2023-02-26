import re
def solution(new_id):
    #1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    #2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    answer = re.sub('[^0-9a-z_.-]+','',new_id.lower())
    #3단계 . 2번 이상을 1개로 압축
    answer = re.sub('\.\.+','.',answer)
    #4단계 양끝 . 제거
    answer = answer.strip('.')
    #5단계 빈문자열 a 추가
    if len(answer) == 0 : answer='a'
    #6단계 15개제외하고 문자모두제거, 우측 . 제거
    answer = answer[:15].rstrip('.')
    #7단계 길이 3 될 때까지 끝 문자 추가    
    answer+=answer[-1]*(3-len(answer))
    
    # +=A*3라면 "A" 3번 붙인다는 뜻, 음수면 아무것도 하지 않는다
        
    return answer