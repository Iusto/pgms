d = {chr(i) : i-64 for i in range(65,91)} # 사전

def solution(msg):
    answer = []
    while True:  # KAKAO AKAO KAO O
        if msg in d: # 마지막 확인하는 단어가 사전에 있을 시
            answer.append(d[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d)+1 # 사전에 없는 단어 추가
                msg = msg[i-1:]
                break
    return answer