def solution(s):
    list_1 = list(map(int, s.split()))
    result = ""
    result += str(min(list_1)) + " "
    result += str(max(list_1))
    
    return result