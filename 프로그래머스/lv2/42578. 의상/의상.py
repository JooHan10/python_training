def solution(clothes):
    type_dict = {}
    for _, type in clothes:
        type_dict[type] = type_dict.get(type, 0) + 1
        
    combination = 1
    for type in type_dict:
        combination *= (type_dict[type] + 1)
        
    answer = combination - 1
    return answer