def solution(s):
    check = []
    for i in s:
        if i == "(":
            check.append(i)
        else:
            if check:
                check.pop()
            else:
                return False
    if check:
        return False
    return True