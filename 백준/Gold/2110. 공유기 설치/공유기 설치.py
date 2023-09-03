from sys import stdin

def solution():
    input = stdin.readline
    N, C = map(int, input().split())
    houses = [int(input()) for _ in range(N)]
    
    houses.sort()
    router_distance_min = 1
    router_distance_max = houses[-1] - houses[0]
    result = 0

    while router_distance_min <= router_distance_max:
        mid = (router_distance_min + router_distance_max) // 2
        router_count = 1
        last_installed = houses[0]

        for house in houses:
            if house - last_installed >= mid:
                router_count += 1
                last_installed = house

        if router_count >= C:
            result = mid
            router_distance_min = mid + 1
        else:
            router_distance_max = mid - 1

    return result

print(solution())