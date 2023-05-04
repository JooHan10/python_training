def solution(my_string):
    answer = ''
    str_list = list(my_string)
    for my_str in str_list:
        if my_str == my_str.upper():
            answer += my_str.lower()
        elif my_str == my_str.lower():
            answer += my_str.upper()
    return answer