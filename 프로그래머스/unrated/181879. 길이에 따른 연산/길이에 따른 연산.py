def solution(num_list):
    if len(num_list) >= 11:
        sum = 0
        for i in range(len(num_list)):
            sum += num_list[i]
        return sum
    elif len(num_list) <= 10:
        by = 1
        for i in range(len(num_list)):
            by *= num_list[i]
        return by