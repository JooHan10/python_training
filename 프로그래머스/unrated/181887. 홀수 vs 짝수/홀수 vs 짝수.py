def solution(num_list):
    d_num = 0
    s_num = 0
    for num in range(len(num_list)):
        if num % 2 == 0:
            d_num += num_list[num]
        elif num % 2 != 0:
            s_num += num_list[num]
    if d_num > s_num:
        return d_num
    else:
        return s_num