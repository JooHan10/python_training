def solution(num_list, n):
    result_list = []
    for i, j in enumerate(num_list):
        if i < n:
            result_list.append(j)
    return result_list

# 다른 사람 풀이 1
def solution(num_list, n):
    return [v for i,v in enumerate(num_list) if i<n]

# 다른 사람 풀이 2
def solution(num_list, n):
    return num_list[:n]