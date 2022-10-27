def solution(numbers, k):
    n = 1
    i = 1
    while (n < k) :
        n += 1
        i += 2
        if i > len(numbers) :
            i = i - len(numbers)
    return numbers[i-1]