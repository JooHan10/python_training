def solution(rsp):
    answer = ""
    rsp_list = list(rsp)
    for i in rsp_list:
        if int(i) == 2:
            answer += "0"
        elif int(i) == 0:
            answer += "5"
        elif int(i) == 5:
            answer += "2"
    return answer