def solution(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    fst_num = sorted_numbers[0]
    snd_num = sorted_numbers[1]
    answer = fst_num * snd_num
    return answer