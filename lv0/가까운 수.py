def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n)) #람다 함수 1번째 abs(x-n)정렬, 2번째 x-n정렬
    return array[0]