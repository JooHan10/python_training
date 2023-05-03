# 내 풀이 1
def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    else:
        return 0

# 내 풀이 2
def solution(number, n, m):
    if number % n ==0:
        if number % m == 0:
            return 1
        else:
            return 0
    else:
        return 0