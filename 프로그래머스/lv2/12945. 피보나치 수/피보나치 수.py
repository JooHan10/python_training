def solution(n):
    result = []
    
    for i in range(n+1):
        if i==0 or i==1:
            result.append(i)
        else:
            f = result[i-1] + result[i-2]
            result.append(f % 1234567)

    return result[-1]