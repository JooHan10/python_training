def solution(my_str):
    my_list = list(my_str)
    my_list.reverse()
    new_str = ""
    for i in my_list:
        new_str += i
    print(new_str)

solution("ProgrammerS123")