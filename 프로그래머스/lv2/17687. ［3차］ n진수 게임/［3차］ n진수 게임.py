def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base)

    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]

def solution(n, t, m, p):
    result = ''
    answer = ''
    i = -1
    
    while i < (p-1) + (m * t):
        i += 1
        result += str(convert(i, n))

    for i in range(len(result)):
        answer += result[(p-1) + (m * i)]
        if len(answer) == t:
            break

    return answer