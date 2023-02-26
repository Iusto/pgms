def solution(dots):
    answer = 0
    dots.sort()
    first_x = dots[0][0]
    first_y = dots[0][1]

    second_x = dots[1][0]
    second_y = dots[1][1]

    third_x = dots[2][0]
    third_y = dots[2][1]

    fourth_x = dots[3][0]
    fourth_y = dots[3][1]

    # case1 : 두번째 값과 직선
    if (first_y - second_y) != 0 and (third_y - fourth_y) != 0:
        if (first_x - second_x) / (first_y - second_y) == (third_x - fourth_x) / (third_y - fourth_y):
            answer = 1
            return answer

    # case2 : 세번째 값과 직선
    if (first_y - third_y) != 0 and (second_y - fourth_y) != 0:
        if (first_x - third_x) / (first_y - third_y) == (second_x - fourth_x) / (second_y - fourth_y):
            answer = 1
            return answer

    # case3 : 네번째 값과 직선
    if (first_y - fourth_y) != 0 and (third_y - second_y) != 0:
        if (first_x - fourth_x) / (first_y - fourth_y) == (third_x - second_x) / (third_y - second_y):
            answer = 1
            return answer
    if (first_y - second_y) == 0 and (third_y - fourth_y) == 0:
        answer = 1
        return answer
    if (first_y - third_y) == 0 and (second_y - fourth_y) == 0:
        answer = 1
        return answer
    if (first_y - fourth_y) == 0 and (third_y - second_y) == 0:
        answer = 1
        return answer

    return answer