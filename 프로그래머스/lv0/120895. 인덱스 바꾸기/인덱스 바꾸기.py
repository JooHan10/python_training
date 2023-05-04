def solution(my_string, num1, num2):
    answer = ''
    str_list = list(my_string)
    str_list[num1],str_list[num2] = str_list[num2],str_list[num1]
    answer = ''.join(str_list)
    return answer

t1 = "hello"
t2 = 1
t3 = 2
print(solution(t1, t2, t3))