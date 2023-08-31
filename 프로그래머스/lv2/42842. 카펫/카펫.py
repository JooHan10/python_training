def solution(brown, yellow):
    for i in range(1, yellow+1):
        if (yellow % i == 0):
            yellow_width = int(yellow / i)
            yellow_length = i
            if (2 * (yellow_width + yellow_length) + 4 == brown):
                return [yellow_width +2, yellow_length+2]