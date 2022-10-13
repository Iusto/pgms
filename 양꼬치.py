def solution(n, k):
    answer = (n * 12000) + (k * 2000) - (n * 12000 // 120000 * 2000)
    return answer