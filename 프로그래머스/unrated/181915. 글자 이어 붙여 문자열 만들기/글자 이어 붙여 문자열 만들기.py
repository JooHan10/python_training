def solution(my_str, index_list):
    answer = ''
    test_list = list(my_str)
    for i in index_list:
        answer += test_list[i]
    return answer