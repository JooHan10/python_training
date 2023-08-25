import sys

n, k = [int(item) for item in sys.stdin.readline().split()]
arr_A = [int(item) for item in sys.stdin.readline().split()]

def selection_sort(n, k, arr_A):
    count = 0
    
    if n < k:
        return -1
    
    for i in range(n - 1, 0, -1):
        max_idx = i
        
        for j in range(i):
            if arr_A[j] > arr_A[max_idx]:
                max_idx = j
        
        if max_idx != i:
            arr_A[i], arr_A[max_idx] = arr_A[max_idx], arr_A[i]
            count += 1
            if count == k:
                return f'{arr_A[max_idx]} {arr_A[i]}'

    return -1

print(selection_sort(n, k, arr_A))