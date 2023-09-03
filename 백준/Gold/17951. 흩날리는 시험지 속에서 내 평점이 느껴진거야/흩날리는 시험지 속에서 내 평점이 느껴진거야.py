from sys import stdin

def solution():
    input = stdin.readline
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    
    score_min = 1
    score_max = 20*(10**5)
    result = 0
    
    while score_min <= score_max:
        mid = (score_min + score_max) // 2
        group_count = 0
        group_score = 0
        
        for score in scores:
            group_score += score
            if group_score >= mid:
                group_score = 0
                group_count += 1
            
        if group_count >= K:
            score_min = mid + 1
            result = mid
        else:
            score_max = mid - 1
    
    return result

print(solution())