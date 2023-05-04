def solution(my_string):
    str_list = []
    for str in my_string:
        if str not in str_list:
            str_list.append(str)
    answer = "".join(s for s in str_list)
    return answer