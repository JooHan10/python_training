def solution(number, limit, power):
    divisors_count = [0] * (number + 1)
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisors_count[j] += 1

    result = 0
    for i in range(1, number + 1):
        if divisors_count[i] > limit:
            result += power
        else:
            result += divisors_count[i]

    return result

number = 5
limit = 3
power = 2

print(solution(number, limit, power))