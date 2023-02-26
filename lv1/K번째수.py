def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command #[2,5,3]
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer