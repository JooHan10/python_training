# 내 풀이
def solution(my_str, target):
    if target in my_str:
        return int(True)
    else:
        return int(False)

# 다른 사람 풀이
def solution(my_str, target):
    return 1 if target in my_str else 0