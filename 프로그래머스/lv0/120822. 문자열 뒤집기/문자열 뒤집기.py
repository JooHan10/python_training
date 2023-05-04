def solution(my_string):
    answer = ""
    my_string_list = list(my_string)
    for i in range(len(my_string_list)):
        answer += my_string_list.pop()
    return answer