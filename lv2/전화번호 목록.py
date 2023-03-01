def solution(phone_book):
    # 1. Hash map을 만든다
    hash_map = {}
    for i in phone_book:
        hash_map[i] = 1
    
    # 2. 접두어가 Hash map에 존재하는지 찾는다
    for i in phone_book:
        jubdoo = ""
        for j in i:
            jubdoo += j
            # 3. 접두어를 찾아야 한다 (기존 번호와 같은 경우 제외)
            if jubdoo in hash_map and jubdoo != i:
                return False
    return True
