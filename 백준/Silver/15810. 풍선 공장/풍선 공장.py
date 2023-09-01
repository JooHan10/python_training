def solution():
    N, M = map(int, input().split())
    times = list(map(int, input().split()))

    time_min = (M // N) * min(times)
    time_max = (M // N + 1) * max(times)
    result = 0
    
    while time_min <= time_max:
        mid = (time_min + time_max) // 2
        count = 0
        
        for time in times:
            count += mid // time

        if count < M:
            time_min = mid + 1
        else:
            result = mid
            time_max = mid - 1

    return result

print(solution())