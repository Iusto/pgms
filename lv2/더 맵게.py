import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    answer = 0
    if scoville[0] >= K:
        return answer
    while scoville[0] < K :
        if len(scoville) == 1:
            return -1
        first = hq.heappop(scoville)
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  
    return answer