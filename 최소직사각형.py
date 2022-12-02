def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
    #60 70 60 80중에서 max(80) / 50 30 30 40 중에서 max(50)