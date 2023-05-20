def solution(s, n):
    lower_str = "abcdefghijklmnopqrstuvwxyz"
    upper_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''

    for str in s:
        if str in lower_str:
            idx = lower_str.find(str) + n 
            answer += lower_str[idx % 26]
        
        elif str in upper_str:
            idx = upper_str.find(str) + n 
            answer += upper_str[idx % 26]
        
        else:
            answer += " "
    return answer