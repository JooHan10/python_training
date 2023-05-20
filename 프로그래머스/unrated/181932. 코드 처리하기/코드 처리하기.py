def solution(code):
    ret = ""
    mode = 0

    for i, j in enumerate(code):
        if mode == 0:
            if j != "1":
                if i % 2 == 0:
                    ret += (j)
            elif j == "1":
                mode = 1

        elif mode == 1:
            if j != "1":
                if i % 2 == 1:
                    ret += (j)
            elif j == "1":
                mode = 0

    if ret == "":
        return "EMPTY"
    else: 
        return ret 