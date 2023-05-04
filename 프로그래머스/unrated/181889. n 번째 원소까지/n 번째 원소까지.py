def solution(num_list, n):
    result_list = []
    for i, j in enumerate(num_list):
        if i < n:
            result_list.append(j)
    return result_list