import heapq

def solution(scoville, K):
    scoville_heap = []
    for scov in scoville:
        heapq.heappush(scoville_heap, scov)

    cnt = 0
    while scoville_heap[0] < K:
        heapq.heappush(scoville_heap, heapq.heappop(scoville_heap) + heapq.heappop(scoville_heap) * 2)
        cnt += 1
        
        if len(scoville_heap) == 1 and scoville_heap[0] < K:
            return -1
    return cnt