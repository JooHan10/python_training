def solution(my_string):
    str_list = list(my_string)
    append_str_list = []
    for i in str_list:
        ascii_str = ord(i)
        if ascii_str >= 48 and ascii_str <= 57:
            ascii_chr = int(chr(ascii_str))
            append_str_list.append(ascii_chr)

    answer = sorted(append_str_list)
    return answer