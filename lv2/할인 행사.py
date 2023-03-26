def solution(want, number, discount):
    answer = 0
    shopping_list = {}
    for i in range(len(want)) :
        shopping_list[want[i]] = number[i]
    from collections import Counter
    shopping_list = Counter(shopping_list)
    for i in range(len(discount)-9) :
        sale = Counter(discount[i:i+10])
        if len(shopping_list - sale) == 0 :
            answer += 1
    return answer