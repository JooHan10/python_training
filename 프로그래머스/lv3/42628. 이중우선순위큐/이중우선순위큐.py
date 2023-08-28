import heapq

def solution(operations):
    result = []
    new_list = []
    
    for operation in operations:
        D_or_I, num = operation.split() 
        num = int(num)
        
        if D_or_I == 'I':
            heapq.heappush(new_list, num)
        elif D_or_I == 'D' and num == 1:
            if len(new_list) != 0:
                max_value = max(new_list)
                new_list.remove(max_value)
        else:
            if len(new_list) != 0:
                heapq.heappop(new_list)
    
    if len(new_list) == 0:
        result = [0, 0]
    else:
        result = [max(new_list), heapq.heappop(new_list)]
        
    return result

