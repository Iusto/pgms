def solution(cipher, code):
    list_cipher = list(cipher)
    answer = []
    for i in range(code-1, len(cipher), code) :
        answer.append(list_cipher[i])
    return "".join(answer)