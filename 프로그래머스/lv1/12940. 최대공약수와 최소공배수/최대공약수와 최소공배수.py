def solution(n, m):
    gcd_n = n
    gcd_m = m
    answer = []
    
    while gcd_m:
        gcd_n, gcd_m = gcd_m, gcd_n % gcd_m
        if gcd_m == 0:
            gcd = gcd_n
            answer.append(gcd)
            lcm = (n * m) // answer[0]
            answer.append(lcm)
    
    return answer